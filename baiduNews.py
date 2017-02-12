# coding:utf-8
# version:python3.5.1
# author:kyh
import requests
from bs4 import BeautifulSoup

words=["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","门头沟区","房山区","通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","密云区","延庆区"]
#百度新闻类,包括url,时间,题目,需要查询的字符串
class baiduNews(object):
    def __init__(self,main_word,url,date):
        self.words=words
        self.main_word=main_word
        self.url=url
        self.date=date

    def write_info(self):
        file=open("{0}.txt".format(self.main_word),'a')
        file.writelines("{0},{1}\n".format(self.url,self.date))
        file.close()
