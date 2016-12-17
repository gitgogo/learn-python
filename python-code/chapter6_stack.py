#coding=utf-8
stack=[]
def push():
	stack.append(raw_input('Enter new string: ').strip())

def pop():
	if len(stack)==0:
		print 'Can not pop from an empty stack! '
	else:
		print 'Removed [',stack.pop(),']'

def viewstack():
	print stack

CMDs={'u':push,'o':pop,'v':viewstack}
def show_menu():
	pr= '''
	PUSH:U
	POP:O
	VIEW:V
	QUIT:Q
	Enter choice: 
	'''
	while True:
		while True:
			try:
				choice=raw_input(pr).strip().lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice='q'
			print 'You picked %s'%choice
			if choice not in 'uovq':
				print 'Invalid option,try again '
			else:break
		if choice=='q':
			break
		else:
			CMDs[choice]()

if __name__ == '__main__':
	show_menu()

