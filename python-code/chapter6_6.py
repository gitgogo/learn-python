#coding=utf-8
#替代string.strip()
s=raw_input('input your str: ')
for i in range(len(s)):
	if s[i]!=' ':
		s=s[i:]
		break
for j in range(len(s)):
	if s[i]==' ':
		s=s[:i]
		break
print '%s is removed spacecase'%s