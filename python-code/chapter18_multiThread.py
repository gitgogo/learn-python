#coding=utf-8
#初始多线程--thread模块
import thread
from time import sleep,ctime

def loop0():
    print 'start loop 0 at:',ctime()
    sleep(4)
    print 'loop 0 done at:',ctime()

def loop1():
    print 'start loop 1 at:',ctime()
    sleep(2)
    print 'loop 1 done at:',ctime()

def main():
    print 'starting at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()

#coding=utf-8
import thread
from time import sleep,ctime
#加锁同步线程

loops=[4,2] #循环等待时长
def loop(nloop,nsec,lock):
    print 'start loop',nloop,'at',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()
    lock.release()

def main():
    print 'starting at:',ctime()
    locks=[]
    nloops=range(len(loops))

    for i in nloops:
        lock=thread.allocate_lock() #分配锁
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass

if __name__ == '__main__':
    main()
    
#使用threading模块实现多线程
#创建一个Thread的实例，传给他一个函数
loops=[4,2] #循环等待时长
def loop(nloop,nsec):
    print 'start loop',nloop,'at',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join() #等待所有线程结束

    print 'all done at:',ctime()

if __name__ == '__main__':
    main()