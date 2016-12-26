#coding=utf-8
# 练习题1：同时读写文件
with open('f:\\1.txt','r+') as f:
	f.seek(0,2)
	f.write('\ni wrote a line\n')
	f.writelines(['the second line','i am writing python code'])
	f.seek(0,0)
	print f.read()
# 练习题2：创建一个空文件
with open('f:\\empty.txt','w') as f:
	pass
# 练习题3：读取文件的前两行
with open('f:\\1.txt') as f:
	print f.readlines()[:2]
# 练习题4：读取文件的奇数行
with open('f:\\1.txt') as f:
	for i,j in enumerate(f):
		if i%2:
			print j
# 练习题5：在文件中写入一个列表的内容
content=[1,2,3,'python',2.7]
with open('f:\\1.txt','a') as f:
	f.writelines([str(i) for i in content])
# 练习题6：在文件中的0、2、4位置写入当前的文件位置偏移量
with open('f:\\1.txt','r+') as f:
	f.write(str(0))
	f.seek(1,1)
	f.write(str(2))
	f.seek(4,0)
	f.write(str(4))
# 练习题7：with写法读取文件内容
with open(r'f:\1.txt') as f:
	f.read()
# 练习题8：统计一个文件中单词个数，文件内容：
# glory road ,wu lao shi
# file,haha
# women, man, love
count=0
with open(r'f:\2.txt') as f:
	content=f.readlines()
	for words in content:
		count+=len(words.replace(',',' ').split())
print count
# 练习题9：将一个文件的所有单词倒序写入文件中
with open(r'f:\2.txt','r+') as f:
	content=f.readlines()[::-1]
	for words in content:
		f.write(' '.join(words.split()[::-1])+'\n')
'''
1.基础题：
检验给出的路径是否是一个文件：
检验给出的路径是否是一个目录：
判断是否是绝对路径：
检验给出的路径是否真地存:
'''
import os
os.path.isfile('/python-code/tmp1126.py')
os.path.isdir(path)
os.path.isabs(path)
os.path.exists(path)
# 2.返回一个路径的目录名和文件名
os.path.split('/python-code/tmp1126.py')
# 3.分离文件名与扩展名
os.path.splitext('python-code/tmp1126.py')
# 4.找出某个目录下所有的文件，并在每个文件中写入“gloryroad”
path='/Users/ralphliu/Document/'
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path,file)):
		with open(os.path.join(path,file),'a') as f:
			f.write('gloryroad!')
# 5.如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了！”
path='/Users/ralphliu/Document/'
for file in os.listdir(path):
	if os.path.splitext(file)[1]=='.txt':
		with open(os.path.join(path,file),'a') as f:
			f.write(os.linesep+u'被发现了！'.encode('utf-8'))
# 6. 命题练习:
# 1） 一个目录下只有文件（自己构造），拷贝几个文件（手工完成）
# 2 ）用listdir函数获取所有文件，如果文件的创建时间是今天，那么就在文件里面写上文件的路径、
# 文件名和文件扩展名
# 3） 如果不是今天创建（获取文件的创建时间，并转化为时间格式，判断是否今天），请删除
# 4 ）计算一下这个程序的执行耗时
import os,time
path='/Users/ralphliu/Document/test/'
start_time=time.time()
for file in os.listdir(path):
	file_path=os.path.join(path,file)
	ctime=os.path.getctime(file_path)
	if time.strftime('%m-%d',time.localtime(ctime))==time.strftime('%m-%d'):
		file_name=os.path.splitext(file)
		with open(file_path,'a') as f:
			f.write(os.linesep+file_path+' '+file_name[0]+' '+file_name[1])
	else:
		os.remove(file_path)
total_time=time.time()-start_time
print total_time

# 7.删除某个目录下的全部文件

# 8.统计某个目录下文件数和目录个数

# 9.删除某个目录下的全部文件(仅限一级目录)

# 10.使用程序建立一个多级的目录，在每个目录下，新建一个和目录名字一样的txt文件

# 11. 查找某个目录下是否存在某个文件名

# 12. 用系统命令拷贝文件

# 13.输入源文件所在路径和目标目录路径，然后实现文件拷贝功能

# 14.遍历某个目录下的所有图片，并在图片名称后面增加_xx

# 15、遍历指定目录下的所有文件，找出其中占用空间最大的前3个文件

# 16、过滤py源码中的#注释，另存为文件result.py，并执行result.py，断言是否执行成功

# 17、文件访问，提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.

# 18、从命令行接受1个路径如：c:\a\b\c\1.py, 实现1个函数创建目录a\b\c,创建文件1.py
# ，实现1个函数删除已创建的目录及文件

# 19、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结果，把结果记录
# 存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1代表ping失败

# 20、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和返回码打印到屏幕
'''

21、文件访问
访问一存在多行的文件，实现每隔一秒逐行显示文本内容的程序，每次显示文本文件的 5
行, 暂停并向用户提示“输入任意字符继续”，按回车键后继续执行，直到文件末尾。
显示文件的格式为：
[当前时间] 一行内容，比如：[2016-07-08 22:21:51] 999370this is test
'''