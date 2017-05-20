#coding=utf-8
from multiprocessing import Process 
import os
import time
def sleeper(name, seconds):
    print "Process ID# %s" % (os.getpid())
    print "Parent Process ID# %s" % (os.getppid())
#仅支持在linux上,一个进程会有父进程和自己的ID，windows上就没有父进程id 
    print "%s will sleep for %s seconds" % (name, seconds) 
    time.sleep(seconds)
# if __name__ == "__main__":
child_proc = Process(target = sleeper, args = ('bob', 5))
child_proc.start()
print "in parent process after child process start"
print "parent process about to join child process"
child_proc.join()
print "in parent process after child process join"
print "the parent's parent process: %s" % (os.getppid())

# 测试单进程和多进程执行效率
#coding: utf-8
import multiprocessing 
import time
def m1(x):
    time.sleep(0.01)
    return x * x
if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) 
    i_list = range(1000)
    time1=time.time()
    pool.map(m1, i_list)
    time2=time.time()
    print 'time elapse:',time2-time1 
    time1=time.time()
    map(m1, i_list) 
    time2=time.time()
    print 'time elapse:',time2-time1

#coding=utf-8
import multiprocessing 
import os
def m1(x):
    print "pid:",os.getpid(),x*x
    return x * x
if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) 
    i_list = range(8)
    print pool.map(m1, i_list)

# 异步执行
#coding=utf-8
from multiprocessing import Pool
def f(x): 
    return x * x
if __name__ == '__main__':
    pool = Pool(processes = 4) # start 4 worker processes
    result = pool.apply_async(f, [10]) # evaluate "f(10)" asynchronously # prints "100" unless your computer is *very* slow
    print result.get(timeout = 1)
    print pool.map(f, range(10)) # prints "[0, 1, 4,..., 81]"

# 执行效率
#encoding=utf-8
import time
from multiprocessing import Pool 
def run(fn):
#fn: 函数参数是数据列表的一个元素 time.sleep(1)
    time.sleep(1)
    return fn * fn
if __name__ == "__main__": 
    testFL = [1,2,3,4,5,6]
    print 'Single process execution sequence:' #顺序执行(也就是串行执行，单 进程)
    s = time.time() 
    for fn in testFL:
        run(fn)
    e1 = time.time()
    print u"顺序执行时间:", int(e1 - s)
    print 'concurrent:' #创建多个进程，并行执行
    pool = Pool(5) #创建拥有5个进程数量的进程池 #testFL:要处理的数据列表，run:处理testFL列表中数据的函数
    rl =pool.map(run, testFL) 
    pool.close()#关闭进程池，不再接受新的进程 pool.join()#主进程阻塞等待子进程的退出
    e2 = time.time()
    print u"并行执行时间:", int(e2 - e1)
    print rl

#encoding=utf-8
from multiprocessing import Process, Queue 
import os, time, random
# 写数据进程执行的代码: 
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value 
        q.put(value) 
        time.sleep(random.random())
# 读数据进程执行的代码 
def read(q):
    while not q.empty():
# if not q.empty():
        print 'Get %s from queue.' % q.get(True) 
        time.sleep(1) # 目的是等待写队列完成
if __name__=='__main__':
# 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target = write, args = (q,)) 
    pr = Process(target = read, args = (q,)) # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()


# 0513更新===进程锁
#encoding=utf-8
# from multiprocessing import Process, Lock  
# import time
# def l(num,lock):  
#   lock.acquire() # 获得锁
#   time.sleep(0.2)
#   print "Hello Num: %s" % (num)  
#   lock.release() # 释放锁
# if __name__ == '__main__':
#   lock = Lock()  # 创建一个共享锁实例
#   for num in range(20): 
#       Process(target = l, args = (num,lock)).start()

# from multiprocessing import Process, Lock  
# import time
# def l(num):  
#   # lock.acquire() # 获得锁
#   time.sleep(0.2)
#   print "Hello Num: %s" % (num)  
#   # lock.release() # 释放锁
# if __name__ == '__main__':
#   lock = Lock()  # 创建一个共享锁实例
#   for num in range(20): 
#       p=Process(target = l, args = (num,))
#       p.start()
#       p.join()

# =======================
#encoding=utf-8
# import multiprocessing
# import time
# def worker(s, i):
#   s.acquire()
#   print multiprocessing.current_process().name + " acquire"
#   time.sleep(i)
#   print multiprocessing.current_process().name + " release"
#   s.release()
#  
# if __name__ == "__main__":
#   # 设置限制最多3个进程同时访问共享资源
#   s = multiprocessing.Semaphore(3)
#   for i in range(5):
#       p = multiprocessing.Process(target = worker, args = (s, i * 2))
#       p.start()

#encoding=utf-8
# import multiprocessing
# import time

# def wait_for_event(e):
#     """Wait for the event to be set before doing anything"""
#     print 'wait_for_event: starting'
#     e.wait() # 等待收到能执行信号，如果一直未收到将一直阻塞
#     print 'wait_for_event: e.is_set()->', e.is_set()

# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     print 'wait_for_event_timeout: starting'
#     e.wait(t)# 等待t秒超时,此时Event的状态仍未未设置，继续执行
#     print 'wait_for_event_timeout: e.is_set()->', e.is_set()
#     e.set()# 初始内部标志为真
    
# if __name__ == '__main__':
#     e = multiprocessing.Event()
#     print "begin,e.is_set()", e.is_set() #只有true Or false两个值
#     w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e,))
#     w1.start()

#     #可将2改为5，看看执行结果
#     w2 = multiprocessing.Process(name='nonblock', target=wait_for_event_timeout, args=(e, 2)) 
#     w2.start()

#     print 'main: waiting before calling Event.set()'
#     time.sleep(3)
#     e.set()   #可注释此句话看效果
    #print 'main: event is set'

#管道pipe
#encoding=utf-8
import multiprocessing as mp

def proc_1(pipe):
    pipe.send('hello')
    print 'proc_1 received: %s' %pipe.recv()
    pipe.send("what is your name?")
    print 'proc_1 received: %s' %pipe.recv()

def proc_2(pipe):
    print 'proc_2 received: %s' %pipe.recv()
    pipe.send('hello, too')
    print 'proc_2 received: %s' %pipe.recv()
    pipe.send("I don't tell you!")

if __name__ == '__main__':
  # 创建一个管道对象pipe
  pipe = mp.Pipe()
  print len(pipe)
  print type(pipe)
  # 将第一个pipe对象传给进程1
  p1 = mp.Process(target = proc_1, args = (pipe[0], ))
  # 将第二个pipe对象传给进程2
  p2 = mp.Process(target = proc_2, args = (pipe[1], ))
  p2.start()
  p1.start()
  p2.join()
  p1.join()

# 消费者
#encoding=utf-8
import multiprocessing as mp
import threading
import time
def consumer(cond):
  with cond:
    print("consumer before wait")
    cond.wait() # 等待消费，释放了。
    print("consumer after wait")

def producer(cond):
  with cond:
    print("producer before notifyAll")
    cond.notify_all() # 通知消费者可以消费了
    print("producer after notifyAll")

if __name__ == '__main__':    
  condition = mp.Condition()  #条件对象，默认内部有个锁

  p1 = mp.Process(name = "p1", target = consumer, args=(condition,))
  p2 = mp.Process(name = "p2", target = consumer, args=(condition,))
  p3 = mp.Process(name = "p3", target = producer, args=(condition,))

  p1.start()
  time.sleep(2)
  p2.start()
  time.sleep(2)
  p3.start()

# 进程共享数据
#encoding=utf-8
# 多进程共享数字变量
from multiprocessing import Process 
def f(n, a):
    n = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
    #print a[i]
if __name__ == '__main__':
    num = 0 #
    arr = range(10)
    p = Process(target = f, args = (num, arr)) 
    p.start()
    p.join()
    print num 
    print arr[:] #运行结果无变化

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0) # 创建一个进程间共享的数字类型，默认值为0
    arr = Array('i', range(10)) # 创建一个进程间共享的数组类型，初始值为range[10]
    p = Process(target = f, args = (num, arr))
    p.start()
    p.join()

    print num.value # 获取共享变量num的值
    print arr[:]

from multiprocessing import Process, Value, Array
def f(n):
    n.value+=1

num=Value('d')
for i in range(3):
    p=Process(target=f,args=(num,))
    p.start()
    p.join()
print num.value #多进程共享数字

#加锁同步
import time
from multiprocessing import Process, Value, Lock
class Counter(object):
    def __init__(self, initval = 0):
        self.val = Value('i', initval) 
        self.lock = Lock()

    def increment(self): 
        with self.lock:
            self.val.value += 1 # 共享变量自加1

    def value(self): 
        with self.lock:
            return self.val.value

def func(counter): 
    for i in range(50):
        time.sleep(0.01) 
        counter.increment()

if __name__ == '__main__':
    counter = Counter(0)
    procs = [Process(target =func, args = (counter,)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join() 
    print counter.value()

# 多进程共享字符串变量
#encoding=utf-8
from multiprocessing import Process, Manager, Value 
from ctypes import c_char_p

def greet(shareStr):
    shareStr.value = shareStr.value + ", World!"

if __name__ == '__main__':
    manager = Manager()
    shareStr = manager.Value(c_char_p, "Hello") 
    for i in range(4):
        process = Process(target = greet, args = (shareStr,)) 
        process.start()
        process.join()
    print shareStr.value

# 多进程共享不同类型的数据结果对象
#encoding=utf-8
from multiprocessing import Process, Manager
def f( shareDict, shareList ): 
    shareDict[1] = '1' 
    shareDict['2'] = 2 
    shareDict[0.25] = None 
    shareList.reverse() # 翻转列表

if __name__ == '__main__':
    manager = Manager()
    shareDict = manager.dict() # 创建共享的字典类型
    shareList = manager.list( range( 10 ) ) # 创 建共享的列表类型
    p = Process( target = f, args = ( shareDict,shareList ) ) 
    p.start()
    p.join()
    print shareDict 
    print shareList

# 进程间共享实例对象
import time, os
import random
from multiprocessing import Pool, Value, Lock, Manager 
from multiprocessing.managers import BaseManager
class MyManager(BaseManager): 
    pass

def Manager():
    m = MyManager() 
    m.start()
    return m

class Counter(object):
    def __init__(self, initval=0):
        self.val = Value('i', initval)
        self.lock = Lock() 

    def increment(self):
        with self.lock: 
            self.val.value += 1

    def value(self): 
        with self.lock:
            return self.val.value
 
# 将Counter类注册到Manager管理类中 
MyManager.register('Counter', Counter)

def long_time_task(name,counter):
    time.sleep(0.2)
    print 'Run task %s (%s)...\n' % (name, os.getpid()) 
    start = time.time()
#time.sleep(random.random() * 3)
    for i in range(50):
        time.sleep(0.01)
        counter.increment()
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    manager = Manager()
# 创建共享Counter类实例对象的变量，Counter类的初始值0 
    counter = manager.Counter(0)
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args = (str(i), counter)) 
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.' 
    print counter.value()

# 共享实例模板
from multiprocessing import Pool, Value, Lock, Manager 
import os, time, random

def long_time_task(name,requestCount,countList): 
    requestCount.value = requestCount.value + 1 
    print u"计数:", requestCount.value 
    countList.append(requestCount.value) 
    time.sleep(0.2)
    print 'Run task %s (%s)...\n' % (name, os.getpid()) 
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    manager = Manager() 
    requestCount = manager.Value('i',0) 
    countList = manager.list([])
    print 'Parent process %s.' % os.getpid() 
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args = (str(i),requestCount,countList))
    print 'Waiting for all subprocesses done...' 
    p.close()
    p.join()
    print 'All subprocesses done.'
    print requestCount.value 
    print countList

# 进程日志
import multiprocessing 
import logging
import sys
def worker():
    print 'I am working....' 
    sys.stdout.flush()
if __name__ == '__main__':
# 设置日志输出到控制台 
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
# 设置输出日志的级别 
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target = worker) 
    p.start()
    p.join()

#守护进程
import multiprocessing 
import time, logging 
import sys
def daemon():
    p = multiprocessing.current_process() 
    print 'Starting:', p.name, p.pid 
    sys.stdout.flush() # 将缓冲区数据写入终端 # 
    time.sleep(2)
    print 'Exiting :', p.name, p.pid 
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process() 
    print 'Starting:', p.name, p.pid 
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid 
    sys.stdout.flush()

if __name__ == '__main__':
# 设置日志输出到控制台 
    multiprocessing.log_to_stderr() 
    logger = multiprocessing.get_logger() # 设置输出日志的级别 
    logger.setLevel(logging.DEBUG)
    d = multiprocessing.Process(name='daemon', target=daemon) 
    d.daemon = True
    n = multiprocessing.Process(name='non-daemon', target=non_daemon) 
    n.daemon = False
    d.start()
    time.sleep(1)
    n.start()
    # d.join(1)
    # n.join()
    print 'd.is_alive()', d.is_alive()
    print "n.is_alive()", n.is_alive()
    print "main Process end!"