#coding=utf-8
shelf=[]
option='''
a for append a book
b for remove a book
c for lookup books
q for quit
count for how many books in shelf

Enter your choice
'''
while True:
	choice=raw_input(option).strip().lower()
	if choice=='a':
		book=raw_input('what book?')
		shelf.append(book)
	elif choice=='b':
		lend=raw_input('what book do you want to lend? ')
		if lend not in shelf:
			print 'no book'
		shelf.remove(lend)
	elif choice=='c':
		for i in shelf:
			print i,
	elif choice=='count':
		print 'now the shelf have %d books'%len(shelf)
	elif choice=='q':
		break
	else :print 'invalid option,try again'
