import time,os,datetime
os.chdir('/Users/ralphliu/Document/')
now=datetime.date.today()
for i in range(3):
	dir_name=now.replace(year=now.year-1+i)
	os.mkdir(str(dir_name))
	filename=dir_name.strftime('%j')
	filepath=os.path.join(str(dir_name),filename+'.log')
	with open(filepath,'w') as f:
		f.write(dir_name.strftime('%U')+os.linesep+dir_name.strftime('%A'))