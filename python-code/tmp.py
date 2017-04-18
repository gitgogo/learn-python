#coding=utf-8
from gevent import monkey
monkey.patch_all()
import gevent
import urllib2

def fun(url):
    print 'GET: %s'%url 
    resp=urllib2.urlopen(url)
    data=resp.read()
    print '%d bytes received from %s'%(len(data),url)

gevent.joinall([gevent.spawn(fun,'https://www.baidu.com'),
    gevent.spawn(fun,'https://www.qq.com'),
    gevent.spawn(fun,'https://github.com')])