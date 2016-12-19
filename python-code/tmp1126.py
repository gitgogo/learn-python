#coding=utf-8
# 输入样例:
# Welcome to the Python world Are you ready
# 输出样例:
# elcomeway otay ethay ythonpay orldway arehay ouyay eadyray
def pig_latin(word):
	word=word.lower()
	if word[0] in 'aeiou':
		return word+'hay'
	if word[:2]=='qu':
		return word[2:]+'quay'
	if word[0] not in 'aeiou':
		for i in range(1,len(word)):
			if word[i] in 'aeiouy':
				return word[i:]+word[:i]+'ay'
def to_pig_latin(sentance):
	tmp_list=sentance.split()
	for i in range(len(tmp_list)):
		tmp_list[i]=pig_latin(tmp_list[i])
	return ' '.join(tmp_list)
print to_pig_latin('Welcome to the Python world Are you ready')



