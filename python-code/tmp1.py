#coding=utf-8
# from multiprocessing import Process,Pool,cpu_count,Queue,Value,Array,Lock
# import time,os,random
# from ctypes import c_char_p
# from multiprocessing.managers import BaseManager

# class Counter(object):
#     def __init__(self,ini=0):
#         self.val=Value('i',ini)
#         self.lock=Lock()
#     def increment(self):
#         with self.lock:
#             self.val.value+=1
#     def value(self):
#         return self.val.value
# def long_task(name,counter):
#     time.sleep(0.1)
#     print 'task {0} running...{1}'.format(name,os.getpid())
#     for i in range(50):
#         time.sleep(0.01)
#         counter.increment()
# # counter=Counter(0)
# class MyManager(BaseManager):
#     pass

# def Manager():
#     m=MyManager()
#     m.start()
#     return m
# MyManager.register('Counter',Counter)
# m=Manager()

# counter=m.Counter(0)
# pool=Pool(cpu_count())
# for i in range(cpu_count()):
#     pool.apply_async(long_task,args=[str(i),counter])
#     print '.....'
#     # p.start()
# pool.close()
# pool.join()
# print counter.value()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
  # 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
  command_executor = 'http://192.168.2.108:6666/wd/hub',
  desired_capabilities = {
        # 指定远程计算机执行使用的浏览器为ie
        "browserName": "chrome",
        "video": "True",
        # 远程计算机的平台
        "platform": "WINDOWS"
  })
print ("Video: " + "http://www.baidu.com" + driver.session_id)

try:
    driver.implicitly_wait(30)
    # driver.maximize_window()
    driver.get("http://www.sogou.com")
    assert u"搜狗" in driver.title
    elem = driver.find_element_by_id("query")
    elem.send_keys(u"webdriver实战宝典")
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    assert u"吴晓华" in driver.page_source
    print 'done!'
finally:
    driver.quit()