__author__ = 'mkleinert'

from bs4 import BeautifulSoup

import requests
import time
import pymongo


url = "api.wunderground.com/api/0f58c05cd95da63a/forecast/q/46231.xml"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

tag_high = soup.high
tag_high
high_temp = tag_high.contents[1]

print(high_temp.contents)

tag_low = soup.low
tag_low
low_temp = tag_low.contents[1]

print(low_temp.contents)
print (time.strftime("%d/%m/%Y"))

wunderground_forecast = {'site_url':url,'site_high_temp':high_temp.contents,'site_low_temp':low_temp.contents, 'forecast_date':time.strftime("%d/%m/%Y")}

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mydb.weather_temp

db.insert(wunderground_forecast)

results = db.find()

print()

client.close()

