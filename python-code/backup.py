#coding = utf-8
#备份文件
import os,time

source=['/Users/ralphliu/Documents','/Users/ralphliu/Music']
target_dir='/Users/ralphliu/Documents/backup/'
target=target_dir+time.strftime('%Y%m%d')+'.zip'
zip_command='zip -qr %s %s'%(target,' '.join(source))
if os.system(zip_command)==0:
	print 'successful backup'
else:
	print 'backup failed'