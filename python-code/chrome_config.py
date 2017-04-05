#encoding=utf-8
from selenium import webdriver
# 导入Options类
from selenium.webdriver.chrome.options import Options
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建Chrome浏览器的一个Options实例对象
        chrome_options = Options()
        # 向Options实例中添加禁用扩展插件的设置参数项
        chrome_options.add_argument("--disable-extensions")
        # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # 添加浏览器最大化的设置参数项，已启动就最大化
        chrome_options.add_argument('--start-maximized')
        # 启动带有自定义设置的Chrome浏览器
        self.driver=webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_extendedAttributesChrome(self):
        # 访问百度首页
        self.driver.get("http://www.baidu.com")
        # 暂停3秒，人工查看上面设置是否已生效
        time.sleep(3)
        # 找到页面的搜索输入框，输入“光荣之路自动化测试”
        self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#config
#encoding=utf-8
from selenium import webdriver
# 导入Options类
from selenium.webdriver.chrome.options import Options
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建Chrome浏览器的一个Options实例对象
        chrome_options = Options()
        # 设置Chrome浏览器禁用PDF和Flash插件,把图片也关掉了。
        profile = {"plugins.plugins_disabled": ['Chrome PDF Viewer'],
                   "plugins.plugins_disabled": ['Adobe Flash Player'],
                   "profile.managed_default_content_settings.images":2}


        chrome_options.add_experimental_option("prefs", profile)
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs", profile)
        # 向Options实例中添加禁用扩展插件的设置参数项
        chrome_options.add_argument("--disable-extensions")
        # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # 添加浏览器最大化的设置参数项，启动同时最大化窗口
        chrome_options.add_argument('--start-maximized')
        # 启动带有自定义设置的Chrome浏览器
        self.driver=webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")

    def test_forbidPdfFlashChrome(self):
        # 访问爱奇艺首页
        self.driver.get("http://www.iqiyi.com")
        # 等待50秒，期间可以看到页面由于禁用了Flash插件，
        # 导致需要Flash支持的内容无法正常展示
        time.sleep(10)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#safe mode
#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.INTERNETEXPLORER
        # 将忽略IE保护模式的参数设置为True
        caps['ignoreProtectedModeSettings'] = True
        # 启动带有自定义设置的IE浏览器
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer", capabilities=caps)

    def test_forbidPdfFlashChrome(self):
        # 访问百度首页
        self.driver.get("http://www.baidu.com")
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#firebug
#encoding=utf-8
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.keys import Keys

class TestDemo(unittest.TestCase):

    def test_openFireBug(self):
        # 找到自定义配置文件路径
        profilePath = r"C:\Users\wuxiaohua\AppData\Roaming\Mozilla\Firefox\Profiles\g6m1cswj.default"
        # 将自定义配置文件加载到FirefoxProfile实例中
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(profilePath)
        # 将添加了新配置文件的Firefox浏览器首页设为百度主页，
        # 以便启动浏览器后将直接跳转到百度首页
        profile.set_preference("browser.startup.homepage", "http://www.baidu.com")
        # 设置启动浏览器的同时主页不为空白页
        profile.set_preference("browser.startup.page", 1)
        # 自动打开firebug
        profile.set_preference("extensions.firebug.allPagesActivation", "on")
        # 启用firebug网络面板功能
        profile.set_preference("extensions.firebug.net.enableSites", True)
        # 启用firebug Cookies面板功能
        profile.set_preference("extensions.firebug.cookies.enableSites", True)
        # 启动自定义配置信息的Firefox浏览器
        driver = webdriver.Firefox(executable_path="e:\\geckodriver", firefox_profile = profile)
        # 等待浏览器启动完成
        time.sleep(3)
        # 找到百度主页中的搜索输入框页面元素
        input = driver.find_element_by_id("kw")
        # 在搜索输入框中输入“selenium”
        input.send_keys("selenium")
        # input.send_keys(Keys.F12)
        # 等待30秒，人工确认上面一系列设置是否生效
        time.sleep(30)
        driver.quit()

if __name__ == '__main__':
    unittest.main()