#coding=utf-8
#find chr from string
def rfindchr(string,chr):
	# string=string[::-1]
	if chr in string:
		# for i in range(len(string)):
		i=len(string)-1
		while i>=0:
			if chr == string[i]:
				# return len(string)-i-1
				return i
			i=i-1
	else:
		print 'not match'
		
print rfindchr('huiij','u')

