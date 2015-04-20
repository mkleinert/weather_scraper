__author__ = 'mkleinert'

from bs4 import BeautifulSoup

import requests

url = "api.wunderground.com/api/0f58c05cd95da63a/conditions/q/46231.json"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

print(soup)