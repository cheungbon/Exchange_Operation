# encoding:UTF-8
import urllib.request as request
import re
from bs4 import BeautifulSoup

url = "https://www.aicoin.com"
rex = re.compile(r'default_market_tabs-pane-.*?')

data = request.urlopen(url)
try:
    data = data.read().decode('UTF-8')
    soup = BeautifulSoup(data)
except:
    pass

res = soup.find(id=rex)
print(res)
