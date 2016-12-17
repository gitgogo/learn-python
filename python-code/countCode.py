#coding=utf-8
'''统计文件目录下所有py文件中的有效代码行数'''
import os

def get_files(path):
	files=[]
	abs_path=os.path.abspath(path)
	for file in os.listdir(abs_path):
		if os.isfile(file):
			files.append(file)
		else:
			abs_path=os.path.join(abs_path,file)
			get_files(abs_path)
	return files
count=0
def countLine(filename):
	global count
	if not os.path.isdir(filename):
		print '%s is not a dir,try agian...'
	else:
		for file in os.listdir(filename):
			if file.endswith('.py'):
				with open(os.path.join(filename,file),'r') as f:
					for line in f:
						if not line.strip().startswith('#') and len(line)-1!=0:#为什么要len-1？
							# print line,len(line)
							count+=1
			elif os.path.isdir(file):
				print 'scr'
				curpath=os.path.join(filename,file)
				countLine(curpath)
	return count

# filename=raw_input('input your filename: ')
print countLine(u'F:\\我的坚果云\\文档\\python-code')