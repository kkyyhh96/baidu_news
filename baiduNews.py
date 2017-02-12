# coding:utf-8
# version:python3.5.1
# author:kyh
import queue
import re

import requests

words = ["东城区", "西城区", "朝阳区", "丰台区", "石景山区", "海淀区", "门头沟区", "房山区", "通州区", "顺义区", "昌平区", "大兴区", "怀柔区", "平谷区", "密云区",
         "延庆区"]


# 百度新闻类,包括url,时间,题目,需要查询的字符串
class baiduNews(object):
    def __init__(self, main_word, url, date):
        self.words = words
        self.main_word = main_word
        self.url = url
        self.date = date

    # 匹配字符串
    def string_matching(self, file):
        try:
            request = requests.get(url=self.url, timeout=10)
            # 如果编码是gb18030
            self.main_word = "东城区"
            request.encoding = 'gb18030'
            word = re.findall(r'{0}'.format(self.main_word).encode('utf-8'), request.text.encode('utf-8'))
            if word.__len__() == 0:
                # 如果编码是utf-8
                request.encoding = 'utf-8'
                word = re.findall(r'{0}'.format(self.main_word).encode('utf-8'), request.text.encode('utf-8'))

            # 如果长度大于0则解析成功,可以进行其他字符串的匹配
            if word.__len__() > 0:
                for matching_word in words:
                    result = re.findall(r'{0}'.format(matching_word).encode('utf-8'), request.text.encode('utf-8'))
                    if result.__len__() > 0:
                        file.writelines("1,")
                    else:
                        file.writelines("0,")
            else:
                self.queue_word = queue.Empty

        except Exception as e:
            print(e)

    # 输入每一条网页的所有信息
    def write_info(self, file):
        try:
            file.writelines("\n{0},{1},".format(str(self.url), str(self.date)))

            self.string_matching(file)
        except Exception as e:
            print(e)
