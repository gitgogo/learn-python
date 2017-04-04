#coding=utf-8
#encoding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard as w
import win32con
import time
import win32api


# 读取剪切板
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

# 设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

VK_CODE ={
    'enter':0x0D,
    'ctrl':0x11,
    'a':0x41,
    'v':0x56,
    'x':0x58
    }

#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)

#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_copyAndPaste(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 定义即将要被设置到剪切板中的内容
        content = u'光荣之路'
        # 将content变量中的内容设置到剪切板中
        setText(content)
        # 从剪切板中获取刚设置到剪切板中的内容
        getContent = getText()
        print getContent
        # 将焦点切换到搜索输入框中
        self.driver.find_element_by_id("kw").click()
        time.sleep(1)
        keyDown('ctrl')
        keyDown('v')
        # 释放Ctrl + v组合键
        keyUp('v')
        keyUp('ctrl')
        # 点击“百度一下”搜索按钮
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#ctrl a
#encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

 
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_simulationCombinationKeys(self):
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 将焦点切换到搜索输入框中
        input = self.driver.find_element_by_id("kw")
        input.send_keys(u"光荣之路")
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.COMMAND).send_keys('a').\
        key_up(Keys.COMMAND).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.COMMAND).send_keys('x').\
        key_up(Keys.COMMAND).perform()
        self.driver.get(url)
        self.driver.find_element_by_id("kw").click()
        # 模拟Ctrl + V组合键，将从剪切板中获取到的内容粘贴到搜索输入框中
        ActionChains(self.driver).key_down(Keys.COMMAND).send_keys('v').\
        key_up(Keys.COMMAND).perform()
        # 点击“百度一下”搜索按钮
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#鼠标操作
#encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import win32clipboard as w
import win32con

# 设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_rigthClickMouse(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        # 找到搜索输入框
        searchBox = self.driver.find_element_by_id("query")
        # 将焦点切换到搜索输入框
        searchBox.click()
        time.sleep(2)
        # 在搜索输入框上执行一个鼠标右键点击操作
        ActionChains(self.driver).context_click(searchBox).perform()
        # 将“gloryroad”数据设置到剪切板中，相当于执行了复制操作
        setText(u'gloryroad')
        # 发送一个粘贴命令，字符p指代粘贴操作
        ActionChains(self.driver).send_keys('P').perform()
        # 点击搜索按钮
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def isElementPresent(self, by, value):
        # 从selenium.common.exceptions模块导入NoSuchElementException异常类
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element(by=by, value=value)
        except NoSuchElementException, e:
            # 打印异常信息
            print e
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True
    
    
    def test_isElementPresent(self):
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 判断页面元素id属性值为“query”的页面元素是否存在
        res = self.isElementPresent("id", "query")
        if res is True:
            print u"所查找的元素存在于页面上！"
        else:
            print u"页面中未找到所需要的页面元素！"



    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_roverOnElement(self):
        url = "http://localhost/test_mouse_hover.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 找到页面上第一个链接元素
        link1 = self.driver.find_element_by_partial_link_text(u"指过来1")
        # 找到页面上第二个链接元素
        link2 = self.driver.find_element_by_partial_link_text(u"指过来2")
        # 找到页面上的p元素
        p = self.driver.find_element_by_xpath("//p")
        print link1.text, link2.text
        # 导入需要的Python包
        from selenium.webdriver import ActionChains
        import time
        # 将鼠标悬浮到第一个链接元素上
        ActionChains(self.driver).move_to_element(link1).perform()
        time.sleep(2)
        # 将鼠标从第一个链接元素移动到p元素上
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)
        # 将鼠标悬浮到第二个链接元素上
        ActionChains(self.driver).move_to_element(link1).perform()
        time.sleep(2)
        # 将鼠标从第二个链接元素移动到p元素上
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#等待。。。。
#coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_explicitWait(self):
        # 导入堆栈类
        import traceback
        # 导入By类
        from selenium.webdriver.common.by import By
        # 导入显示等待类
        from selenium.webdriver.support.ui import WebDriverWait
        # 导入期望场景类
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException, NoSuchElementException
        url = "http://127.0.0.1/test_explicity_wait.html"
        # 访问自动以测试网页
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            wait.until(EC.title_is(u"你喜欢的水果"))
            print u"网页标题是“你喜欢的水果”"
            # 等待10秒，直到要找的按钮出现
            element = WebDriverWait(self.driver, 10).until\
                (lambda x: x.find_element_by_xpath("//input[@value='Display alert box']"))
            element.click()
            # 等待alert框出现
            alert = wait.until(EC.alert_is_present())
            # 打印alert框体消息
            print alert.text
            # 确认警告信息
            alert.accept()
            # 获取id属性值为“peach”的页面元素
            peach = self.driver.find_element_by_id("peach")
            # 判断id属性值为“peach”的页面元素是否能被选中
            peachElement = wait.until(EC.element_to_be_selected(peach))
            print u"下拉列表的选项“桃子”目前处于选中状态"
            # 判断复选框是否可见并且能被点击
            wait.until(EC.element_to_be_clickable((By.ID, 'check')))
            print u"复选框可见并且能被点击"
        except TimeoutException, e:
            # 捕获TimeoutException异常
            print traceback.print_exc()
        except NoSuchElementException, e:
            # 捕获NoSuchElementException异常
            print traceback.print_exc()
        except Exception, e:
            # 捕获其他异常
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#切换多窗口
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_identifyPopUpWindowByTitle(self):
        # 导入多个异常类型
        from selenium.common.exceptions import NoSuchWindowException, \
            TimeoutException
        # 导入期望场景类
        from selenium.webdriver.support import expected_conditions as EC
        # 导入By类
        from selenium.webdriver.common.by import By
        # 导入WebDriverWait类
        from selenium.webdriver.support.ui import WebDriverWait
        # 导入堆栈类
        import traceback
        # 导入时间模块
        import time
        url = "http://127.0.0.1/test_popup_window.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 显示等待找到页面上链接文字为“sogou 搜索”的链接元素，找到后点击它
        WebDriverWait(self.driver, 10, 0.2).until(EC.element_to_be_clickable \
                                                      ((By.LINK_TEXT, 'sogou 搜索'))).click()
        # 获取当前所有打开的浏览器窗口句柄
        all_handles = self.driver.window_handles
        # 打印当前浏览器窗口句柄
        print self.driver.current_window_handle
        # 打印打开的浏览器窗口的个数
        print len(all_handles)
        # 等待2秒，以便更好查看效果
        time.sleep(2)
        # 如果存储浏览器窗口句柄的容器不对空，再遍历all_handles中所有的浏览器句柄
        if len(all_handles) > 0:
            try:
                for windowHandle in all_handles:
                    # 切换窗口
                    self.driver.switch_to.window(windowHandle)
                    print self.driver.title
                    # 判断当前浏览器窗口的title属性是否等于
                    # “搜狗搜索引擎 - 上网从搜狗开始”
                    if u'上网' in self.driver.title: #if u'喜欢' in self.driver.page_source:
                        # 显示等待页面搜索输入框加载完成，
                        # 然后输入“sogou 首页的浏览器窗口被找到”
                        WebDriverWait(self.driver, 10, 0.2).until \
                            (lambda x: x.find_element_by_id("query")). \
                            send_keys(u"sogou 首页的浏览器窗口被找到")
                        print self.driver.title
                        time.sleep(2)
            except NoSuchWindowException, e:
                # 捕获NoSuchWindowException异常
                print traceback.print_exc()
            except TimeoutException, e:
                # 捕获TimeoutException异常
                print traceback.print_exc()
        # 将浏览器窗口切换回默认窗口
        self.driver.switch_to.window(all_handles[0])
        print self.driver.title
        # 断言当前浏览器窗口的title属性是“你喜欢的水果”
        self.assertEqual(self.driver.title, u"你喜欢的水果")


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#coding=utf-8
#encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_HandleFrame(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException
        url = "http://127.0.0.1/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 使用索引方式进入指定的frame页面，索引号从0开始。
        # 所以想进入中间的frame，需要使用索引号1
        # 如果没有使用此行代码，则无法找到页面中左侧frame中的任何页面元素
        self.driver.switch_to.frame(0)
        # 找到左侧frame中的p标签元素
        leftFrameText = self.driver.find_element_by_xpath("//p")
        # 断言左侧frame中的文字是否和“这是左侧 frame 页面上的文字”几个关键字相一致
        self.assertAlmostEqual(leftFrameText.text, u"这是左侧 frame 页面上的文字")
        # 找到左侧frame中的按钮元素，并点击该元素
        self.driver.find_element_by_tag_name("input").click()
        try:
            # 动态等待alert窗体出现
            alertWindow = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # 打印alert消息
            print alertWindow.text
            alertWindow.accept()
        except TimeoutException, e:
            print e
        # 使用driver.switchTo.default_content方法，从左侧frame中返回到frameset页面
        # 如果不调用此行代码，则无法从左侧frame页面中直接进入其他frame页面
        self.driver.switch_to.default_content()
    
        # 通过标签名找到页面中所有的frame元素，然后通过索引进入该frame
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("frame")[1])
        # 断言页面源码中是否存在“这是中间 frame 页面上的文字”关键子串
        assert u"这是中间 frame 页面上的文字" in self.driver.page_source
        # 再输入框中输入“我在中间frame”
        self.driver.find_element_by_tag_name("input").send_keys(u"我在中间frame")
        self.driver.switch_to.default_content()
    
        self.driver.switch_to.frame(self.driver.find_element_by_id("rightframe"))
        assert u"这是右侧 frame 页面上的文字" in self.driver.page_source
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("rightframe")
        assert u"这是右侧 frame 页面上的文字" in self.driver.page_source
        self.driver.switch_to.default_content()
        
    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#switch to frame
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_HandleFrame(self):
        # from selenium.webdriver.support import expected_conditions as EC
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.common.exceptions import TimeoutException
        url = "http://mail.126.com/"
        # 访问自动以测试网页
        self.driver.get(url)
        # log_tag=self.driver.find_element_by_id("lbNormal")
        self.driver.switch_to_frame('x-URS-iframe')

        # log_tag.click()
        time.sleep(2)
        self.driver.find_element_by_name('email').send_keys('liudongjie2015')
        self.driver.find_element_by_name('password').send_keys('liudongjie126')
        self.driver.find_element_by_id('dologin').click()
        self.driver.implicity_wait(10)
        # logout=self.driver.find_element_by_id
        self.assertTrue(u'退出' in self.driver.page_source)
        print self.driver.title
        self.driver.find_element_by_link_text(u'退出').click()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_HandleFrameByPageSource(self):
        url = "http://127.0.0.1/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 找到页面上所有的frame页面对象，并存储到名为framesList列表中
        framesList = self.driver.find_elements_by_tag_name("frame")
        # 通过for循环遍历framesList中所有的frame页面，查找页面源码中含有
        # “中间 frame”的frame页面
        for frame in framesList:
            # 进入与frame页面
            self.driver.switch_to.frame(frame)
            # 判断每个frame的HTML源码中是否包含“中间 frame”几个关键词
            if u"中间 frame" in self.driver.page_source:
                # 如果包含需要查找的关键字，则查找到页面上的p标签元素
                p = self.driver.find_element_by_xpath("//p")
                # 断言页面上p元素文本内容是否是“这是中间 frame 页面上的文字”
                self.assertAlmostEqual(u"这是中间 frame 页面上的文字", p.text)
                # 退出frame
                self.driver.switch_to.default_content()
                # 找到指定的frame页面，并作相应的操作后退出循环
                break
            else:
                # 若果没找到指定的frame，则调用此行代码，返回到frameset页面中
                # 以便下次for循环中能继续调用driver.switch_to.frame方法,否则会报错
                self.driver.switch_to.default_content()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_HandleIFrame(self):
        url = "http://127.0.0.1/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 改变操作区域，切换进入页面上第一个frame，也就是左边的frame
        self.driver.switch_to.frame(0)
        # 断言页面是否存在“这是左侧 frame 页面上的文字”关键字串，
        # 以判断是否成功切换进frame页面
        assert u"这是左侧 frame 页面上的文字" in self.driver.page_source
        
        # 改变操作区域，切换进入id为“showIfame”的iframe页面
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe"))
        # 断言页面是否存在“这是iframe页面上的文字”这样的关键字串，
        # 以便判断是否成功切换进iframe页面
        assert u"这是iframe页面上的文字" in self.driver.page_source
    
        # 将操作区域切换到frameset页面，以便能成功进入其他frame
        self.driver.switch_to.default_content()
        # 断言页面的title值是否为“frameset 页面”
        assert u"frameset 页面" == self.driver.title
    
      


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_HandleAlert(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = "http://127.0.0.1/test_alert.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 通过id属性值查找页面上的按钮元素
        button = self.driver.find_element_by_id("button")
        # 单击按钮元素，则会弹出一个Alert消息框，
        # 上面显示“这是一个alert弹出框”和“确定”按钮
        button.click()

        try:
            # 使用driver.switch_to_alert()方法获取alert对象
            alert = self.driver.switch_to_alert()
            time.sleep(2)
            # 使用alert.text属性获取alert框中的内容，
            # 并断言文字内容是否是“这是一个 alert 弹出框”
            self.assertAlmostEqual(alert.text, u"这是一个 alert 弹出框")
            # 调用alert对象的accept()方法，模拟鼠标单击alert弹窗上的“确定”按钮
            # 以便关闭alert窗
            alert.accept()
        except NoAlertPresentException, e:
            # 如果Alert框未弹出显示在页面上，则会抛出NoAlertPresentException的异常
            self.fail("尝试操作的 alert 框未被找到")
            print e

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_Handleconfirm(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = "http://127.0.0.1/test_confirm.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 通过id属性值查找页面上的按钮元素
        button = self.driver.find_element_by_id("button")
        # 单击按钮元素，则会弹出一个confirm提示框，
        # 上面显示“这是一个 confirm 弹出框”、“确定”和“取消”按钮
        button.click()
        try:
            # 较高版本的selenium推荐使用driver.switch_to.alert方法代替
            # driver.switch_to_alert()方法来获取alert对象
            alert = self.driver.switch_to.alert
            time.sleep(2)
            # 使用alert.text属性获取confirm框中的内容，
            # 并断言文字内容是否是“这是一个 confirm 弹出框”
            self.assertAlmostEqual(alert.text, u"这是一个 confirm 弹出框")
            # 调用alert对象的accept()方法，模拟鼠标单击confirm弹窗上的“确定”按钮
            # 以便关闭confirm窗
            #alert.accept()
            # 取消下面一行代码的注释，就会模拟单击confirm框上的“取消”按钮
            alert.dismiss()
        except NoAlertPresentException, e:
            # 如果confirm框未弹出显示在页面上，则会抛出NoAlertPresentException的异常
            self.fail("尝试操作的confirm框未被找到")
            print e

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def testHandlePrompt(self):
        url = "http://127.0.0.1/test_prompt.html"
        # 访问自定义网页
        self.driver.get(url)
        # 使用id定位方式，找到被测试网页上唯一按钮元素
        element = self.driver.find_element_by_id("button")
        element.click()
        time.sleep(2)
        # 单击按钮元素，弹出一个prompt提示框，
        # 上面将显示“这是一个prompt弹出框”、输入框、
        # “确定”按钮和“取消”按钮
        # 使用driver.switch_to_alert()方法获取Alert对象
        alert = self.driver.switch_to.alert
        # 使用alert.text方法获取prompt框上面的文字，
        # 并断言文字内容是否和“这是一个 prompt 弹出框”一致
        self.assertEqual(u"这是一个 prompt 弹出框", alert.text)
        time.sleep(1)
        # 调用alert.send_keys()方法，在prompt窗体的输入框中输入
        # “光荣之路：要想改变命运，必须每天学习2小时！”
        # alert.send_keys(u"光荣之路：要想改变命运，必须每天学习2小时！")
        alert.send_keys('hello world!!!')
        time.sleep(1)
        # 使用alert对象的accept方法，
        # 点击prompt框的“确定”按钮，关闭prompt框
        alert.accept()
        # 使用alert对象的dismiss方法，单击prompt框上的“取消”按钮，关闭prompt框
        # 取消下面一行代码的注释，就会模拟单击prompt框上的“取消”按钮
        # alert.dismiss()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_Cookie(self):
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 得到当前页面下所有的Cookies，并输出它们所在域、name、value、有效期和路径
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print "%s -> %s -> %s -> %s -> %s" \
                  % (cookie['domain'], cookie["name"], cookie["value"], \
                     cookie["expiry"], cookie["path"])
    
        # 根据Cookie的name值获取该条Cookie信息，获取name值为'SUV'的Cookie信息
        ck = self.driver.get_cookie("SUV")
        print "%s -> %s -> %s -> %s -> %s" \
              % (ck['domain'], ck["name"], ck["value"], \
                 ck["expiry"], ck["path"])
    
        # 删除cookie有2种方法
        # 第一种：通过Cookie的name属性，删除name值为“ABTEST”的Cookie信息
        print self.driver.delete_cookie("ABTEST")
    
        # 第二种：一次性删除全部Cookie信息
        self.driver.delete_all_cookies()
        # 删除全部Cookie后，再次查看Cookies，确认是否已被全部删除
        cookies = self.driver.get_cookies()
        print cookies
    
        # 添加自定义Cookie信息
        self.driver.add_cookie({"name": "gloryroadTrain", 'value': '1479697159269020'})
        # 查看添加的Cookie信息
        cookie = self.driver.get_cookie("gloryroadTrain")
        print cookie

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class setPageLoadTime(unittest.TestCase):
    def setUp(self):
        # 启动火狐浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_PageLoadTime(self):
        # 设定页面加载限制时间为4秒
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            startTime = time.time()
            self.driver.get("http://mail.126.com")
        except TimeoutException:
            print u'页面加载超过设定时间，超时'
            # 当页面加载时间超过设定时间，
            # 通过执行Javascript来stop加载，然后继续执行后续动作
            self.driver.execute_script('window.stop()')
        end = time.time() - startTime
        print end
        # 切换进frame控件
        self.driver.switch_to.frame("x-URS-iframe")
        # 获取用户名输入框
        userName = self.driver.find_element_by_xpath('//input[@name="email"]')
        # 输入用户名
        userName.send_keys("liudongjie2015")
        # 获取密码输入框
        pwd = self.driver.find_element_by_xpath("//input[@name='password']")
        # 输入密码
        pwd.send_keys("liudongjie126")
        # 发送一个回车键
        pwd.send_keys(Keys.RETURN)
        time.sleep(5)
        assert u"退出" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        #self.driver = webdriver.Chrome(executable_path = "c:\\chromedriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_executeScript(self):
        url = "http://www.sogou.com"
        # 访问baidu首页
        self.driver.get(url)
        # 构造JavaScript查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('query').value='光荣之路';"
        # 构造JavaScript查找百度首页的搜索按钮的代码字符串
        searchButtonJS = "document.getElementById('stb').click()"
        try:
            # 通过JavaScript代码在百度首页搜索输入框中输入“光荣之路”
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            # 通过JavaScript代码点击百度首页上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue(u"光荣之路" in self.driver.page_source)
        except WebDriverException, e:
            # 当定位失败时，会抛出WebDriverException异常
            print u"在页面中没有找到要操作的页面元素 ",traceback.print_exc()
        except AssertionError, e:
            print u"页面不存在断言的关键字串"
        except Exception, e:
            # 发生其他异常时，打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_scroll(self):
        url = "http://www.sohu.com/"
        # 访问selenium官网首页
        try:
            self.driver.get(url)
            # 使用JavaScript的scrollTo函数和document.body.scrollHeight参数
            # 将页面的滚动条滑动到页面的最下方
            for i in range(20):

                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.execute_script('window.scrollBy(0,100);')

                # self.driver.execute_script("window.scrollTo(0, 0);")
                # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
                # 根据测试需要，可注释下面的停顿代码
                # time.sleep(2)
                # self.driver.execute_script("window.scrollTo(0, 0);")
                # self.driver.execute_script('window.scrollBy(0,30);')
                # 使用JavaScript的scrollIntoView函数将被遮挡的元素滚动到可见屏幕上
                # scrollIntoView(true)表示将元素滚到屏幕中间
                # scrollIntoView(false)表示将元素滚动屏幕底部
                # self.driver.execute_script("document.getElementsByTagName('a')[500].scrollIntoView(true);")
                #for i in range(10,900):
                #driver.execute_script("document.getElementsByTagName('a')[%s].scrollIntoView(true);" %i)

                #("document.getElementById('choice').scrollIntoView(true);")
                # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
                # 根据测试需要，可注释下面的停顿代码
                time.sleep(2)

            # 使用JavaScript的scrollTo方法，使用0和400横纵坐标参数，
            # 将页面纵向向下滚动400像素
            self.driver.execute_script("window.scrollBy (0,400);")
            # 停顿3秒，用于人工验证滚动条是否滑动到指定的位置。
            # 根据测试需要，可注释下面的停顿代码
            time.sleep(3)
        except Exception, e:
            # 打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_AjaxDivOptionByKeys(self):
        url = "http://www.sogou.com/"
        # 访问sogou的首页
        self.driver.get(url)
        # 找到搜狗首页中的搜索输入框页面元素
        searchBox = self.driver.find_element_by_id("query")
        # 在搜索输入框中输入“光荣之路”
        searchBox.send_keys(u"光荣之路")
        # 等待2秒，以便悬浮框加载完成
        time.sleep(2)
        for i in range(3):
            # 选择悬浮框中中第几个联想关键词选项就循环几次
            # 模拟键盘点击下箭头
            searchBox.send_keys(Keys.DOWN)
            time.sleep(0.5)
        # 当按下箭头到想要选择的选项后，再模拟键盘点击回车键，选中该选项
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_AjaxDivOptionByIndex(self):
        url = "http://www.baidu.com/"
        # 访问sogou的首页
        self.driver.get(url)
        try:
            # 找到搜狗首页中的搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("kw")
            # 在搜索输入框中输入“光荣之路”
            searchBox.send_keys(u"光荣之路")
            # 等待2秒，以便悬浮框加载完成
            time.sleep(2)
            # 查找浮动框中的第三选项，只要更改li[3]中的索引数字，
            # 就可以实现任意单击选项浮动框中的选项。注意，索引从1开始
            suggetion_option = self.driver. \
                find_element_by_xpath(".//*[@id='form']/div/ul/li[3]")
            # 点击找到的选项
            print suggetion_option.get_attribute('data-key')
            suggetion_option.click()
            time.sleep(3)
        except NoSuchElementException, e:
            # 打印异常堆栈信息
            print traceback.print_exc()


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_AjaxDivOptionByWords(self):
        url = "http://www.sogou.com/"
        # 访问sogou的首页
        self.driver.get(url)
        try:
            # 找到搜狗首页中的搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("query")
            # 在搜索输入框中输入“光荣之路”
            searchBox.send_keys(u"光荣之路")
            # 等待2秒，以便悬浮框加载完成
            time.sleep(2)
            # 查找内容包含“篮球电影”的悬浮选项
            suggetion_option = self.driver.\
                find_element_by_xpath("//ul/li[contains(., '电影')]")
            # 点击找到的选项
            suggetion_option.click()
            time.sleep(3)
        except NoSuchElementException, e:
            # 打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


import os

class VisitSogouByIE(unittest.TestCase):


    def test_killWindowsProcess(self):
        # 启动火狐浏览器
        firefox = webdriver.Firefox(executable_path = "/Users/ralphliu/Document/webdriver/geckodriver")
        # 启动IE浏览器
        safari = webdriver.Safari()
        # 启动Chrome浏览器
        chrome = webdriver.Chrome(executable_path="/Users/ralphliu/Document/webdriver/chromedriver")
        # 导入Python的os包
        import os
        # 结束Firefox浏览器进程
        returnCode = os.system("taskkill /F /iM firefox.exe")
        if returnCode == 0:
            print u"成功结束Firefox浏览器进程！"
        else:
            print u"结束Firefox浏览器进程失败！"
        # 结束IE浏览器进程
        returnCode = os.system("taskkill /F /iM iexplore.exe")
        if returnCode == 0:
            print u"成功结束IE浏览器进程！"
        else:
            print u"结束IE浏览器进程失败！"
        # 结束Chrome浏览器进程
        returnCode = os.system("taskkill /F /iM chrome.exe")
        if returnCode == 0:
            print u"成功结束Chrome浏览器进程！"
        else:
            print u"结束Chrome浏览器进程失败！"


if __name__ == '__main__':
    unittest.main()

def addAttribute(driver, elementObj, attributeName, value):
    # 封装向页面标签中添加新属性方法
    # 调用JavaScript代码给页面标签添新属性，arguments[0]－［2］分别会用后面的
    # element、attributeName和value参数值进行替换，并执行该JavaScript代码
    # 添加新属性的JavaScript代码语法为：element.attributeName = value
    # 比如input.name="test"
    driver.execute_script("arguments[0].%s=arguments[1]" %attributeName,\
                          elementObj, value)

def setAttribute(driver, elementObj, attributeName, value):
    # 封装设置页面对象的属性值的方法
    # 调用JavaScript代码修改页面元素的属性值，arguments[0]－［2］分别会用后面的
    # element、attributeName和value参数值进行替换，并执行该JavaScript代码
    driver.execute_script("arguments[0].setAttribute\
    (arguments[1],arguments[2])", elementObj, attributeName, value)

def getAttribute(elementObj, attributeName):
    # 封装获取页面对象的属性值的方法
    return elementObj.get_attribute(attributeName)

def removeAttribute(driver, elementObj, attributeName):
    # 封装删除页面元素属性的方法
    # 调用JavaScript代码删除页面元素的指定的属性，arguments[0]－［1］分别会用后面的
    # element、attributeName参数值进行替换，并执行该JavaScript代码
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",\
                          elementObj, attributeName)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Chrome(executable_path = "e:\\chromedriver")
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
    def test_dataPicker(self):
        url = "http://127.0.0.1/test_change_attr.html"
        # 访问自定义网页
        self.driver.get(url)
        # 找到页面上标签名为input的页面元素
        element = self.driver.find_element_by_xpath("//input")

        # 向页面文本框input标签中添加新属性name="search"
        addAttribute(self.driver, element, 'name', "search")
        # 添加新属性后，查看一下新添加的属性
        print u'添加的新属性值%s="%s"' %("name", getAttribute(element, "name"))

        # 查看修改前文本框input标签的value属性值
        print u"更改文本框中的内容前的内容：", getAttribute(element, "value")
        # 更改input页面元素的value属性值为“这是更改后的文字内容”
        setAttribute(self.driver, element, "value", u"xxxxxxx")
        # 更改input页面元素的value属性值后，再次查看其value属性值
        print u"更改文本框中内容后的内容：", getAttribute(element, "value")
        time.sleep(3)

        # 查看修改前文本框input页面元素中的size属性值
        print u"更改前文本框标签中的size属性值：", getAttribute(element, "size")
        # 更改input页面元素的size属性值为“20”
        setAttribute(self.driver, element, "size", 20)
        # 更改input页面元素的size属性值后，再次查看其size属性值
        print u"更改后文本框标签中的size属性值：", getAttribute(element, "size")
        time.sleep(3)

        # 查看删除input页面元素value属性前value属性值
        print u"文本框value属性值：", getAttribute(element, "value")
        # 删除文本框的value属性
        removeAttribute(self.driver, element, "value")
        # 删除文本框的value属性后，再次查看value属性值
        print u"删除value属性值后value属性值：", getAttribute(element, "value")
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#下载文件
class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建一个FirefoxProfile实例，用于存放自定义配置
        profile = webdriver.FirefoxProfile()
        # 指定下载路径，默认只会自动创建一级目录，如果指定了
        # 多级不存在的目录，将会下载到默认路径
        profile.set_preference('browser.download.dir', 'd:\\iDownload')
        # 将browser.download.folderList设置为2，表示将文件下载到指定路径
        # 设置成2表示使用自定义下载路径；
        # 设置成0表示下载到桌面；设置成1表示下载到默认路径
        profile.set_preference('browser.download.folderList', 2)
        # browser.helperApps.alwaysAsk.force对于未知的 MIME 类型文件会弹出窗口
        # 让用户处理，默认值为true，设定为False表示不会记录打开未知 MIME 类型
        # 文件的方式
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        # 在开始下载时是否显示下载管理器
        profile.set_preference('browser.download.manager.showWhenStarting',\
                               False)
        # 设定为 False 会把下载框进行隐藏
        profile.set_preference("browser.download.manager.useWindow", False)
        # 默认值为 true，设定为 False 表示不获取焦点
        profile.set_preference("browser.download.manager. focusWhenStarting",\
                               False)
        # 下载.exe文件弹出警告，默认值是 true，设定为False 则不会弹出警告框
        profile.set_preference("browser.download.manager.alertOnEXEOpen",\
                               False)
        # browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框
        # 默认值为空字符串，下行代码行设定了多种文件的 MIME类型，
        # 例如application/exe，表示.exe类型的文件，
        # application/excel表示 Excel 类型的文件
        profile.set_preference("browser.helperApps.neverAsk.openFile", \
                               "application/pdf")
        # 对所给出文件类型不再弹出框进行询问，直接保存到本地磁盘
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', \
                               'application/zip, application/octet-stream')
        # browser.download.manager.showAlertOnComplete设定下载文件结束后是否显示下
        #载完成提示框，默认为true，设定为False表示下载完成后不显示下载完成提示框
        profile.set_preference("browser.download.manager. showAlertOnComplete",\
                               False);
        # browser.download.manager.closeWhenDone设定下载结束后是否自动
        # 关闭下载框，默认值为true，设定为False 表示不关闭下载管理器
        profile.set_preference("browser.download.manager.closeWhenDone",\
                               False)

        # self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")
        # 启动浏览器时，通过firefox_profile参数
        # 将自动以配置添加到FirefoxProfile对象中
        self.driver = webdriver.Firefox(executable_path="/Users/ralphliu/Document/webdriver/geckodriver",\
                                        firefox_profile = profile)

    def test_dataPicker(self):
        # 访问WebDriver驱动Firefox的驱动文件下载网址
        url1 = "https://github.com/mozilla/geckodriver/releases"
        self.driver.get(url1)
        # 选择下载zip类型文件，使用application/zip指代此类型文件
        self.driver.find_element_by_xpath\
            ('//strong[.="geckodriver-v0.11.1-win64.zip"]').click()
        # 等待加载下载文件
        time.sleep(10)

        # 访问Python2.7.12文件下载页面，下载扩展名为msi文件
        # 使用application/octet-stream来指明此类文件类型
        url = "https://www.python.org/downloads/release/python-2712/"
        self.driver.get(url)
        # 找到Python2.7.12下载页面中链接文字为“Windows x86-64 MSI installer”
        # 的链接页面元素，点击进行无人工干预的下载Python2.7.12解释器文件
        self.driver.find_element_by_link_text\
            ("Windows x86-64 MSI installer").click()
        # 等待文件下载完成，根据各自的网络带宽情况设定等待相应的时间
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


import win32clipboard as w
import win32api
import win32con
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 用于设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘按键映射字典
VK_CODE = {
    'enter':0x0D,
    'ctrl':0x11,
    'v':0x56}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")

    def test_uploadFileByKeyboard(self):
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
            # 将即将要上传的文件名及路径设置到剪切板中
            setText(u"c:\\test.txt")
            # 查找页面上ID属性值为“file”的文件上传框,
            # 并点击调出选择文件上传框
            self.driver.find_element_by_id("file").click()
            time.sleep(2)
            # 模拟键盘按下ctrl + v组合键
            keyDown("ctrl")
            keyDown("v")
            # 模拟键盘释放Ctrl + v组合键
            keyUp("v")
            keyUp("ctrl")
            time.sleep(1)
            # 模拟键盘按下回车键
            keyDown("enter")
            # 模拟键盘释放回车键
            keyUp("enter")
            # 暂停查看上传的文件
            time.sleep(2)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Chrome浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_uploadFileBySendKeys(self):
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
            # 查找页面上ID属性值为“file”的文件上传框
            fileBox = self.driver.find_element_by_id("file")
            # 在文件上传框的路径框里输入要上传的文件路径“c:\\test.txt”
            fileBox.send_keys("/Users/ralphliu/Document/webdriver/geckodriver")
            # 暂停查看上传的文件
            time.sleep(4)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

