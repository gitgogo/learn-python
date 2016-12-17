#coding=utf-8
#将string中的srcstr替换为dststr输出，python核心编程7-9
def tr(srcstr,dststr,string):
	if srcstr not in string:
		print 'invalid src'
	index=string.find(srcstr)
	result=string[:index]+dststr+string[index+len(srcstr):]
	print result

string=raw_input(u'源字符串: ')
srcstr=raw_input(u'你要翻译的字符: ')
dststr=raw_input(u'你想要翻译为: ')
tr(srcstr,dststr,string)