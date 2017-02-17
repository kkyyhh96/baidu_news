# coding:utf-8
# version:python3.5.1
# author:kyh

import requests
import datetime
import time
from bs4 import BeautifulSoup

class baidu_news(object):
    def __init__(self):
        self.url="http://news.baidu.com/ns"

    #搜索关键词
    def search_news(self,words,count,begin_time=0,end_time=0):
        params={
           "word":str(words),
            "pn":str(count),
            "cl": "2",
            "ct": "1",
            "tn": "news",
            "rn": "20",
            "ie": "utf-8",
            "bt": str(begin_time),
            "et": str(end_time)
        }
        #发送搜索请求,如果超过3s则重新发送
        request = requests.get(url=self.url, params=params, timeout=3)
        return request.text


