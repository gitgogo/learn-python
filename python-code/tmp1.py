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
def bubble_sort(listx):
    xlen=len(listx)
    for i in range(xlen-1):
        for j in range(xlen-1-i):
            if listx[j]>listx[j+1]:
                listx[j],listx[j+1]=listx[j+1],listx[j]
    return listx

if __name__ == '__main__':
    print bubble_sort([2,3,1,33,12,45,12])