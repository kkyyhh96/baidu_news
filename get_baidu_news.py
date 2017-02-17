# coding:utf-8
# version:python3.5.1
# author:kyh

import requests
import time
from bs4 import BeautifulSoup
import datetime
from baiduNews import baiduNews


# 传入关键词,获取一页所有的新闻内容(20条)
def search_words(url, words, count,begin_time=0,end_time=0):
    params = {
        "word": str(words),
        "pn": str(count),
        "cl": "2",
        "ct": "1",
        "tn": "newsdy",
        "rn": "20",
        "ie": "utf-8",
        "bt": str(begin_time),
        "et": str(end_time)
    }
    request = requests.get(url=url, params=params, timeout=5)
    print(request.url)
    #print(request.text)
    return request.text


# 提取出本页的新闻,如果结束返回True,如果所有新闻查询完毕,返回False
def translate_url(html, words):
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    while count < 20:
        if create_news(soup, words, count):
            count += 1
        else:
            return False
    return True


# 提取新闻日期和url,如果提取成功返回True,否则返回False
def create_news(soup, words, count):
    try:
        # 新闻的日期
        news_date = soup.find_all("div", class_="result")[count].find('p', class_="c-author").string
    except Exception as e:
        return False
    try:
        year = str(news_date).split('年')[0][-4:]
        month = str(news_date).split('年')[1].split('月')[0]
        day = str(news_date).split('月')[1].split('日')[0]
        news_date = "{0}-{1}-{2}".format(year, month, day)
        # 新闻的url
        news_url = soup.find_all('div', {'class': 'result'})[count].find('a')['href']
        baidu_news = baiduNews(words, news_url, news_date)
        baidu_news.write_info(file)
        return True
    except Exception as e:
        return True


url = "http://news.baidu.com/ns"
#传入关键词
words = '(东城区 | 西城区 | 朝阳区 | 丰台区 | 石景山区 | 海淀区)'
start_date=datetime.date(2014,1,1)
end_date=datetime.date(2017,1,31)
temp_time=start_date
while temp_time<=end_date:
    print(temp_time)
    begin_time=temp_time
    temp_time+=datetime.timedelta(days=1)
    end_time=temp_time

    begin_time=str(time.mktime(begin_time.timetuple())).split('.')[0]
    end_time=str(time.mktime(end_time.timetuple())).split('.')[0]

    #打开文件
    file=open("1.txt".format(words),'a')
    count = 0
    html = search_words(url, words, count,begin_time,end_time)
    while translate_url(html, words):
        count += 20
        print(count)
        #防止百度封ip,设置为1s
        time.sleep(1)
        html = search_words(url, words, count,begin_time,end_time)
    file.close()
