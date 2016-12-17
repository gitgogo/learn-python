#coding=utf-8
#将前半段字母映射到后半段字母（13个）,大小写保持不变，如：a-n ,O-B
def rot13(stri):
	result=''
	for i in stri:
		if i.isalpha():
			if 'a'<=i<='m' or 'A'<=i<='M':
				i=chr(ord(i)+13)
			elif i>'m' or 'M'<i<='Z':
				i=chr(ord(i)-13)
		result=result+i
	return result

stri=raw_input('input a string: ')
print 'The rot13 string is: ',rot13(stri)