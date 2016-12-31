#coding=utf-8
import sys,os
def create_file():
	file_name=os.path.split(sys.argv[1])
	os.makedirs(file_name[0])
	os.chdir(file_name[0])
	with open(file_name[1],'w') as f:
		pass

def remove_file():
	file_name=os.path.split(sys.argv[1])
	os.remove(os.path.join(sys.argv[1]))
	os.removedirs(file_name[0])

create_file()