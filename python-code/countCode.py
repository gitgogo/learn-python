#coding=utf-8
'''统计文件目录下所有py文件中的有效代码行数'''
import os

# def get_files(path):
# 	files=[]
# 	abs_path=os.path.abspath(path)
# 	for file in os.listdir(abs_path):
# 		if os.isfile(file):
# 			files.append(file)
# 		else:
# 			abs_path=os.path.join(abs_path,file)
# 			get_files(abs_path)
# 	return files
# count=0
# def countLine(filename):
# 	global count
# 	if not os.path.isdir(filename):
# 		print '%s is not a dir,try agian...'
# 	else:
# 		for file in os.listdir(filename):
# 			if file.endswith('.py'):
# 				with open(os.path.join(filename,file),'r') as f:
# 					for line in f:
# 						if not line.strip().startswith('#') and len(line.strip)!=0:
# 							count+=1
# 			elif os.path.isdir(file):
# 				print 'scr'
# 				curpath=os.path.join(filename,file)
# 				countLine(curpath)
# 	return count

# filename=raw_input('input your filename: ')
# print countLine(u'F:\\我的坚果云\\文档\\python-code')

#使用os.walk()实现统计代码行数
def codeLines(path):
	count_py=0
	while not os.path.isdir(path):
		print path,'is not a valid dir,try again...'
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.endswith('.py'):
				file_path=os.path.join(root,file)
				with open(file_path) as f:
					for line in f:
						if line.strip().startswith('#') or line.strip()=='':
							continue
						else:count_py+=1
	return count_py

print codeLines('/Users/ralphliu/Document/learn-python/python-code/')



