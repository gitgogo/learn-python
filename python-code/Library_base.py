#coding=utf-8
#图书馆功能
def Lib():
	promp='''
	a：增加新书
	r：借书
	i：还书
	s：查看所有书
	q: 退出
	请选择……
	'''
	book_shelf=[]
	flag=True
	while flag:
		choice=raw_input(promp.decode('utf-8').encode('gbk')).strip().lower()
		if choice=='a':
			book_name=raw_input('请输入你要添加的书名：'.decode('utf-8').encode('gbk'))
			book_shelf.append(book_name)
			print u'%s已经添加成功！'%book_name
		elif choice=='r':
			book_name=raw_input('请输入你要添加的书名：'.decode('utf-8').encode('gbk'))
			if book_name in book_shelf:
				book_shelf.remove(book_name)
				print u'%s借出成功！'%book_name
			else:print u'没有这本书！'
		elif choice=='i':
			book_name=raw_input('请输入你要添加的书名：'.decode('utf-8').encode('gbk'))
			book_shelf.insert(0,book_name)
			print u'%s已经归还'%book_name
		elif choice=='s':
			print u'所有的书有：%s'%(' , '.join(book_shelf))
		elif choice=='q':
			flag=False
			print u'再见!'
		else:print u'输入错误，请重试：'
Lib()
######改进版本
import sys
def add():
    global library_books
    bookname=raw_input("please input book name to add:")
    library_books.append(bookname)

def borrow():
    bookname=raw_input("please input book name to borrow:")
    if bookname in library_books and bookname not in borrow_books.keys():
        reader_name=raw_input("please input your name to record borrow info:")
        borrow_books[bookname]=reader_name
    else:
    	print 'the book has borrowed or library has not the book'

def back():
    global borrow_books
    bookname=raw_input("please input book name to lend:")
    while 1:
        if bookname not in borrow_books.keys():
            print "no borrow record info found!please input your book name again!"
        else:
            break
    del borrow_books[bookname]

def check():
    print " all books in library are the followings:"
    global library_books
    for i in library_books:
        print i
def exit():
    sys.exit()

print "'*'*30\nwelcome to gloryroad library*'*30\n"
print """
"add" command to add new book to library
"borrow" command to borrow book from library
"back" command to lend book to libraay
"delete"command to delete book from library
"check" command to get all book names from library
"exit" command to quit the library system
*'*30\n
"""

library_books=[]
borrow_books={}
while 1:
    command=raw_input("please input your command:")
    exec(command+"()")
