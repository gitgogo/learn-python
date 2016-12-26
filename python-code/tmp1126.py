#coding=utf-8
import os,time
path='/Users/ralphliu/Document/test/'
start_time=time.time()
for file in os.listdir('/Users/ralphliu/Document/test/'):
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