#encoding=utf-8
from selenium import webdriver
import unittest
import time, os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_uploadFileByAutoIt(self):
        url = "http://127.0.0.1/test_upload_file.html"
        # 访问自定义网页
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被点击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()
        else:
            # 查找页面上ID属性值为“file”的文件上传框,
            # 并点击调出选择文件上传框
            self.driver.find_element_by_id("file").click()
            # 通过Python提供的os模块的system方法执行生成的test.exe文件
            os.system("E:\\test.exe")
            # 由于AutoIt脚本转换后的可执行文件test.exe可能执行速度比较慢，
            # 这里等待5秒，以确保test.exe脚本执行成功
            time.sleep(5)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))
            time.sleep(2)
    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#download files
# encoding=utf-8
from selenium import webdriver
import unittest, time, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32api
import win32con

VK_CODE ={'enter':0x0D, 'down_arrow':0x28}

#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    def test_dataPickerByRightKey(self):
        # 定义将要访问的网址
        url = "http://ftp.mozilla.org/pub/mozilla.org//firefox/releases/35.0b8/win32/zh-CN/"
        self.driver.get(url)
        # 将窗口最大化
        self.driver.maximize_window()
        # 暂停5秒，目的防止页面有一些多余的弹窗占据焦点
        time.sleep(5)
        # 找到文本内容为“Firefox Setup 35.0b8.exe”超链接元素
        a = self.driver.find_element_by_link_text("Firefox Setup 35.0b8.exe")
        time.sleep(2)
        # 在找到的链接元素上模拟点击鼠标右键，
        # 以便调出选择“另存为”选项的菜单
        ActionChains(self.driver).context_click(a).perform()
        # 暂停2秒，防止命令执行太快
        time.sleep(2)
        for i in range(4):
            # 循环按4次下箭头，将焦点切换到“另存为”选项上
            # 不同浏览器此选项的位置可能不同
            #a.send_keys(Keys.DOWN)
            keyDown("down_arrow")
            keyUp("down_arrow")
            print i
            time.sleep(2)
        time.sleep(2)
        # 当焦点切换到“另存为”选项上后，模拟点击回车键
        # 调出保存下载文件路径的Windows窗体
        keyDown("enter")
        keyUp("enter")
        time.sleep(3)
        # 通过执行AutoIt编写的操作弹窗的Windows文件保存窗体
        # 完成文件保存路径的设置
        os.system("e:\\upload_file1.exe")
        # 等待文件下载完成，根据各自的网络带宽情况设定等待相应的时间
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


#datepicker
#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_datePicker(self):
        url = "http://jqueryui.com/resources/demos/datepicker/other-months.html"
        # 访问指定的网址
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的日期输入框是否可见并且能被点击
            wait.until(EC.element_to_be_clickable((By.ID, 'datepicker')))
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()
        else:
            # 查找被测试页面上的日期输入框页面元素
            dateInputBox = self.driver.find_element_by_id("datepicker")
            # 查找到日期输入框，直接输入指定格式的日期字符串
            # 就可以变相模拟在日期控件上进行选择了
            dateInputBox.send_keys("11/24/2016")
            time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#browser setting
#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class TestFailCaptureScreen(unittest.TestCase):

    def setUp(self):
        # 创建存储自定义配置文件的路径变量
        #proPath = "C:\\Users\\wuxiaohua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\tbbmxtkv.webdriver"
        # proPath = "C:\\Users\\wuxiaohua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\g6m1cswj.default"
        proPath = "/Users/ralphliu/Library/Application Support/Firefox/Profiles/xgivxd44.default" #中间空格不用加\
        
        # 加载自定义配置文件到FirefoxProfile实例中，
        # 等价profile = webdriver.FirefoxProfile(proPath)
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(proPath)
        # 将添加了新配置文件的Firefox浏览器首页设为搜狗主页
        profile.set_preference("browser.startup.homepage", "http://www.sogou.com")
        # 设置开始页面不是空白页，0表示空白页，
        # 这一步必须做，否则设置的主页不会生效
        profile.set_preference("browser.startup.page", 1)
        # 启动带自定义配置文件的Firefox浏览器
        self.driver = webdriver.Firefox(executable_path="/Users/ralphliu/Document/webdriver/geckodriver", firefox_profile=profile)

    def testSoGouSearch(self):
        # 等待5秒，以便浏览器启动完成
        time.sleep(5)
        try:
            # 找到搜狗主页搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("query")
            # 在找到的搜索输入框中输入“光荣之路自动化测试”
            searchBox.send_keys(u"光荣之路自动化测试")
            # 找到搜索按钮，并点击
            self.driver.find_element_by_id("stb").click()
            time.sleep(5)
        except NoSuchElementException, e:
            print "修改带自定义配置文件的浏览器主页不成功！"

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#图片对比
#encoding=utf-8
from selenium import webdriver
import unittest, time
from PIL import Image


class ImageCompare(object):
    '''
    本类实现了对两张图片通过像素比对的算法，获取文件的像素个数大小
    然后使用循环的方式将两张图片的所有项目进行一一对比，
    并计算比对结果的相似度的百分比
    '''
    def make_regalur_image(self, img, size=(256, 256)):
        # 将图片尺寸强制重置为指定的size大小
        # 然后再将其转换成RGB值
        return img.resize(size).convert('RGB')

    def split_image(self, img, part_size=(64, 64)):
        # 将图片按给定大小切分
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw, j + ph)).copy() \
                for i in xrange(0, w, pw) for j in xrange(0, h, ph)]

    def hist_similar(self, lh, rh):
        # 统计切分后每部分图片的相似度频率曲线
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) \
                   for l, r in zip(lh, rh)) / len(lh)

    def calc_similar(self, li, ri):
        # 计算两张图片的相似度
        return sum(self.hist_similar(l.histogram(), r.histogram())\
            for l, r in zip(self.split_image(li), self.split_image(ri))) / 16.0

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.IC = ImageCompare()
        # 启动Firefox浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_ImageComparison(self):
        url = "http://doc.outofmemory.cn/python/webpy-cookbook/"
        # 访问搜狗首页
        self.driver.get(url)
        time.sleep(3)
        # 截取第一次访问搜狗首页的图片，并保存在本地
        self.driver.save_screenshot("/Users/ralphliu/Downloads/sogou1.png")
        self.driver.get(url)
        time.sleep(3)
        # 截取第二次访问搜狗首页的图片，并保存在本地
        self.driver.save_screenshot("/Users/ralphliu/Downloads/sogou2.png")
        # 打印两张截图比对后相似度，100表示完全匹配
        print self.IC.calc_similar_by_path('/Users/ralphliu/Downloads/sogou1.png','/Users/ralphliu/Downloads/sogou2.png') * 100

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#config
#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
import ConfigParser
import os

class ObjectMap(object):
    def __init__(self):
        # 获取存放页面元素定位表达方式及定位表达式的配置文件所在绝对路径
        # os.path.abspath(__file__)表示获取当前文件所在路径目录
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__))\
                            + "\\UiObjectMap.ini"
        print self.uiObjMapPath

    def getElementObject(self, driver, webSiteName, elementName):
        try:
            # 创建一个读取配置文件的实例
            cf = ConfigParser.ConfigParser()
            # 将配置文件内容加载到内存
            cf.read(self.uiObjMapPath)
            # 根据section和option获取配置文件中页面元素的定位方式及
            # 定位表达式组成的字符串，并使用“>”分割
            locators = cf.get(webSiteName, elementName).split(">")
            # 得到定位方式
            locatorMethod = locators[0]
            # 得到定位表达式
            locatorExpression = locators[1]
            print locatorMethod, locatorExpression
            # 通过显示等待方式获取页面元素
            element = WebDriverWait(driver, 10).until(lambda x: \
                    x.find_element(locatorMethod, locatorExpression))
        except Exception, e:
            raise e
        else:
            # 当页面元素被找到后，将该页面元素对象返回给调用者
            return element

#配置文件
#encoding=utf-8
from selenium import webdriver
import unittest
import time, traceback
from ObjectMap import ObjectMap

class TestSoGouByObjectMap(unittest.TestCase):

    def setUp(self):
        self.obj = ObjectMap()
        # 启动Firefox浏览器
        self.browser=webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def testSoGouSearch(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        try:
            # 查找页面搜索输入框
            searchBox = self.obj.getElementObject\
                (self.driver, "sogou", "searchBox")
            # 在找到的搜索输入框中输入“WebDriver实战宝典”
            searchBox.send_keys(u"WebDriver实战宝典")
            # 查找搜索按钮
            searchButton = self.obj.getElementObject\
                (self.driver, "sogou", "searchButton")
            # 点击找到的搜索按钮
            searchButton.click()
            # 等待2秒，以便页面加载完成
            time.sleep(2)
            # 断言关键字“吴晓华”是否按预期出现在页面源代码中
            self.assertTrue(u"吴晓华" in self.driver.page_source, "assert error!")
        except Exception, e:
            # 打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#发送邮件
#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

# 用于设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘按键映射字典
VK_CODE = {'ctrl':0x11, 'v':0x56}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Firefox浏览器
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Firefox(executable_path="e:\\geckodriver")

    def test_SohuMailSendEMail(self):
        url = "http://mail.sohu.com"
        # 访问搜狐邮箱登录页
        self.driver.get(url)
        try:
            userName = self.driver.find_element_by_xpath\
                (u'//input[@placeholder="请输入您的邮箱"]')
            userName.clear()
            userName.send_keys("fosterwu")
            passWord = self.driver.find_element_by_xpath\
                (u'//input[@placeholder="请输入您的密码"]')
            passWord.clear()
            passWord.send_keys("1111")
            login = self.driver.find_element_by_xpath(u'//input[@value="登 录"]')
            login.click()
            wait = WebDriverWait(self.driver, 10)
            # 显示等待，确定页面是否成功登录并跳转到登录成功后的首页
            wait.until(EC.element_to_be_clickable\
                           ((By.XPATH, '//li[text()="写邮件"]')))
            self.driver.find_element_by_xpath(u'//li[text()="写邮件"]').click()
            time.sleep(2)
            receiver = self.driver.find_element_by_xpath\
                ('//div[@arr="mail.to_render"]//input')
            # 输入收件人
            receiver.send_keys("fosterwu@sohu.com")
            subject = self.driver.find_element_by_xpath\
                ('//input[@ng-model="mail.subject"]')
            # 输入邮件标题
            subject.send_keys(u"一封测试邮件！")
            # 获取邮件正文编辑区域的iframe页面元素对象
            iframe = self.driver.find_element_by_xpath\
                ('//iframe[contains(@id, "ueditor")]')
            # 通过switch_to.frame()方法切换进入富文本框中
            self.driver.switch_to.frame(iframe)
            # 获取富文本框中编辑页面元素对象
            editBox = self.driver.find_element_by_xpath("/html/body")
            # 输入邮件正文

            editBox.send_keys(u"邮件的正文内容") #input text

            self.driver.execute_script("document.getElementsByTagName('body')\
                [0].innerHTML='<b>邮件的正文内容<b>;'") #input text by js

            subject.send_keys(Keys.TAB)
            # 设置剪切板内容，也就是将要输入的正文内容
            setText(u"邮件正文内容")
            # 模拟键盘的Ctrl + v组合键，将剪切板内容粘贴到富文本编辑区中
            keyDown("ctrl")
            keyDown("v")
            keyUp("v")
            keyUp("ctrl")

            # 从富文本框中切换出，回到默认页面
            self.driver.switch_to.default_content()
            # 找到页面上的“发送”按钮，并单击它
            self.driver.find_element_by_xpath('//span[.="发送"]').click()
            # 显示都等待含有关键字串“发送成功”的页面元素出现在页面中
            wait.until(EC.visibility_of_element_located\
                           ((By.XPATH, '//span[.="发送成功"]')))
            print u"邮件发送成功"
        except TimeoutException:
            print u"显示等待页面元素超时"
        except NoSuchElementException:
            print u"寻找的页面元素不存在", traceback.print_exc()
        except Exception:
            # 打印其他异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#js
#encoding=utf-8
import unittest
from selenium import webdriver
import time

def highLightElement(driver,element):
    # 封装好的高亮显示页面元素的方法
    # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别设置为
    # 绿色和红色
    driver.execute_script("arguments[0].setAttribute('style',\
    arguments[1]);", element,"background:green; border:2px solid red;")

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        self.driver=webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_HighLightWebElement(self):
        url = "http://sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id("query")
        # 调用高亮显示元素的封装函数，将搜索输入框进行高亮显示
        highLightElement(self.driver, searchBox)
        # 等待3秒，以便查看高亮效果
        time.sleep(3)
        searchBox.send_keys(u"光荣之路自动化测试")
        submitButton = self.driver.find_element_by_id("stb")
        # 调用高亮显示元素的封装函数，将搜索按钮进行高亮显示
        highLightElement(self.driver, submitButton)
        time.sleep(3)
        submitButton.click()
        time.sleep(3)

        def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


#double keys
encoding=utf-8
import unittest
from selenium import webdriver
import time
import win32api, win32con

VK_CODE ={'ctrl':0x11, 't':0x54, 'tab':0x09}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

# 封装的按键方法
def simulateKey(firstKey, secondKey):
    keyDown(firstKey)
    keyDown(secondKey)
    keyUp(secondKey)
    keyUp(firstKey)

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
    def test_newTab(self):
        # 等待3秒，等待浏览器启动完成
        time.sleep(3)
        # 使用for循环，再新开两个新的标签页
        for i in range(2):
            simulateKey("ctrl", "t")
        # 通过Ctrl + tab组合键，将当前页面切换为默认页面，
        # 也就是最先打开的标签页
        simulateKey("ctrl", "tab")
        # 访问搜狗首页
        self.driver.get("http://sogou.com")
        self.driver.find_element_by_id("query").send_keys(u"光荣之路")
        self.driver.find_element_by_id("stb").click()
        time.sleep(3)
        #self.assertTrue(u"乔什•卢卡斯" in self.driver.page_source)

        # 获取所有的打开的窗口句柄
        all_handles = self.driver.window_handles
        print len(all_handles)
        # 将当前窗口句柄切换至第二个标签页
        self.driver.switch_to.window(all_handles[1])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys(u"WebDriver实战宝典")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertTrue(u"吴晓华" in self.driver.page_source)

        # 将当前窗口的句柄切换至第三个标签页
        self.driver.switch_to.window(all_handles[2])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertTrue("www.seleniumhq.org" in self.driver.page_source)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
