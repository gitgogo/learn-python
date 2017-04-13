#coding=utf-8
# ['dom', 'parsers', 'sax', 'etree']
import urllib
from xml.parsers.expat import ParserCreate
import re
# 解析天气预报,百度天气
xml = ''
url='http://api.map.baidu.com/telematics/v2/weather?location=%E5%8C%97%E4%BA%AC&ak=B8aced94da0b345579f481a1294c9094'
try:
    page = urllib.urlopen(url)
    xml = page.read()
finally:
    page.close()
# print xml
class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self._weather = dict()
        self._count = 0
        self._current_element = ''
    def start_element(self, name, attrs):
        if name == 'result':
            self._count += 1
            self._weather[self._count] = dict()
        self._current_element = name
    def end_element(self, name):
        pass
    def char_data(self, text):
        # 排除换行符和空白内容
        re_str = '^[\n|\s]+$'
        if self._current_element and not re.match(re_str, text) and self._weather:
            self._weather[self._count][self._current_element] = text
    def show_weather(self):
        for v in self._weather.values():
            print v['date'], '\t'*(7-len(v['date'])), v['temperature'], v['weather'], v['wind']
handler = BaiduWeatherSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
handler.show_weather()