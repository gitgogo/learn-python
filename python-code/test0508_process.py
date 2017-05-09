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