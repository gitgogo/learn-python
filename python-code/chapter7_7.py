#coding=utf-8
#颠倒输入的字典
raw_dict={}
ch_dict={}
key=raw_input('input the key of dict: ')
value=raw_input('input the value: ')
raw_dict[key]=value
ch_dict[value]=key
print 'the raw dict is %s\nthe changed dict is %s'%(str(raw_dict),str(ch_dict))

# dict1=dict(raw_input('input a dict: '))
# print {dict1.values()[0]:dict1.keys()[0]}