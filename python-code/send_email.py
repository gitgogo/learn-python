#coding=utf-8
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class AutoSendEmail(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        self.browser.get('https://mail.qq.com/')
        self.name='865479851'
        self.passwd='ralph1989-11-23'
        self.subject=u'每日练习-柳栋杰'+time.strftime('%Y%m%d')
        self.filepath='/Users/ralphliu/Document/learn-python/python-code/tmp.py'

    def test_send_email(self):
        self.browser.maximize_window()
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
            body=self.browser.find_element('xpath',"html/body")
            # body.send_keys(u'#自动发送每日练习'+os.linesep)
            for line in f:
                body.send_keys(line.decode('utf-8','ignore'))

        time.sleep(2)
        #跳出最外层页面
        self.browser.switch_to.default_content()
        #切换到有发送按钮的页面iframe
        self.browser.switch_to.frame('mainFrame')
        WebDriverWait(self.browser,10,0.2).until(lambda x:x.find_element_by_name('sendbtn')).click()
        # self.browser.find_element_by_link_text(u'发送').click()
        # self.browser.implicitly_wait(10)
        # element = WebDriverWait(driver, 10).until(lambda x: \
        #             x.find_element(locatorMethod, locatorExpression))
        WebDriverWait(self.browser, 10).until(
            lambda x:self.assertTrue(u'已发送' in x.page_source))
        # self.assertTrue(u'邮件已发送' in self.browser.page_source)
        print u'邮件已发送！'
        #跳出最外层页面
        self.browser.switch_to.default_content()
        # 点击退出按钮
        self.browser.find_element_by_link_text(u'退出').click()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()