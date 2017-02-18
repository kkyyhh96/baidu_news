# coding:utf-8
# version:python3.5.1
# author:kyh
import re

import requests
from bs4 import BeautifulSoup

url = "http://news.xinhuanet.com/local/2015-11/12/c_128420821.htm"
url = "http://www.takefoto.cn/viewnews-588204.html"
# http://news.sohu.com/20061204/n246775300.shtml"
# request=requests.get(url="http://tech.qianlong.com/2015/1120/107256_4.shtml")
request = requests.get(url=url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.text, 'html.parser', from_encoding='gb18030')
print(soup.prettify())

a = re.findall(r'东城区'.encode('utf-8'), request.text.encode('utf-8'))
print(len(a))
