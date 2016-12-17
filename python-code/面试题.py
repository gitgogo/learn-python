#coding=utf-8
#字符串逆序输出
s='hello'
s[::-1] #切片

lis=list(s) #转为list
lis.reverse()
''.join(lis)