#coding=utf-8
# 1、实现任意自定义类
class Festival(object):
	def __init__(self,name,food,action):
		self.name=name
		self.food=food
		self.action=action

	def hay(self):
		print 'Happy',self.name

Spring=Festival('Spring Festival','dumpling','fireworks')
Spring.hay()

# 2 、实现@property 方法
class Student(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	@property
	def get_name(self):
		return self.name

XiaoMing=Student('xm',22)
print XiaoMing.get_name

# 3、实现单继承类
class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def get_name(self):
		return self.name

class Singer(Person):
	def __init__(self,name,age,gender):
		Person.__init__(self,name,age)
		self.gender=gender

	def sing(self):
		print 'sing my song...'

Maroon=Singer('maroon5',43,'M')
print Maroon.get_name()
print Maroon.gender
Maroon.sing()

# 4、实现多继承类 
class Worker(object):
	def __init__(self,name,payment):
		self.name=name
		self.payment=payment

	def work(self):
		return [x for x in range(5)]

class POP(Singer,Worker):
	def __init__(self,name,age,gender,payment):
		Worker.__init__(self,name,payment)
		Singer.__init__(self,name,age,gender)
		# self.age=age

Jim=POP('jim',23,'M',450.56)
print Jim.work()
Jim.sing()
print Jim.gender
print Jim.get_name()

# 5、实现同时具备类方法、静态方法和实例子方法的一个类 
class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def get_name(self):
		return self.name

	@classmethod
	def get_cls_name(cls):
		return cls.__name__

	@staticmethod
	def static_method():
		print 'staticmethod is called...'

Lucy=Person('lucy',21)
print Lucy.get_name()
print Lucy.get_cls_name()
Person.static_method()

# 6、删除无重复元组中给定的元素，返回新元组 
def get_tuple(tup,element):
	tup=set(tup)
	try:
		tup.remove(element)
		return tuple(tup)
	except KeyError,e:
		print e
		return -1
print get_tuple((2,3,4,'f'),'j')

# 8、实现栈类
# 9、实现队列类 
# 10、实现任意2种自定义的不同类型适配器

# 1、类和对象的概念和关系是什么? 
# 2、什么样的代码才是面向对象? 
# 3、类的构造方法与成员方法之间有什么区别? 
# 4、self关键词的作用是什么? 
# 5、类的构造方法和成员方法之间的区别? 
# 6、说出类方法和静态方法的区别?分别实现一个类方法和静态方法 实例
# 7、什么是数据封装与隐藏? 
# 8、什么是方法重写，方法重写的规则是什么?

# 9、编写程序片段，定义表示课程的类Course。课程的属性包括课程名、编号、选修课号;
# 方法包括设置课程名、设置编号、设置选修课 号以及获取课程名、获取编号、获取选修课程号，
# 然后打印输出该对 象的课程名、编号以及选修课号。
class Course(object):
	def __init__(self,name,no,sub_no):
		self.name=name
		self.no=no
		self.sub_no=sub_no

	def set_name(self,name):
		self.name=name

	def set_no(self,no):
		self.no=no

	def set_subno(self,sub_no):
		self.sub_no=sub_no

	def get_name(self):
		return self.name

	def get_no(self):
		return self.no

	def get_subno(self):
		return self.sub_no

math=Course('Math',12234,23455)
print math.get_name()
print math.get_no()
print math.get_subno()
math.set_name('Chinese')
print math.get_name()

# 10、实现一个多重继承类，并访问该类

# 14、按如下规律打印列表 
# 1 [1*, 2, 3, 4, 5]
# 2 [1, 2*, 3, 4, 5]
# 3 [1, 2, 3*, 4, 5]
# 4 [2, 3, 4*, 5, 6] 
# 5 [3, 4, 5*, 6, 7] 
# 6 [4, 5, 6*, 7, 8] 
# ...
# 20 [16, 17, 18, 19, 20*]
k=g=1
for i in range(1,8):
	if i%2:
		for j in range(3):
			print g,[x for x in range(1,k*5+1)][-5:]
			g+=1
		k+=1
	else:
		for h in range(1,4):
			print g,[x for x in range(1,i/2*5+1+h)][-5:]
			g+=1

# 15、写一个函数, 将驼峰命名法字符串转成下划线命名字符串，如GetItem -
# > get_item，getItem -> get_item。
def changeName(name):
	name=list(name)
	name[0]=name[0].lower()
	for i,s in enumerate(name[1:],1):
		if s.isupper():
			name[i]='_'+s.lower()
	return ''.join(name)

print changeName('GetNameOne')

# 16、给定一些NxN的矩阵，对于任意的路线，定义其【和】为其线路上所有 节点的数字的和，
# 计算从左上角到右下角的路线和最小值。每条路线只能从 某一点到其周围(上下左右)的点，不可斜行。
# 例如:
# 4,6
# 2,8 的路线和最小值为 4-2-8 14
# 1,2,3
# 4,5,6
# 7,8,9 的路线和最小值为 1-2-3-6-9 21

# 17、有两个序列a,b，大小都为n,序列元素的值任意整形数，无序;
# 要求: 通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最 小。



def my_split(strr,s):
	result=[]
	while s in strr:
		index=strr.find(s)
		result.append(strr[:index])
		strr=strr[index+len(s):]
	result.append(strr)
	return result

print my_split('21aab21cc21rf21gt','21')

def my_find(strr,s):
	if s in strr:
		for i in range(len(strr)):
			if strr[i:i+len(s)]==s:
				return i
		return -1
	else:return -1

print my_find('helloworldyell','ll')
