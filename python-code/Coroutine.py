#-*- coding:utf-8
'''
我们要让生产者发送1,2,3,4,5给消费者，消费者接受数字，
返回状态给生产者，而我们的消费者只需要3,4,5就行了，
当数字等于3时，会返回一个错误的状态。
最终我们需要由主程序来监控生产者－消费者的过程状态，
调度结束程序。
'''
def consumer():
    status = True
    while True:
        n = yield status
        print("我拿到了{}!".format(n))
        if n == 3:
            status = False

def producer(consumer):
    n = 5
    while n > 0:
        # yield给主程序返回消费者的状态
#generator.send(n)的作用是：把n发送generator(生成器)中yield的赋值语句中，
#同时返回generator中yield的变量（结果）
        yield consumer.send(n) 
        n -= 1
 
if __name__ == '__main__':
    c = consumer() #consumer为生成器generator
    c.send(None) #将consumer程序推进到yield处，即第5行
    p = producer(c) #同样定义为generator，并传入消费者生成器，来让producer与consumer通信
    for status in p:
        if status == False:
            print("我只要3,4,5就行啦")
            break
    print("程序结束")

'''
模拟Unix的tail -f命令的coroutine
'''
import time
def follow(thefile, target):
    thefile.seek(0,2)      # 到达文件的底部
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)
             continue
         target.send(line)
#这里定义了coroutine作为装饰器，帮我们做了send(None)的操作，免去了我们的手动调用。
def coroutine(func):
    def wrapper(*args, **kws):
        cr = func(*args, **kws)
        cr.send(None)
        return cr 
    return wrapper

@coroutine
def printer():
    while True:
         line = (yield)
         print line
#在管道中间定义一个过滤器，同样的，模拟的是UNIX中grep的功能。
def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print line,
#如此管道是这样的：follow -> grep -> printer
# f = open("access-log")
# p = printer()
# follow(f,broadcast([grep('python',p),grep('ply',p),grep('swig',p)])
#应用：演示了一个爬取公交车信息的例子，它使用了xml.sax
#来解析读取的xml信息，其中用到了事件处理和数据过滤。

@coroutine
def text_collector(target):
    while True:
        while True:
            event, value = (yield)
            if event == 'start' or event == 'end':
                target.send((event,value))
            else:
                chunks = [value]
                while True:
                    event, value = (yield)
                    if event != 'text': break
                    chunks.append(value)
                target.send(('text',"".join(chunks)))
                target.send((event,value))

@coroutine
def buses_to_dicts(target):
    while True:
        event, value = (yield)
        # Look for the start of a <bus> element</bus>
        if event == 'start' and value[0] == 'bus':
            busdict = { }
            # Capture text of inner elements in a dict
            while True:
                event, value = (yield)
                if event == 'text':  
                    textvalue = value
                elif event == 'end':
                    if value != 'bus':
                        busdict[value] = textvalue
                    else:
                        target.send(busdict)
                        break

@coroutine
def filter_on_field(fieldname,value,target):
    while True:
        d = (yield)
        if d.get(fieldname) == value:
            target.send(d)

@coroutine
def bus_locations():
    while True:
        bus = (yield)
        print "%(route)s,%(id)s,\"%(direction)s\","\
              "%(latitude)s,%(longitude)s" % bus 

if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler

    xml.sax.parse("allroutes.xml",
              EventHandler(
                   text_collector(
                   buses_to_dicts(
                   filter_on_field("route","22",
                   filter_on_field("direction","North Bound",
                   bus_locations()))))
              ))