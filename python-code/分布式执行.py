#encoding=utf-8
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
#########################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random

# 节点主机的访问地址
host="http://192.168.1.12:6666/wd/hub"
browsers = ["firefox", "chrome", "internet explorer"]
driver = webdriver.Remote(
  # 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
  command_executor = host,
  desired_capabilities = {
        # 在browsers列表中随机选择一个浏览器
        "browserName": random.choice(browsers),
        "platform": "WINDOWS"
  })

try:
    driver.implicitly_wait(30)
    driver.maximize_window()
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

###########################################################
#多进程方式执行
#encoding=utf-8
from multiprocessing import Pool
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Manager, current_process

def node_task(name, lock, arg, successTestCases, failTestCases):
    # 获取当前进程名
    procName = current_process().name
    print procName
    time.sleep(1.2)
    print arg['node']
    print arg["browerName"]
    print 'Run task %s (%s)...\n' % (name, os.getpid())
    start = time.time()
    driver = webdriver.Remote(
        command_executor = "%s" %arg['node'],
        desired_capabilities={
            "browserName": "%s" %arg["browerName"],
            "video": "True","platform": "WINDOWS"})
    try:
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.sogou.com")
        assert u"搜狗" in driver.title
        elem = driver.find_element_by_id("query")
        elem.send_keys(u"webdriver实战宝典")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert u"吴晓华" not in driver.page_source
        # 请求获取共享资源的锁
        lock.acquire()
        # 向进程间共享列表successTestCases中添加执行成功的用例名称
        successTestCases.append("TestCase" + str(name))
        # 释放共享资源的锁，以便其他进程能获取到此锁
        lock.release()
        print "TestCase" + str(name) + " done!"
    except AssertionError,e:
        print "AssertionError occur!""testCase" + str(name)
        print e
        # 截取屏幕
        driver.save_screenshot('e:\\screenshoterror' + str(name) + '.png')
        lock.acquire()
        # 向共享列表failTestCases中添加执行失败的用例名称
        failTestCases.append("TestCase" + str(name))
        lock.release()
        print u"测试用例执行失败"
    except Exception,e:
        print "Exception occur!"
        print e
        driver.save_screenshot('e:\\screenshoterror' + str(name) + '.png')
        # 请求获得共享资源操作的锁，操作完后自动释放
        with lock:
            # 向共享列表failTestCases中添加执行失败的用例名称
            failTestCases.append("TestCase" + str(name))
        print u"测试用例执行失败"
    finally:
        driver.quit()
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

def run(nodeSeq):
    # 创建一个多进程的Manager实例
    manager = Manager()
    # 定义一个共享资源列表successTestCases
    successTestCases = manager.list([])
    # 定义一个共享资源列表failTestCases
    failTestCases = manager.list([])
    # 创建一个资源锁
    lock = manager.Lock()
    # 打印主进程的进程ID
    print 'Parent process %s.' % os.getpid()
    # 创建一个容量为3的进程池
    p = Pool(processes=3)
    testCaseNumber = len(nodeSeq)
    for i in range(testCaseNumber):
        # 循环创建子进程，并将需要的数据传入子进程
        p.apply_async(node_task, args=(i + 1, lock, nodeSeq[i],
                                       successTestCases, failTestCases))
    print 'Waiting for all subprocesses done...'
    # 关闭进程池，不再接受新的请求任务
    p.close()
    # 阻塞主进程直到子进程退出
    p.join()
    return successTestCases, failTestCases

def resultReport(testCaseNumber, successTestCases, failTestCases):
    # 下面代码用于打印本次测试报告
    print u"测试报告:\n"
    print u"共执行测试用例:" + str(testCaseNumber) + u"个\n"
    print u"成功的测试用例:", str(len(successTestCases))
    if len(successTestCases) > 0:
        for t in successTestCases:
            print t
    else:
        print u"无"
    print u"失败的测试用例:", str(len(failTestCases))
    if len(failTestCases) > 0:
        for t in failTestCases:
            print t
    else:
        print u"无"

if __name__ == '__main__':
    # 节点列表
    nodeList=[
        {"node":"http://172.29.10.127:6666/wd/hub","browerName":"internet explorer"},
        {"node":"http://172.29.10.127:6666/wd/hub","browerName":"chrome"},
        {"node":"http://172.29.10.127:6666/wd/hub", "browerName":"firefox"}]
    # 获取节点个数
    testCaseNumber = len(nodeList)
    # 开始多进程分布式测试
    successTestCases, failTestCases = run(nodeList)
    print 'All subprocesses done.'
    # 在控制台中打印测试报告
    resultReport(testCaseNumber, successTestCases, failTestCases)