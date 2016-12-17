#coding=utf-8
def subchr(string,origchar,newchar):
	for i in range(len(string)):
		if origchar in string:
			string=string[:string.find(origchar)]+newchar+string[(string.find(origchar))+1:]
	print string

subchr('womwen','w','p')