#coding=utf-8
#1.切割字符串函数
def split(str,split_str=' '):
	lis=[]
	while split_str in str:
		index=str.index(split_str)
		lis.append(str[:index])
		str=str[index+len(split_str):]
	lis.append(str)
	return lis
print split('abbcbbdbbe','bb')
#方法2
def split_string(str,split_str=" "):
    tmp=""   #存储切割后的字符串
    length=len(split_str)  #计算一下被切割字符串的长度
    result=[]     #存储切割后的结果
    i=0   #循环每一个字符需要用到的初始化变量i
    while i<=len(str)-1:   #遍历str中的每一个字符
        if str[i:i+length]==split_str:  #当前字符位置+length-1个的字符串是否等于切割字符串
            result.append(tmp)   #触发了if条件，说明遍历到了切割字符串的位置，把之前的字符串写入到result中
            tmp=""  #清空，用于下次累加               
            i+=length   #跳过length个长度，以此实现跳过分割的字符串，来继续遍历
        else:
            tmp+=str[i]  #触发else条件，说明不是切割点，需要存到tmp中
            i+=1   #加一后跳到下一个字符继续遍历
    result.append(tmp) #把最后的tmp添加到result中
    return result
#2.判断是否字符串
def is_string(s):
    # if isinstance(s,(str,unicode)):
    #     return True
    try:
        s+""
        return True
    except Exception,e:
        return False

class newstring():
    def __init__(self, value):
        self.value=value
    def __str__(self):
        return self.value
    def __add__(self,other):
        return str(self.value)+str(other)

print is_string(newstring("abc"))
print newstring("abc")+"a"
#递归字符串转列表
lis=[]
def strr(s):
	if len(s)==1:
		lis.append(s[:])
	else:
		lis.append(s[0])
		strr(s[1:])
strr('gloryroad')
print lis

#大小写转换
# map(lambda x:chr(ord(x)+32) if x in string.uppercase else chr(ord(x)-32) , 'uiJKgH')
#奇数位大小写转换
def swap_even_index_letter(str):
    str="gloryroad"
    str=list(str)
    for i in range(0,len(str),2):
        if ord(str[i])>97 and ord(str[i])<122:
            str[i]=chr(ord(str[i])-32)
        elif ord(str[i])>65 and ord(str[i])<90:
            str[i]=chr(ord(str[i])+32)
    return "".join(str)
#base64编码
str = "this is string example....wow!!!";
str = str.encode('base64','strict');
print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
#依次找出字符串中的字符，返回索引的列表
def find_str(s,find_string):
	lis=[]
	i=0
	while i!=-1:
		lis.append(s.find(find_string,i))
		i=s.find(find_string,i)
		i=i+len(find_string)
	return lis
print find_str('hellohello','ll')
#循环输出字符，超出的长度折行打印
s='abcdefghijklmn'
s1=s[:]
i=1
while i<9:
    if len(s1)<i:
        s1=s1+s
    print s1[:i]
    s1=s1[i:]
    i+=1
