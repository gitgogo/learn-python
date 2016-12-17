#coding=utf-8
#find chr from string
def findchr(string,chr):
	if chr in string:
		for i in range(len(string)):
			if chr == string[i]:
				return i
	else:
		print 'not match'
		
print findchr('huiij','i')

