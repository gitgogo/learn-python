#coding=utf-8
#计算语句中每个字母的个数
s='from random import randrange'
dict_s={}
for i in s:
	if i.isalpha():
		dict_s[i]=s.count(i)
print dict_s
#读写文件
f=open('f:\\1.txt','w')
j=97
for i in range(1,101):
	f.write(str(i)+' '+chr(j)+'\n')
	j+=1
	if j>122:
		j=97
f.close()
#指定读第几行
def readline(filename,num):
	fp=open(filename,'r')
	row=0
	for line in fp:
		row+=1
		if row==num:
			fp.close()
			return line
print readline('f:\\1.txt',100)

def readline(filename,num):
	fp=open(filename,'r')
	lines=fp.readlines()
	for i in range(len(lines)):
		if i==num-1:
			return lines[i]
#chardet
import chardet
try:
	fp=open("f:\\1.txt","r")
	file_content=fp.read()
	print chardet.detect(file_content)
	print file_content.decode("utf-8").encode("gbk")
	# print file_content
except Exception ,e:
	print e
finally:
	fp.close()
#with...as...
class Sample:
	def __enter__(self):
		print "In __enter__()"
		return "Foo"

	def __exit__(self, type,value, trace):
		print "In __exit__()"

def get_sample():
	return Sample()

with get_sample() as sample:
	print "sample:",sample
#文件属性
fp = open( "f:\\1.txt",'w')
print u"文件是否关闭：", fp.closed
print u"文件的访问模式：", fp.mode
print u"文件名称：", fp.name
print u"末尾是否强制加空格：", fp.softspace
fp.close()
#第三方包
import linecache
file_content=linecache.getlines('f:\\1.txt')
print file_content
file_content =linecache.getlines('f:\\1.txt')[0:4]
print file_content
file_content =linecache.getline('f:\\1.txt',2)
print file_content

file_content =linecache.updatecache('f:\\1.txt')
print file_content
#更新缓存
linecache.checkcache('f:\\1.txt')
#清理缓存
linecache.clearcache()
#去除空行
fp = open(r'f:\1.txt')
aList = []
for item in fp:
    if item.strip():
        aList.append(item)
fp.close()
fp = open(r'f:\4.txt','w')
fp.writelines(aList)
fp.close()
