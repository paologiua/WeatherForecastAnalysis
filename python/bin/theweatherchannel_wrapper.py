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

def extract_source(url):
     agent = {"User-Agent":"Mozilla/5.0"}
     source=requests.get(url, headers=agent).text
     return source

def findIndexCountry(array, x):
    i = 0
    for country in array['country']:
        if(str(country).lower() == str(x).lower()):
            return i
        i = i + 1
    return -1

def main():
    if(len(sys.argv) != 3):
        sys.stderr.write('Use python3 ' + str(sys.argv[0]) + ' [location] [country]\n')
        sys.exit(-1)
    
    apiKey = 'da328055e2e940d8b28055e2e9e0d851'
    location = str(sys.argv[1])
    search = json.loads(extract_source('https://api.weather.com/v3/location/search?query=' + location + '&locationType=city&language=en-US&format=json&apiKey=' + apiKey))
    try:
        search = search['location']
    except:
        sys.stderr.write(location + ' not found\n')
        sys.exit(-1)

    index = findIndexCountry(search, str(sys.argv[2]))
    if(index == -1):
        sys.stderr.write('Country not found')
        sys.exit(-1)
        
    print('Getting weather data from ' + str(search['address'][index]))
    url = 'https://api.weather.com/v3/wx/observations/current?geocode=' + str(search['latitude'][index]) + '%2C' + str(search['longitude'][index]) + '&units=m&language=en-US&format=json&apiKey=' + apiKey
    while True:
        data = json.loads(extract_source(url))
        data = {
            'Source': 'TheWeatherChannel',
            'LocalizedName': search['city'][index], 
            'AdministrativeArea': search['adminDistrict'][index],
            'Country': search['country'][index],
            'CurrentUTC': utc_now(),
            'Weather' : data
        }

        send_to_logstash('10.0.100.8', 5001, data)
        
        print('\n#######################\n')
        time.sleep(60)

if __name__ == "__main__":
    main()
