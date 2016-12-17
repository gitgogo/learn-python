#coding=utf-8
#实时显示文件下载进度  urlretrieve(url, filename=None, reporthook=None, data=None)
import urllib
def cbk(a, b, c): 
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    ''' 
    per = 100.0 * a * b / c 
    if per > 100: 
        per = 100 
    print '%.2f%%' % per
   
url = 'http://www.google.com'
local = 'd://google.html'
urllib.urlretrieve(url, local, cbk)