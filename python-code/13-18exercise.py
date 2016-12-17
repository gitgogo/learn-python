#coding=utf-8
#13-3.将输入的浮点型数值转换为美元格式输出

def dollarize(num):
	num1=str(round(num,2))
	num_str=num1[:-3]
	l=[]
	l.append(num_str[-3:])
	if len(num_str)>3:
		i=4
		while i<len(num_str)+1:
			l.append(num_str[-i-2:-i+1])
			i+=3
	return '$'+','.join(l[::-1])+num1[-3:]

print dollarize(14.7892)


def split_right_n(s,n):
	l=[]
	l.append(s[-n:])
	i=n+1
	while i<len(s)+1:
		l.append(s[-i-n+1:-i+1])
		i+=n
	return l[::-1]

print split_right_n('jijfosgwoosjnbmcsakjkl12341212',5)