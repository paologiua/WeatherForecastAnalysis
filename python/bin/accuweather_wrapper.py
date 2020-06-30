from datetime import datetime
import time
import json
import bs4
import requests
import re
import sys
import socket

def send_to_logstash(host, port, data):
    error = True
    while(error):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created. sock: " + str(sock))
        
            sock.connect((host, port))
            print("Socket connected to HOST: " + host + " PORT: " + str(port))
            print("Socket connected. Sock: " + str(sock))

            print("Sending message: " + str(data))

            sock.sendall(json.dumps(data).encode())
            print("End connection")
            sock.close()
            error = False
        except:
            print("Connection error. There will be a new attempt in 10 seconds")
            time.sleep(10)

def utc_now():
    return str(datetime.utcnow()).split('.')[0] + ' UTC'

def take_first_number(source):
    try:
        return take_all_numbers(source)[0]
    except:
        return "null"

def take_all_numbers(source):
    return [int(numeric_string) for numeric_string in re.findall("\d+", source)]

def getFloatNumber(integer, fractional):
    return float(str(integer) + '.' + str(fractional))

def extract_source(url):
     agent = {"User-Agent":"Mozilla/5.0"}
     source=requests.get(url, headers=agent).text
     return source

def extract_data(source):
    soup=bs4.BeautifulSoup(source, 'lxml')

    weather = soup.find("div", {"class": "current-conditions-card content-module non-ad"})

    details = weather.find("div", {"class": "list"})

    value = take_all_numbers(str(details))

    data = {
        'LocationTime': weather.find("p", {"class": "module-header sub date"}).next,
        'WeatherText': weather.find("div", {"class": "phrase"}).next,
        'Temperature': {
            'Value': take_first_number(weather.find("p", {"class": "value"}).next),
            'Unit': "C"
        },
        'RealFeelTemperature': {
            'Value': take_first_number(weather.find("p", {"class": "realFeel top"}).next),
            'Unit': "C"
        },
        'RealFeelTemperatureShade': {
            'Value': take_first_number(weather.findAll("p", {"class": "realFeel"})[1].next),
            'Unit': "C"
        },
        'UVIndex': value[0],   #without unit
        'Wind': { 
            'Direction': details.findAll("p")[1].next.split()[1],
            'Speed': { 
                'Value': value[1], 
                'Unit': 'km/h' 
            }
        },
        'WindGust': {
            'Speed': { 
                'Value': value[2], 
                'Unit': 'km/h' 
            }
        },
        'RelativeHumidity': value[3],   #%
        'IndoorRelativeHumidity': value[10],   #%
        'DewPoint': {
            'Value': value[4],
            'Unit': 'C'
        },
        'Pressure': {
            'Value': getFloatNumber(value[5], value[6]),
            'Unit': 'mb'  #mbar
        },
        'CloudCover': value[7],
        'Visibility': {
            'Value': value[8],
            'Unit': 'km'
        },
        'Ceiling': {
            'Value': value[9],
            'Unit': 'm'
        }
    }

    return data

def findIndexCountry(array, x):
    i = 0
    for country in array:
        if(str(country['Country']['EnglishName']).lower() == str(x).lower()):
            return i
        i = i + 1
    return -1

def main():
    if(len(sys.argv) != 3):
        sys.stderr.write('Use python3 ' + str(sys.argv[0]) + ' [location] [country]\n')
        sys.exit(-1)
    
    apiKey = 'vdGGbGbF1ODlSHzAwxCH4lUgibWIW2sy'
    location = str(sys.argv[1])
    search = json.loads(extract_source('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + apiKey + '&q=' + location))
    
    index = findIndexCountry(search, str(sys.argv[2]))
    if(index == -1):
        sys.stderr.write(location + ' not found\n')
        sys.exit(-1)
    
    search = search[index]

    print('Getting weather data from ' + search['LocalizedName'] + ', ' + search['Country']['LocalizedName'])

    url='https://www.accuweather.com/en/us/' + search['LocalizedName'] + '/' + str(search['Key']) + '/current-weather/' + str(search['Key'])
    while True:
        data = extract_data(extract_source(url))
        data = {
            'Source': 'AccuWeather',
            'LocalizedName': search['LocalizedName'], 
            'AdministrativeArea': search['AdministrativeArea']['LocalizedName'],
            'Country': search['Country']['LocalizedName'],
            'CurrentUTC': utc_now(),
            'Weather' : data
        }

        send_to_logstash('10.0.100.8', 5000, data)
        
        print('\n#######################\n')
        time.sleep(60)

if __name__ == "__main__":
    main()
