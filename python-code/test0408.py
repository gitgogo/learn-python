# coding=utf-8
# import unittest

# class Calc(object):

#     def add(self, x, y, *d):
#         # 加法计算
#         result = x + y
#         for i in d:
#             result += i
#         return result

#     def sub(self, x, y, *d):
#         # 减法计算
#         result = x - y
#         for i in d:
#             result -= i
#         return result

#     @classmethod
#     def mul(cls, x, y, *d):
#         # 乘法计算
#         result = x * y
#         for i in d:
#             result *= i
#         return result

#     @staticmethod
#     def div(x, y, *d):
#         # 除法计算
#         if y != 0:
#             result = x / y
#         else:
#             return -1
#         for i in d:
#             if i != 0:
#                 result /= i
#             else:
#                 return -1
#         return result

# import unittest
# class TestFun(unittest.TestCase):
#     def setUp(self):
#         self.obj=Calc()
#         print 'start'

#     def test_add(self):
#         self.assertEqual(self.obj.add(1,2,3),6)

#     def test_sub(self):
#         self.assertEqual(self.obj.sub(1,2,3),-4)

#     def test_mul(self):
#         self.assertEqual(Calc.mul(1,2,3),6)

#     def test_div(self):
#         self.assertEqual(self.obj.div(4,2),6)

#     def tearDown(self):
#         print 'done'

# if __name__ == '__main__':
#     unittest.main()

#encoding=utf-8
import unittest

# 被测试类
class myclass(object):
    @classmethod
    def sum(self, a, b):
        return a + b #将两个传入参数进行相加操作

    @classmethod
    def sub(self, a, b):
        return a - b #将两个传入参数进行相减操作

class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "初始化类固件" #只会被执行一次
        print "----setUpClass"

    @classmethod
    def tearDownClass(cls):
        "重构类固件" #只会被执行一次
        print "----tearDownClass"

    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 1
        print "--setUp"

    # 退出清理工作
    def tearDown(self):
        print "--tearDown"

    # 具体的测试用例，一定要以test开头
    def testsum(self):
        # 断言两数之和的结果是否是4
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        # 断言两数之差的结果是否是2
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')

if __name__ == '__main__':
    unittest.main() # 启动单元测试
		
# if __name__=="__main__":
#     c=Calc()
#     print c.add(1,2,3,4)
#     print c.mul(2,3,4)
#     print c.div(10,5)
#     print Calc.mul(1,2,3,4)
#     print Calc.div(100,10,5,1)	

#encoding=utf-8
# import unittest
# import random
# class TestSequenceFunctions(unittest.TestCase):
#     def setUp(self):
#         # 初始化一个递增序列
#         self.seq = range(10)
#         print "setup completed!"

#     def test_run(self):
#         # 从序列seq中随机选取一个元素
#         element = random.choice(self.seq)
#         # 验证随机元素确实属于列表中
#         self.assertTrue(element in self.seq)
        
#     def test_sth(self):
#         assert 1==1
        
#     def tearDown(self):
#         print "tearDown completed"
        
# class TestDictValueFormatFunctions(unittest.TestCase):
#     def setUp(self):
#         self.seq = range(10)

#     def test_shuffle(self):
#         # 随机打乱原seq的顺序
#         random.shuffle(self.seq)
#         self.seq.sort()
#         self.assertEqual(self.seq, range(10))
#         # 验证执行函数时抛出了TypeError异常
#         self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

# if __name__ == '__main__':
#     unittest.main()

# coding=utf-8
import random
import unittest 
import sys

class TestSequenceFunctions(unittest.TestCase):
    a = 1

    def setUp(self):
        self.seq = list(range(10))

    @unittest.skip("skipping") # 无条件忽略该测试方法
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    # 如果变量a > 5，则忽略该测试方法
    @unittest.skipIf(a > 5, "condition is not satisfied!")
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    # 除非执行测试用例的平台是Linux平台，否则忽略该测试方法
    @unittest.skipUnless(sys.platform.startswith("liux"), "requires Linux")
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity = 2).run(suite)

#encoding=utf-8
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_choice(self):
        # 从序列seq中随机选取一个元素
        element = random.choice(self.seq)
        # 验证随机元素确实属于列表中
        self.assertTrue(element in self.seq)

    def test_sample(self):
        # 验证执行的语句是否抛出了异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_shuffle(self):
        # 随机打乱原seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # 验证执行函数时抛出了TypeError异常
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

if __name__ == '__main__':
    # 根据给定的测试类，获取其中的所有以“test”开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(
    TestSequenceFunctions)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(
    TestDictValueFormatFunctions)
    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite2, suite1])  #通过调整suit2和suite1的顺序，可以设定执行顺序
    # 设置verbosity = 2，可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity = 2).run(suite)

#断言
#encoding=utf-8
import unittest
import random

# 被测试类
class MyClass(object):
    @classmethod
    def sum(self, a, b):
        return a + b

    @classmethod
    def div(self, a, b):
        return a / b

    @classmethod
    def retrun_None(self):
        return None

# 单元测试类
class MyTest(unittest.TestCase):

    # assertEqual()方法实例
    def test_assertEqual(self):
        # 断言两数之和的结果
        try:
            a, b = 1, 2
            sum = 13
            self.assertEqual(a + b, sum, '断言失败，%s + %s != %s' %(a, b, sum))
        except AssertionError, e:
            print e

    # assertNotEqual()方法实例
    def test_assertNotEqual(self):
        # 断言两数之差的结果
        try:
            a, b = 5, 2
            res = 3
            self.assertNotEqual(a - b, res, '断言失败，%s - %s != %s' %(a, b, res))
        except AssertionError, e:
            print e

    # assertTrue()方法实例
    def test_assertTrue(self):
        # 断言表达式的为真
        try:
            self.assertTrue(1 == 1, "表达式为假")
        except AssertionError, e:
            print e

    # assertFalse()方法实例
    def test_assertFalse(self):
        # 断言表达式为假
        try:
            self.assertFalse(3 == 2, "表达式为真")
        except AssertionError, e:
            print e

    # assertIs()方法实例
    def test_assertIs(self):
        # 断言两变量类型属于同一对象
        try:
            a = 12
            b = a
            self.assertIs(a, b, "%s与%s不属于同一对象" %(a, b))
        except AssertionError, e:
            print e

    # test_assertIsNot()方法实例
    def test_assertIsNot(self):
        # 断言两变量类型不属于同一对象
        try:
            a = 12
            b = "test"
            self.assertIsNot(a, b, "%s与%s属于同一对象" %(a, b))
        except AssertionError, e:
            print e

    # assertIsNone()方法实例
    def test_assertIsNone(self):
        # 断言表达式结果为None
        try:
            result = MyClass.retrun_None()
            self.assertIsNone(result, "not is None")
        except AssertionError, e:
            print e

    # assertIsNotNone()方法实例
    def test_assertIsNotNone(self):
        # 断言表达式结果不为None
        try:
            result = MyClass.sum(2, 5)
            self.assertIsNotNone(result, "is None")
        except AssertionError, e:
            print e

    # assertIn()方法实例
    def test_assertIn(self):
        # 断言对象A是否包含在对象B中
        try:
            strA = "this is a test"
            strB = "is"
            self.assertIn(strB, strA, "%s不包含在%s中" %(strB, strA))
        except AssertionError, e:
            print e

    # assertNotIn()方法实例
    def test_assertNotIn(self):
        # 断言对象A不包含在对象B中
        try:
            strA = "this is a test"
            strB = "Selenium"
            self.assertNotIn(strB, strA, "%s包含在%s中" %(strB, strA))
        except AssertionError, e:
            print e

    # assertIsInstance()方法实例
    def test_assertIsInstance(self):
        # 测试对象A的类型是否值指定的类型
        try:
            x = MyClass
            y = object
            self.assertIsInstance(x, y, "%s的类型不是%s" %(x, y))
        except AssertionError, e:
            print e

    # assertNotIsInstance()方法实例
    def test_assertNotIsInstance(self):
        # 测试对象A的类型不是指定的类型
        try:
            a = 123
            b = str
            self.assertNotIsInstance(a, b, "%s的类型是%s" %(a, b))
        except AssertionError, e:
            print e

    # assertRaises()方法实例
    def test_assertRaises(self):
        # 测试抛出的指定的异常类型
        # assertRaises(exception)
        with self.assertRaises(ValueError) as cm:
            random.sample([1,2,3,4,5], "j")
        # 打印详细的异常信息
        print "===", cm.exception

        # assertRaises(exception, callable, *args, **kwds)
        try:
            self.assertRaises(ZeroDivisionError, MyClass.div, 3, 0)
        except ZeroDivisionError, e:
            print e

    # assertRaisesRegexp()方法实例
    def test_assertRaisesRegexp(self):
        # 测试抛出的指定异常类型，并用正则表达式具体验证
        # assertRaisesRegexp(exception, regexp)
        with self.assertRaisesRegexp(ValueError, 'literal') as ar:
            int("xyz")
        # 打印详细的异常信息
        print ar.exception
        # 打印正则表达式
        print "re:",ar.expected_regexp.pattern

        # assertRaisesRegexp(exception, regexp, callable, *args, **kwds)
        try:
            self.assertRaisesRegexp(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
        except AssertionError, e:
            print e


if __name__ == '__main__':
    # 执行单元测试
    unittest.main()