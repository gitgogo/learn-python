#coding=utf-8
import re

# 1、匹配一行文字中的所有开头的字母内容 
print re.match(r'[a-zA-Z]','oneday this12').group()
print re.match(r'[a-zA-Z]+\b','hello world').group()

# 2、匹配一行文字中的所有开头的数字内容 
print re.search(r'^\d+','1234white').group()

# 3、匹配一行文字中的所有开头的数字内容或数字内容
print re.match(r'\w+','hello123,you i').group()

# 4、 只匹配包含字母和数字的行 
print re.search(r'.*\w.*',' hello ,123').group()

# 5、写一个正则表达式，使其能同时识别下面所有的字符串:'bat', 'bit', 'but', 'hat', 'hit', 'hut‘
print re.search(r'b[aiu]t','but').group()

# 6、匹配所有合法的python标识符 
print re.match(r'[_a-zA-Z]\w+$','_you123').group()

# 7、提取每行中完整的年月日和时间字段 
print re.search(r'[0-9]{4}(1[0-2]|0[1-9])(3[01]|[012][0-9])','time is20170921day').group()

# 8、将每行中的电子邮件地址替换为你自己的电子邮件地址 
print re.sub('\S+@\w+\.com|cn','ldjwyyx@163.com','email:wangli@gloryroad.com')

# 9、匹配\home关键字:’re.match(‘\\\home’,’\home’)

# 1、使用正则提取出字符串中的单词

# 2、使用正则表达式匹配合法的邮件地址:
# 国际域名格式如下: 域名由各国文字的特定字符集、英文字母、数字及“-”(即连字符或减号)任意组 合而成, 
# 但开头及结尾均不能含有“-”，“-”不能连续出现。域名中字母不分大 小写。
# 域名最长可达60个字节(包括后缀.com、.net、.org等)。 

# 3、提取字符串中合法的超链接地址
# 比如:s = '<a href="http://www.gloryroad.cn">光荣之路官网</a>' 要求，
# 给出的正则表达式能兼顾所有链接地址。

# 4、统计文件中单词个数

# 5、写一个函数，其中用正则验证密码的强度

# 6、匹配ip的正则表达式:
# r'^(([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$'


