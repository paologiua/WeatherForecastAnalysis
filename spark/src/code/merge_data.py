from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import json
from json import dumps

from kafka import KafkaProducer
from elasticsearch import Elasticsearch

import uuid

elastic_host = "10.0.100.51"
elastic_index = "weather"
elastic_document = "_doc"

elasticSearch = Elasticsearch(hosts=[elastic_host])

def clearData(x):
    return x.replace("'",'"').replace('u"','"')

def getPrediction(timestamp, city):
  PARAMS = {"query": {"bool": {"must": [{"match": {"@timestamp": timestamp}},{"match": {"city": city}}]}}}
  result = elasticSearch.search(index="prediction", doc_type="_doc", body=PARAMS)['hits']['hits'][0]
  elasticSearch.delete(index="prediction", doc_type="_doc", id=result['_id'])
  return result


def sendToElasticSearch(record):
  uuId = uuid.uuid4()
  print(uuId)
  try:
    response = elasticSearch.index(
      index = elastic_index,
      doc_type = elastic_document,
      id = uuId,
      body = record,
    )
  except Exception as e:
    print(e)

def handler(message):
  records = message.collect()
  for record in records:
    record = clearData(str(record))[1:-1]
    record = json.loads(record)
    
    timestamp = str(record['@timestamp']).split(".")[0][0:-3]
    city = str(record['city'])
    try:
      prediction = clearData(str(getPrediction(timestamp,city)))
      prediction = json.loads(prediction)['_source']

      temperaturePlus5 = prediction['temperaturePlus5']
      humidityPlus5 = prediction['humidityPlus5']

      record['temperaturePlus5'] = temperaturePlus5
      record['humidityPlus5'] = humidityPlus5
    except Exception as e:
      print(e)
    sendToElasticSearch(record)
    print(json.dumps(record, indent=4))

sc = SparkContext("local[2]", "MergeData")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 1)

zooKeeperAddress = "10.0.100.22:2181"
topic = "processed-data"
kvs = KafkaUtils.createStream(ssc, zooKeeperAddress, "spark-merge", {topic: 1})
relevant_data = kvs.map(lambda x: clearData(x[1]))

relevant_data.foreachRDD(handler)

ssc.start()
ssc.awaitTermination()
