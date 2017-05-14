#coding=utf-8
import multiprocessing
import time
class Consumer(multiprocessing.Process):
    def __init__(self,task_queue,result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue=task_queue
        self.result_queue=result_queue

    def run(self):
        proc_name=self.name
        while True:
            next_task=self.task_queue.get()
            if next_task is None:
                print "{proc_name} exiting!".format(proc_name=proc_name)
                self.task_queue.task_done()
                break
            print "{proc_name}:{next_task}".format(proc_name=proc_name,next_task=next_task)
            answer=next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return

class Task(object):
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def __call__(self):
        time.sleep(0.1)
        return "{a}*{b}={c}".format(a=self.a,b=self.b,c=self.a*self.b)
    def __str__(self):
        return "{a}*{b}".format(a=self.a,b=self.b)

if __name__ == '__main__':
    task_queue=multiprocessing.JoinableQueue()
    result_queue=multiprocessing.Queue()

    num_consumers=multiprocessing.cpu_count()
    consumers=[Consumer(task_queue,result_queue) for i in range(num_consumers)]
    for p in consumers:
        p.start()

    for i in range(10):
        task_queue.put(Task(i,i))

    for i in range(num_consumers):
        task_queue.put(None)

    task_queue.join()

    for i in range(10):
        print "Result:{result}".format(result=result_queue.get())