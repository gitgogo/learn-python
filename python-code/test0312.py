#coding=utf-8
from selenium import webdriver
# import unittest
from time import sleep

driver=webdriver.Firefox(executable_path=r'/Users/ralphliu/Document/webdriver/geckodriver')
driver.get('https://www.baidu.com')
sleep(3)
search=driver.find_element_by_id('kw')
search.send_keys('python')
sleep(2)
driver.find_element_by_id('su').click()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(3)
# driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()
driver.find_element_by_link_text('Python_百度百科').click()
sleep(5)

driver.close()
# driver.quit()