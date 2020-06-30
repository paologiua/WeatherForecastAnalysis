from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from pyspark.sql import SQLContext, SparkSession

from pyspark.sql.types import LongType, DoubleType
from pyspark.sql.functions import udf
from datetime import datetime

from pyspark.ml.linalg import Vectors 
from pyspark.ml.feature import VectorAssembler 

from pyspark.ml.regression import LinearRegression 

import time
from datetime import datetime, timedelta

from pyspark.sql import types as T
from pyspark.sql import Row
from pyspark.ml.linalg import VectorUDT, SparseVector,DenseVector

import json

from elasticsearch import Elasticsearch
import uuid

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "DataPrediction")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 1)
ssc.checkpoint("checkpoint")

#Elasticsearch data
elastic_host = "10.0.100.51"
elastic_index = "prediction"
elastic_document = "_doc"

# Create a DStream that will connect to Kafka
zooKeeperAddress = "10.0.100.22:2181"
topic = "processed-data"
lines =  KafkaUtils.createStream(ssc, zooKeeperAddress, "spark-mllib", {topic: 1})

def clearData(x):
    return x[0][1].replace("'",'"').replace('u"','"')[1:-1]

# Count each word in each batch
pairs = lines.map(lambda word: (word, 1))
windowedWordCounts = pairs.reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 60*5, 30) \
                          .filter(lambda x: True if x[1] != 0 else False) \
                          .map(clearData)

def jsonToDataFrame(records):
    spark = SparkSession.builder.getOrCreate()
    sc = spark.sparkContext

    return spark.read.json(sc.parallelize(records))

#Time functions
def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return int(unix_time(dt) * 1000)

def utcToInt(str):
    a = datetime.strptime(str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return long(unix_time_millis(a))

def utcNowPlusN(n):
    return str(datetime.utcnow() + timedelta(minutes = n)).replace(' ', 'T') + 'Z'

def createInputUtc(utc):
    spark = SparkSession.builder.getOrCreate()
    int_utc = (utcToInt(utc))
    print "timestamp: ", utc, "num_time: ", int_utc

    schema = T.StructType([T.StructField('features', VectorUDT())])
    return spark.createDataFrame([Row(features=DenseVector([int_utc]))], schema = schema)
###############

def getItemFromDataFrame(dataframe, column, index):
  return dataframe.select(column).collect()[index][column]

def predict(dataframe, something, time):
    iplookup_udf = udf(utcToInt)
    indexed = dataframe.withColumn("time", iplookup_udf("@timestamp").cast(LongType()))
    indexed.show(truncate=False)

    assembler = VectorAssembler(inputCols=['time'], outputCol='features') 
    output = assembler.transform(indexed) 

    final_data = output.select('features', something) 
    final_data.show(5) 

    train_data,test_data = final_data.randomSplit([0.7,0.3]) 
    print "###TRAIN DATA###"
    train_data.describe().show()
    print "###TEST DATA###" 
    test_data.describe().show() 

    lr = LinearRegression(featuresCol='features', labelCol=something) 
    trained_model = lr.fit(train_data) 

    #evaluating model trained for Rsquared error 
    results = trained_model.evaluate(train_data)
    print 'Rsquared Error :', results.r2 

    #testing Model on unlabeled data 
    #create unlabeled data from test_data 
    #testing model on unlabeled data 
    unlabeled_data = test_data.select('features') 
    unlabeled_data.show(5) 

    predictions=trained_model.transform(unlabeled_data) 
    predictions.show(truncate=False) 

    input = time
    input.show(5)
    predictions = trained_model.transform(input) 
    predictions.show(truncate=False) 
    return getItemFromDataFrame(predictions, 'prediction', 0)

def sendToElasticSearch(record):
    uuId = uuid.uuid4()
    print(uuId)
    try:
        response = Elasticsearch(hosts=[elastic_host]).index(
            index = elastic_index,
            doc_type = elastic_document,
            id = uuId,
            body = record,
        )
    except Exception as e:
        print(e)

def handler(message):
    records = message.collect()
    if(records != []):
        try:
            df = jsonToDataFrame(records)
            df.show(df.count(), truncate=False)

            str_plus_n = utcNowPlusN(5)
            input_dataframe = createInputUtc(str_plus_n)
            temperature_prediction = predict(df, 'temperature', input_dataframe)
            humidity_prediction = predict(df, 'humidity', input_dataframe)

            recordsJSON = json.loads(records[0])
            response = {
                'type': 'predicted_weather',
                '@timestamp': str_plus_n,
                'city': str(recordsJSON['city']),
                'country': str(recordsJSON['country']),
                'temperaturePlus5': temperature_prediction,
                'humidityPlus5': humidity_prediction
            }
            print response
            sendToElasticSearch(response)
        except Exception as e:
            print(e)

windowedWordCounts.foreachRDD(handler)

# Print the first ten elements of each RDD generated in this DStream to the console
windowedWordCounts.pprint()

ssc.start()
ssc.awaitTermination()

