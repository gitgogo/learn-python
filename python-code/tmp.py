#coding=utf-8
# from selenium import webdriver
# import time
from openpyxl import load_workbook

# wb=load_workbook(filename)
# ws=wb.active
# kw=ws.rows[1][0]
# ws.cell(row=2,column=ws.max_column+1,value='xxx')
# ws.rows[2][ws.max_column+1]='xxx'

# browser=webdriver.Chrome(executable_path='/Users/ralphliu/Document/webdriver/chromedriver')
# browser.get("https://www.baidu.com")
# with open('/Users/ralphliu/Document/test/data.txt') as f:
# 	for line in f:
# 		kw=line.split('||')[0].strip().decode('utf-8')
# 		ass=line.split('||')[1].strip().decode('utf-8')

# 		time.sleep(2)
# 		browser.find_element_by_id('kw').send_keys(kw)
# 		browser.find_element_by_id('su').click()
# 		time.sleep(3)
# 		assert ass in browser.page_source
# browser.quit()
# wb=load_workbook('test.xlsx')
# ws=wb.get_sheet_by_name('student')
# print ws.rows[2][4].value
# print ws.max_row,ws.max_column
# ws.append(['append'])
# ws.cell(row=2,column=4,value='cell')
# for cell in ws.rows:
# 	for i in range(ws.max_row):
# 		print cell[i].value
#coding=utf-8
# from xml.dom import minidom
# import codecs
# domTree=minidom.parse('interview.xml')
# root=domTree.documentElement
# print root.toxml()
# print root.getAttribute('name')
# # print root.hasAttribute('comment')
# position=root.getElementsByTagName('position')
# print position[0].getAttribute('comment')
# print position[0].childNodes[0].data

#coding=utf-8
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

xml=ET.ElementTree(file='movies.xml')
# print xml.toxml()
root=xml.getroot()
print root.tag
for i in root.findall('movie'):
	for j in list(i.iter())[1:]:
		print j.tag
	break

from lettuce import *
from selenium import webdriver
import time

@step(u'启动一个浏览器')
def start_browser(step):
	world.driver=webdriver.Chrome(executable_path='')

@step(u'用户访问(.*)网址')
def visit_url(step,url):
	world.driver.get(url)

@step(u'用户输入输入用户名(.*)和密码(.*)')
def send_user_pass(step,username,passwd):
	world.driver.switch_to.frame("xxx")
	user=world.driver.find_element_by_id("xxx")
	passw=world.driver.find_element_by_id("xxx")
	user.clear()
	user.send_keys(username)
	passw.clear()
	passw.send_keys(passwd)
	passw.send_keys(Keys.RETURN)

@step(u'页面会出现(.*)关键字')
def assert_result(step,keyword):
	assert keyword in world.driver.page_source

@before.all
def say_hello():
	print u'开始测试。。。'

@before.each_scenario
def setup_some_scenario(scenario):
	print u'开始执行测试用例%s'%scenario.name

@after.each_scenario
def teardown_some_scenario(scenario):
	print u'over%s'%scenario.name

@after.all
def after_test(total):
	print u'test down...'total.scenarios_ran,total.scenarios_passed