#coding=utf-8
''' 1.对应ascii编码表，自定义输出形式；
	2.对输入的字符串加密输出'''
# s=''
# for i in range(256):
# 	if 97<=i<=122 or 65<=i<=90 or 48<=i<=57:
# 		s=s+chr(i)
# print s
# 将输入的字符加密输出
# s=raw_input('input a str: ')
# print 'before string: ',s
# s2=''
# for i in s:
# 	if ord(i)<118:
# 		s2+=chr(ord(i)+5)
# 	elif ord(i)>117:
# 		s2+=chr(ord(i)-21)
# print 'after string: ',s2
#十进制转二进制
# def decimal_to_binary(n):
# n=input('input a number: ')
# s=''
# while n:
# 	s+=str(n%2)
# 	n=n/2
# print s[::-1]
# print decimal_to_binary(25)
#转换编码方式写文件,读asni文件，写入utf-8文件
# f1=open('aa.txt','r')
# info=f1.read()
# tmp=info.decode('gb2312').encode('utf-8')
# f2=open('a1.txt','w')
# f2.write(tmp)
# f1.close()
# f2.close()

# fp1 = open('aa.txt', 'r') #文件是ansi保存（gbk）
# info1 = fp1.read()
# print type(info1)
# print info1  #默认使用gbk编码进行转换，转换unicode进行打印
# # 已知是 GBK 编码，解码成 Unicode
# tmp = info1.decode('GBK')
# print isinstance(tmp, unicode) 
# print isinstance(info1, unicode)

# import sys
# print sys.getdefaultencoding()
# reload(sys)
# sys.setdefaultencoding('utf-8')#改变系统默认编码方式为utf-8
# print type(u'我'.decode('utf-8'))

# import chardet
# import urllib
# data=urllib.urlopen('http://www.baidu.com').read()
# print chardet.detect(data)

# number=int(raw_input("input  a number:"))
# def decimal_to_binary(number):
# 	bin_list=[]
# 	while 1:
# 	    quient=number/2   #每次循环除2
# 	    bin_list.append(str(number%2))  #将余数添加到list中
# 	    number=quient  #将商赋值给number用于下次循环继续做除数
# 	    if number==0:  #如果number=0说明都除尽了，可以退出循环
# 	        break
# 	return "result:","".join(bin_list[-1::-1])  #翻转list，并用join函数拼接list中的元素输出结果
# print decimal_to_binary(25)

# 向文件写number个数，从1-number从文件读出来，把所有的数求和
# 返回累加的结果
def sum(number):
	f=open('a1.txt','w')
	for i in range(1,number+1):
		f.write(str(i)+'\n')
	f.close()
	f=open('a1.txt','r')
	result=0
	for j in f:
		result+=int(j)
	f.close()
	return result
print sum(6)