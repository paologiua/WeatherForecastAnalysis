from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import json
from json import dumps

from kafka import KafkaProducer

import uuid

def getTemperature(d):
  return d['Weather']['Temperature']['Value'] if d['Source'] == 'AccuWeather' else d['Weather']['temperature']

def getHumidity(d):
  return d['Weather']['RelativeHumidity'] if d['Source'] == 'AccuWeather' else d['Weather']['relativeHumidity']

def getPressure(d):
  return d['Weather']['Pressure']['Value'] if d['Source'] == 'AccuWeather' else d['Weather']['pressureMeanSeaLevel']

def getUVIndex(d):
  return d['Weather']['UVIndex'] if d['Source'] == 'AccuWeather' else d['Weather']['uvIndex']

def getWindSpeed(d):
  return d['Weather']['Wind']['Speed']['Value'] if d['Source'] == 'AccuWeather' else d['Weather']['windSpeed']

def getWindDirection(d):
  if(d['Source'] == 'AccuWeather'):
    return {
        'N': 0,
        'NNE': 22.5,
        'NE': 45,
        'ENE': 67.5,
        'E': 90,
        'ESE': 112.5,
        'SE': 135,
        'SSE': 157.5,
        'S': 180,
        'SSW': 202.5,
        'SW': 225,
        'WSW': 247.5,
        'W': 270,
        'WNW': 292.5,
        'NW': 315,
        'NNW': 337.5
    }.get(d['Weather']['Wind']['Direction'])
  else:
    return d['Weather']['windDirection']



def data_cleaner(x):
  try:
    d = json.loads(x)

    return {
      'type': 'current_weather',
      'city': d['LocalizedName'],
      'country': d['Country'],
      '@timestamp': d['@timestamp'],
      'temperature': getTemperature(d),
      'humidity': getHumidity(d),
      'pressure': getPressure(d),
      'uvIndex': getUVIndex(d),
      'windSpeed': getWindSpeed(d),
      'windDirection': getWindDirection(d)
    }
  except:
    return {
      'type': None,
      'city': None,
      'country': None,
      '@timestamp': None,
      'temperature': None,
      'humidity': None,
      'pressure': None,
      'uvIndex': None,
      'windSpeed': None,
      'windDirection': None
    }

producer = KafkaProducer(bootstrap_servers=['kafkaServer:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def sendToKafka(record):
  producer.send('processed-data', record)
  producer.flush()

def handler(message):
  records = message.collect()
  for record in records:
    record = str(record)
    if(not 'None' in record):
      sendToKafka(record)

sc = SparkContext("local[2]", "DataCleaner")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 1)

zooKeeperAddress = "10.0.100.22:2181"
topic = "data"
kvs = KafkaUtils.createStream(ssc, zooKeeperAddress, "spark-processing", {topic: 1})
relevant_data = kvs.map(lambda x: data_cleaner(x[1]))

relevant_data.foreachRDD(handler)

relevant_data.pprint()

ssc.start()
ssc.awaitTermination()
