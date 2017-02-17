# coding:utf-8
# version:python3.5.1
# author:kyh

import requests
import datetime
import time
from bs4 import BeautifulSoup
from baidu_news_api import baidu_news

#计算时间
def compute_date(y0,m0,d0,y1,m1,d1):
    start_time=datetime.date(y0,m0,d0)
    end_time=datetime.date(y1,m1,d1)
    temp_time=start_time
    while temp_time<=end_time:
        temp_time+=datetime.timedelta(days=1)


baiduNews=baidu_news()
words0 ='(东城区 | 西城区 | 朝阳区 | 丰台区 | 石景山区 | 海淀区)'
words1='(门头沟区 | 房山区 | 通州区 | 顺义区 | 昌平区 | 大兴区)'
words2='(怀柔区 | 平谷区 | 密云区 | 延庆区)'
compute_date(2017,1,6,2017,2,10)

