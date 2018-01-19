# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# SAX编程解析XML格式
from xml.parsers.expat import ParserCreate
from urllib import request
import json
import time

# 自定义的解析函数类
# 需要定义三个方法，对应标签头-标签内容-标签尾
# 返回的数据大部分都在标签头的属性里
class SaxHandle(object):
    def __init__(self):
        self.location = {}
        self.forecast = []

    # name 标签名，attrs 属性对象
    def start_element(self, name, attrs):
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.location = attrs
        if name == 'yweather:forecast':
            data = {}
            # 时间格式化：strftime 时间转str / strptime str转时间
            date = time.strftime(
                '%Y-%m-%d', time.strptime(attrs['date'], '%d %b %Y'))
            data['date'] = date
            data['high'] = attrs['high']
            data['low'] = attrs['low']
            self.forecast.append(data)

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

# 解析
def parseXML(xml_str):
    handler = SaxHandle()  # 解析函数类实例
    parser = ParserCreate()  # 创建自定义解析
    parser.StartElementHandler = handler.start_element # 依次赋予相应解析函数
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)  # 解析
    return {
        'city': handler.location['city'],
        'forecast': handler.forecast
    }


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXML(data.decode('utf-8'))
print(result['city'] == 'Beijing')