#coding=utf-8
import time
# 15、将单词表中由相同字母组成的单词归成一类，每类单词按照单词的 首字母排序，并按每类中第一个单词字典序由大到小排列输出各个类别。
# 输入格式:按字典序由小到大输入若干个单词，每个单词占一行，以end 结束输入。
# cinema
# iceman
# maps spam aboard abroad end
# 输出格式:一类单词一行，类别间单词以空格隔开。 aboard abroad
# cinema iceman
# maps spam
content=[]
while True:
	words=raw_input('input words-->')
	content.extend(words.strip().split())
	if words.endswith('end'):
		break
content.remove('end')
content.sort()

for index,word in enumerate(content,1):
	result=[word]
	for mac in content[index:]:
		if sorted(word)==sorted(mac):
			result.append(mac)
			content.remove(mac)
	print ' '.join(result)