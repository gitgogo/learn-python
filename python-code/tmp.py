#coding=utf-8
import sys,os
def find_big_files(path):
	big_file={}
	for root,dirs,files in os.walk(path):
		for file in files:
			file_path=os.path.join(root,file)
			big_file[file_path]=os.path.getsize(file_path)
	return sorted(big_file.items(),key=lambda x:x[1])[-3:]
print find_big_files('f:\\test')
