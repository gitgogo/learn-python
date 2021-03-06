#coding=utf-8
#随机生成指定长度的数字字母序列
import random
import string
def get_random_string(num):
    return ''.join(random.choice(string.letters+string.digits) for _ in range(num))

print get_random_string(15)
#处理商品价格，取有效位小数
def handle_price(price):
    price_str=str(price)[::-1]
    for index,num in enumerate(price_str):
        if num!='0':
            return price_str[index:][::-1].strip('.')
print handle_price(23.000012000)
print handle_price(23.000)

'''
自动化测试网站登录、退出功能
'''
#coding=utf-8
import unittest
from time import sleep
from selenium import webdriver

class MyTest(unittest.TestCase):
    def setUp(self):
        self.userName='18810936553'
        self.passwd='000000'
        self.browser = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        self.browser.maximize_window()

    def test_login(self):
        self.browser.get('https://www.9drug.com')
        sleep(4)
        self.assertTrue(u'九药网' in self.browser.title)
        login=self.browser.find_element_by_link_text(u'登录')
        login.click()
        sleep(3)
        self.assertEqual(u'用户登录_九药网',self.browser.title)
        self.browser.find_element_by_id('userName').send_keys(self.userName)
        self.browser.find_element_by_id('passWord').send_keys(self.passwd)
        #cancel auto login
        auto_login=self.browser.find_element_by_name('auto_login')
        if auto_login.is_selected():
            auto_login.click()
        self.browser.find_element_by_id('login_btn').click()
        sleep(2)
        name=self.browser.find_element_by_xpath("//div[@class='login_btn']/child::a")
        self.assertEqual(u'出黄金甲AS',name.text)
        #logout
        self.browser.find_element_by_xpath("//div[@class='regist_btn']/child::a").click()
        sleep(2)
        assert u'免费注册' in self.browser.page_source

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()

#自动化发送每日练习作业

#coding=utf-8
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AutoSendEmail(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome(executable_path='/Users/ralphliu/Document/webdriver/chromedriver')
        self.browser.get('https://mail.qq.com/')
        self.name='865479851'
        self.passwd='ralph1989-11-23'
        self.subject=u'每日练习-柳栋杰'+time.strftime('%Y%m%d')
        self.filepath='/Users/ralphliu/Document/learn-python/python-code/tmp.py'

    def test_send_email(self):
        time.sleep(3)
        self.browser.switch_to_frame(0)
        self.browser.find_element_by_id('switcher_plogin').click()
        # self.browser.find_element_by_link_text(u'帐号密码登录').click()
        self.browser.find_element_by_id('u').send_keys(self.name)
        self.browser.find_element_by_id('p').send_keys(self.passwd)
        self.browser.find_element_by_id('login_button').click()
        # self.browser.implicitly_wait(15)
        time.sleep(5)
        self.assertTrue(u'退出' in self.browser.page_source)
        #编辑邮件内容
        self.browser.find_element_by_id('folder_8').click()
        time.sleep(2)
        #切换frame
        self.browser.switch_to_frame('mainFrame')
        self.browser.find_element_by_link_text(u'写群邮件').click()
        # self.browser.find_element_by_id('qqgroupid').click()
        qq_group=Select(self.browser.find_element_by_xpath('//select'))
        qq_group.select_by_visible_text(u'秋天铁血战车学习群')
        self.assertTrue(qq_group.options[-1].is_selected())
        self.browser.find_element_by_id('subject').send_keys(self.subject)
        self.browser.switch_to_frame(self.browser.find_element_by_class_name('qmEditorIfrmEditArea'))
        # with open(filepath) as f:
        #     for line in f:
        with open(self.filepath) as f:
            content=f.read().decode('utf-8','ignor')
            body=self.browser.find_element('xpath',"html/body")
            body.send_keys(u'#自动发送每日练习'+os.linesep)
            body.send_keys(content)
        time.sleep(2)
        #跳出最外层页面
        self.browser.switch_to.default_content()
        #切换到有发送按钮的页面iframe
        self.browser.switch_to_frame('mainFrame')
        self.browser.find_element_by_link_text(u'发送').click()
        self.assertTrue(u'成功' in self.browser.page_source)
        #跳出最外层页面
        self.browser.switch_to.default_content()
        # 点击退出按钮
        self.browser.find_element_by_link_text(u'退出').click()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
