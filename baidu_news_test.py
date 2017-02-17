# coding:utf-8
# version:python3.5.1
# author:kyh

import requests
import datetime
import time
from bs4 import BeautifulSoup
import re

#计算时间
def compute_date(y0,m0,d0,y1,m1,d1):
    start_time=datetime.date(y0,m0,d0)
    end_time=datetime.date(y1,m1,d1)
    temp_time=start_time
    while temp_time<=end_time:
        temp_time+=datetime.timedelta(days=1)



url_test="http://www.beijing.gov.cn/zfzx/qxrd/hdq/t1257589.htm"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
request = requests.get(url=url_test,headers=headers, timeout=3)
request.encoding='gb18030'
print(request.text)
word = re.findall(r'{0}'.format("海淀").encode('utf-8'), request.text.encode('utf-8'))
print(word)
