# coding:utf-8
# version:python3.5.1
# author:kyh

import requests
from bs4 import BeautifulSoup

from baiduNews import baiduNews


# 传入关键词,获取一页所有的新闻内容(20条)
def search_words(url, words):
    params = {
        "word": str(words),
        "pn": "0",
        "cl": "2",
        "ct": "1",
        "tn": "news",
        "rn": "20",
        "ie": "utf-8",
        "bt": "0",
        "et": "0"
    }
    request = requests.get(url=url, params=params, timeout=15)
    return request.text


# 提取出新闻的日期和url,如果结束返回True
def translate_url(html, words):
    soup = BeautifulSoup(html, 'html.parser')
    count=1
    while count<=20:
        if create_news(soup,words,count):
            count+=1
        else:
            return True
    return True


def create_news(soup, words,count):
    try:
        # 新闻的日期
        news_date = soup.find_all("div", class_="result")[count].find('p', class_="c-author").string
        year = str(news_date).split('年')[0][-4:]
        month = str(news_date).split('年')[1].split('月')[0]
        day = str(news_date).split('月')[1].split('日')[0]
        news_date = "{0}-{1}-{2}".format(year, month, day)
        # 新闻的url
        news_url = soup.find_all('div', {'class': 'result'})[count].find('a')['href']
        baidu_news = baiduNews(words, news_url, news_date)
        return True
    except Exception as e:
        return False


url = "http://news.baidu.com/ns"
words = "西城区 东城区 朝阳区 供暖"
html = search_words(url, words)
translate_url(html, words)
