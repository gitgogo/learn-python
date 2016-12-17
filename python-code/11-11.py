#coding=utf-8
#读取文件内容，清除每行头尾空白，写入新文件，提供选择创建新文件或覆盖源文件两种选择
with open('a1.txt','r') as f:
	content=map(lambda line:line.strip(),f.readlines())
	choice=raw_input('creat or replace? ').lower()
	if choice=='c':
		with open('a11.txt','w') as file:
			file.writelines(content)
	elif choice=='r':
		with open('a1.txt','w') as f:
			f.writelines(content)