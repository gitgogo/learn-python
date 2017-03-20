#coding=utf-8
#随机生成指定长度的数字字母序列
import random
import string
def get_random_string(num):
    return ''.join(random.choice(string.letters+string.digits) for _ in range(num))

print get_random_string(15)
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

