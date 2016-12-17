#coding: utf-8
import re
from pprint import pprint

with open('stations.html','r') as f:
	text=f.read()
	# print text
	stations=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',text)
	# print stations
	pprint(dict(stations),indent=4)
	