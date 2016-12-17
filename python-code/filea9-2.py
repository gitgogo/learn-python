#coding=utf-8
#显示文件f的前n行
def acfile(F,N):
	lines=[]
	f=open(F,'r')
	for i in range(N):
		print f.readline(),
	f.close()
F=raw_input('input filename: ')
f=open(F,'r')
# N=input('input line number: ')
# acfile(F,N)

#每次显示文件的25行
n=0
# for line in f:#运行报错ValueError: Mixing iteration and read methods would lose data
# 	n+=1
# 	print f.readline()
# 	if n==15:
# 		n=0
# 		raw_input(u'按任意键继续：')
# 		continue
# f.close()

while True:
	lines=f.readline()
	if not lines: break
	n+=1
	print f.readline()
	if n==15:
		n=0
		if raw_input('input any key continue: ')
		# raw_input(u'按任意键继续：'.decode('utf-8').encode('gbk'))
		continue
f.close()