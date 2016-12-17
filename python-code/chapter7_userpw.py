#coding=utf-8
db={}
logtime={}
import time
def newuser():
	while True:
		username=raw_input('Enter your name: ')
		if username in db.keys():
			print 'Name has used ,try again'
			continue
		elif not username.isalnum():
			print 'Invalid username,try again'
		else: 
			break
	pwd=raw_input('passwd: ')
	db[username]=pwd
	logtime[username]=time.strftime('%Y-%m-%d %H:%M:%S')

def olduser():
	for i in range(1,5):
		username=raw_input('Enter your name: ')
		if username not in db.keys():
			print 'Registerr first'
			newuser()
			break
		elif username in logtime.keys():
			#时间转换，字符串转为时间戳做比较
			timetuple=time.strptime(logtime[username],'%Y-%m-%d %H:%M:%S')
			timeu=time.mktime(timetuple)
			#如果登陆时长在10s内，则无需输入密码，直接登陆
			if time.time()-timeu<10:
				print 'You already logged in at: ',logtime[username]
				break
			else:
				pwd=raw_input('Enter your passwd: ')
				if pwd==db[username]:
					print 'Welcom back', username,'your last login is %s'%logtime[username]
					#更新登陆日期
					logtime[username]=time.strftime('%Y-%m-%d %H:%M:%S')
					break
				else:
					print 'username or passwd incorrect, try again\n\
					 and you have %d chance'%(5-i)

def manager():
	prop='''
	(D)elete user
	(S)how users
	(B)ack
	Enter your choice
	'''
	back=False
	while not back:
		choice=raw_input(prop).strip().lower()
		if choice not in 'bds':
			print 'Invalid choice,try again'
		else:
			if choice=='d':
				userd=raw_input('Who you want to delete: ')
				del db[userd]
				print 'Okay, %s have deleted'%userd
			if choice=='s':
				for user in db.keys():
					print '%s--%s'%(user,db[user])
			if choice=='b':back=True

def showmenu():
	prompt= '''
	(N)ew User Login
	(E)xisting User Login
	(Q)uit
	(M)anager
	Enter choice: '''
	done=False
	while not done:
		chosen=False
		while not chosen:
			try:
				choice=raw_input(prompt).strip().lower()
			except (EOFError,KeyboardInterrupt):
				choice=='q'
			if choice not in 'mneq':
				print 'Invalid ,try again'
			else:
				chosen=True
		if choice=='n': newuser()
		if choice=='e': olduser()
		if choice=='m': manager()
		if choice=='q': done=True

if __name__ == '__main__':
	showmenu()
