#按位与、或
#coding=utf-8
a=1
b=2
print u"a的二进制是：",bin(a)[2:].zfill(len(bin(a))) 
print u"b的二进制是：",bin(b)[2:].zfill(len(bin(b))) 
print u"a和b的位与结果",a&b #结果的二进制表示为：0
print u"a和b的位或结果",a|b #结果的二进制表示为：0011
print u"a和b的按位异或结果",a^b #结果的二进制表示为：0011
#取反操作
#coding=utf-8
a=9
print u"a的二进制是：",bin(a)[2:].zfill(len(bin(a))) 
print u"a按位翻转的与结果",~a 
print u"a按位翻转后的二进制表示为：",bin(~a)
