#coding=utf-8
import re
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
#\2, \1表示分组引用，分别代表第二个分组，第一个分组
print p.sub(r'\2 \1', s)

#当repl为方法时，将匹配的结果m传入方法
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)
print p.findall(s)
