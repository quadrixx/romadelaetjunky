import requests
import json
from bs4 import BeautifulSoup as bs

url = 'https://tenor.com/ru/view/yes-zyzz-zyzz-yes-bodybuilder-gif-23904689'
r = requests.get(url)
soup = bs(r.text, "html.parser")
print(soup.select('[itemprop="contentUrl"]')[0]['content'])