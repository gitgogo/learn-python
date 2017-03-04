#coding=utf-8
import re
def match(s1,s2):
	content=re.search(s1,s2)
	if content:
		print content.group()
	else:
		print 'have no %s'%s1

match('python','hellopython')
match('python1','hellopython')

func=lambda s1,s2:s1 if re.search(s1,s2) else 'not found'
print func('python1','hellopython')

import re
def match(s):
	pattern=re.compile(r'\D\d{5}\D|^\d{5}\D|\D\d{5}$|^\d{5}$')
	result=pattern.search(s)
	# result=re.search(r'\D\d{5}\D|^\d{5}\D|\D\d{5}$|^\d{5}$'," 12345")
	if result:
	    word_list=[]
	    for s in result.group():
	        if s in "0123456789": 
	            word_list.append(s)
	    print "".join(word_list)

	else:
	    print "not found!"

match('12345')
match('w12345w')
match('12345w')
match('w12345')
match('123s5')
match('1234')
match('123456')
match('qwert')

def test_regular(destine_string):
    result=re.search(r'\D\d{5}\D|^\d{5}\D|\D\d{5}$|^\d{5}$',destine_string)
    if result:
        word_list=[]
        for s in result.group():
            if s in "0123456789": 
                word_list.append(s)
        print "".join(word_list)
        return "".join(word_list)

    else:
        print "not found!"
        return None

if __name__=="__main__":
	test_data=[]
	with open('f:\\1.txt') as f:
		for line in f:
			test_data.append(line.strip())
    # test_data=["12345"," 12345","ted12345"]
	test_data_fault=['1234','123r45','123456']
	for data in test_data:
		assert test_regular(data)=="12345"
	for data in test_data_fault:
		try:
			assert test_regular(data)=="12345"
		except Exception as e:
			print e
        
	print "test completed!"

# re.sub应用
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
#\2, \1表示分组引用，分别代表第二个分组，第一个分组
print p.sub(r'\2 \1', s)

#当repl为方法时，将匹配的结果m传入方法
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)
print p.findall(s)