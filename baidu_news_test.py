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


words0 ='(东城区 | 西城区 | 朝阳区 | 丰台区 | 石景山区 | 海淀区)'
words1='(门头沟区 | 房山区 | 通州区 | 顺义区 | 昌平区 | 大兴区)'
words2='(怀柔区 | 平谷区 | 密云区 | 延庆区)'
compute_date(2017,1,6,2017,2,10)

url_test="http://www.beijing.gov.cn/zfzx/qxrd/hdq/t1257589.htm"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
request = requests.get(url=url_test,headers=headers, timeout=3)
request.encoding='gb18030'
print(request.text)
word = re.findall(r'{0}'.format("海淀").encode('utf-8'), request.text.encode('utf-8'))
print(word)
