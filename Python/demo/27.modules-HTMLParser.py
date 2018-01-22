# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from urllib import request

class MyHTMLParser(HTMLParser):

    # 函数名是固定的
    def handle_starttag(self, tag, attrs):
        print('starttag: <%s> attrs: %s' % (tag, attrs))

    def handle_endtag(self, tag):
        print('endtag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag: <%s/>' % tag)

    def handle_data(self, data):
        print('data: %s' % data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('entityref: &%s;' % name)

    def handle_charref(self, name):
        print('charref: &#%s;' % name)

parser = MyHTMLParser()

# URL = 'http://www.baidu.com'
# with request.urlopen(URL, timeout=4) as f:
# 	data = f.read().decode('utf-8') # read得到的是bytes类型，解析需要str类型
# parser.feed(data)

parser.feed('''<html>
<head></head>
<body class="ABC">
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')