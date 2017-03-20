#coding=utf-8
from selenium import webdriver
# import unittest
from time import sleep
from selenium.common.exceptions import TimeoutException

driver=webdriver.Firefox(executable_path=r'/Users/ralphliu/Document/webdriver/geckodriver')
driver.get('https://www.baidu.com')
driver.set_page_load_timeout(3) #设置加载时间，需捕获异常
try:
	driver.get('http://www.qq.com')
except TimeoutException,e: #超时异常
	print 'loading....'

print driver.page_source[:1000].encode('gbk','ignore') #获取网页源码，page_source为driver的一个静态变量【字符串】

sleep(3)
search=driver.find_element_by_id('kw')
search=driver.find_element('id','kw') #可实现数据驱动测试，自定义定位方法
search=driver.find_element_by_css_selector('#kw') #使用css定位元素
search=driver.find_element_by_tag_name('a') #通过标签获取元素
elements=find_elements_by_xpath('//a') #找出所有a标签的元素，可循环处理
elements=find_elements('xpath','//a') #同，自定义定位方式
elements=find_elements_by_tag_name('a')

driver.get_window_size() #获取浏览器窗口大小
driver.set_window_size(900,720) #设置窗口大小
driver.maximize_window() #最大化窗口
driver.get_window_position() #获取窗口的位置
driver.set_window_position(1000,500) #设置窗口位置
print driver.title #浏览器标题
driver.name
driver.port
driver.current_url
driver.window_handles
driver.get_screenshot_as_file('e:\\1.png') #截屏
driver.execute_script('js脚本')
driver.execute_script("document.getElementById('kw'),value='hello';")
drier.execute_script("return document.getElementById('query').value;")
print driver.desired_capabilities #浏览器默认设置
search.send_keys('python')
sleep(2)
driver.find_element_by_id('su').click()
sleep(2)
driver.back() #back网页返回
sleep(2)
driver.forward() #向前
sleep(3)
# driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click() #通过xpath定位元素
driver.find_element_by_link_text('Python_百度百科').click() #通过链接文本定位元素
sleep(5)

driver.close()
# driver.quit()

#homework
'''
1 ie firefox chrome三种浏览器下
2 分别截图Baidu sogou youdao
3 图片分别保存在当前日期的目录下
4 网址要保存在某个数据文件中
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime

class GetScreenshot(object):
    def __init__(self,browser):
        self.browser=browser

    def get_screenshot(self,url):
        if self.browser.lower()=='firefox':
            driver= webdriver.Firefox(executable_path='/Users/ralphliu/Document/webdriver/geckodriver')
        elif self.browser.lower()=='chrome':
            driver= webdriver.Chrome(executable_path='/Users/ralphliu/Document/webdriver/chromedriver')
        elif self.browser.lower()=='safari':
            driver= webdriver.Safari()

        driver.set_page_load_timeout(4)
        try:
            driver.get(url)
            time.sleep(3)
        except TimeoutException,e:
            print 'loading...'

        desdir=str(datetime.date.today())
        if not os.path.exists(desdir):
            os.mkdir(desdir)
        filepath=os.path.join(desdir,url.split('.')[1]+'.png')
        driver.get_screenshot_as_file(filepath)
        #save url and png
        # os.mkdir(os.path.join(os.curdir,datetime.date.today())
        with open('urls.txt','w') as f:
            f.writelines([driver.current_url])

        driver.quit()

firefox=GetScreenshot('firefox')
firefox.get_screenshot('https://www.baidu.com')
firefox.get_screenshot('https://www.dict.youdao.com')

