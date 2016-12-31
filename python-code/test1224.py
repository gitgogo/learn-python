#coding=utf-8
'''
一个文件有很多英文单词，找到出现次数最多的字母，
讲字母和出现次数加在第一行，其他文件内容加后面，原文保持不变。
'''
def get_most_alphabet(filename):
	with open(filename,'r+') as f:
		content=f.read()
		alpha_dict=dict.fromkeys(content,0)
		for alpha in content:
			if alpha.isalpha():
				alpha_dict[alpha]+=1
		result=sorted(alpha_dict.items(),key=lambda x:x[1])[-1]
		f.seek(0,0)
		f.write(result[0]+':'+str(result[1])+'\n'+content)
		f.seek(0,0)
		print f.read()
get_most_alphabet('f:\\test.txt')
#指定位置写入文件
import os
def write_by_index(filename,index,string):
	with open(filename,'r+') as f:
		if index>os.path.getsize(filename):
			f.seek(0,2)
            f.write(string)
		else:
			f.seek(index-1,0)
			f.write(string)
#统计行数
def count_lines(filename):
	count=0
	with open(filename) as f:
		for line in f:
			if '__' in line:
				continue
			if len(line.strip())!=0:
				count+=1
	return count
print count_lines(ur'f:\笔记.txt')
#新建多级目录
import os
def mkdir(path,dir_name,depth):
	for i in range(depth):
		os.chdir(path)
		os.mkdir(dir_name)
		path=os.path.join(dir_name)
mkdir('f:\\','a',4)
##新建目录
# import os
# def create_multiple_dir(dir_path,depth,dir_name):
#     try:
#         os.chdir(dir_path)
#     except Exception,e:
#         return -1
#     for i in range(depth):
#         os.mkdir(dir_name+str(i))
#         os.chdir(dir_name+str(i))
#         with open(dir_name+str(i)+".txt","w") as fp:
#             fp.write(dir_name+str(i))
#     return 0

# print create_multiple_dir("e:\\test",5,"gloryroad")
#
dirList = os.popen('dir f:\\')
for i in dirList.readlines() :
  print i
 #打印目录下的文件绝对路径
 for root,dirs,files in os.walk('f:test\\'):
	for file in files:
		print os.path.join(root,file)
	print '*'*30
	for dir in dirs:
		print os.path.join(root,dir)
#周二课练习题
import sys,os
print sum(int(x) for x in sys.argv[1:])
#统计目录下的txt文件
def count_txt(path):
	count=0
	for root,dirs,files in os.walk(path):
		for file in files:
			file_path=os.path.join(root,file)
			if os.path.exists(file_path):
				if os.path.splitext(file)[1]=='.txt':
					count+=1
	return count
print count_txt('f:\\test')
#
import os,sys
#第一题：命令行输入4个参数，然后用程序求和，例如： python b.py 10 100 1000 10000
# print sum(int(x) for x in sys.argv[1:])

# 第二题：自己构造一个目录A，下面有2个文件a.txt和b.txt ，新建一个目录B，
# 下面有文件c.txt。请使用程序构造这个目录并且封装在一个函数中
def setupDir(path):
	os.chdir(path)
	os.mkdir('A')
	os.chdir('A')
	with open('a.txt','w') as f:
		pass
	with open('b.txt','w') as f:
		pass
	path_B=os.path.join(path,'B')
	os.mkdir(path_B)
	with open(os.path.join(path_B,'c.txt'),'w') as f:
		pass
setupDir('f:\\')

# 第三题：把刚才的目录中的子目录和所有文件的路径，
# 写入到一个文件d.txt中，文件在同级创建的目录下。
def write_path(path):
	for root,dirs,files in os.walk(path):
		for dir in dirs:
			with open(os.path.join(path,'test.txt'),'a') as f:
				f.write(os.patn.join(root,dir))
		for file in files:
			with open(os.path.join(path,'test.txt'),'a') as f:
				f.write(os.patn.join(root,file))