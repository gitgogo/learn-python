#coding=utf-8
from selenium import webdriver
# driver=Firefox(executable_path='/Users/ralphliu/Document/webdriver/geckodriver')
import unittest
import time
import chardet
# from selenium import webdriver
 
class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        
    def test_doubleClick(self):
        url = "file:///private/etc/apache2/web/test_doubleclick.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 获取页面输入元素
        inputBox = self.driver.find_element_by_id("inputBox")
        # 导入支持双击操作的模块
        from selenium.webdriver import ActionChains
        # 开始模拟鼠标双击操作
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()

        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        # self.driver.quit()
        pass

# if __name__ == '__main__':
#     unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_printSelectText(self):
        url = "file:///private/etc/apache2/web/test_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用name属性找到页面上name属性为“fruit”的下拉列表元素
        select = self.driver.find_element_by_name("fruit")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            print u"选项显示的文本：", option.text
            print u"选项值为：", option.get_attribute("value")
            option.click()
            time.sleep(1)
            if option.text==u'橘子':
                break

    def tearDown(self):
        # 退出IE浏览器
        # self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        #启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Chrome(executable_path = "/Users/ralphliu/Document/webdriver/chromedriver")
        
    def test_operateDropList(self):
        url = "file:///private/etc/apache2/web/test_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 导入Select模块
        from selenium.webdriver.support.ui import Select
        # 使用xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 打印默认选中项的文本
        print select_element.first_selected_option.text
        # 获取所有选择项的页面元素对象
        all_options = select_element.options
        # 打印选项总个数
        print len(all_options)
        '''
        is_enabled()：判断元素是否可操作
        is_selected()：判断元素是否被选中
        '''
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # 方法一：通过序号选择第二个元素，序号从0开始
            select_element.select_by_index(1)
            # 打印已选中项的文本
            print select_element.all_selected_options[0].text
            # assertEqual()方法断言当前选中的选项文本是否是“西瓜”
            self.assertEqual(select_element.all_selected_options[0].text, u"西瓜")
        time.sleep(2)
        # 方法二：通过选项的显示文本选择文本为“猕猴桃”选项
        select_element.select_by_visible_text("猕猴桃")
        # 断言已选中项的文本是否是“猕猴桃”
        self.assertEqual(select_element.all_selected_options[0].text, u"猕猴桃")
        time.sleep(2)
        # 方法三：通过选项的value属性值选择value=“shanzha”选项
        select_element.select_by_value("juzi")
        print select_element.all_selected_options[0].text
        self.assertEqual(select_element.all_selected_options[0].text, u"橘子")


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
        
    def test_checkSelectText(self):
        url = "file:///private/etc/apache2/web/test_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 导入Select模块
        from selenium.webdriver.support.ui import Select
        # 使用xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 获取所有选择项的页面元素对象
        actual_options = select_element.options
        # 声明一个list对象，存储下拉列表中所期望出现的文字内容
        expect_optionsList = [u"桃子",u"西瓜",u"橘子",u"猕猴桃",u"山楂",u"荔枝"]
        # 使用Python内置map()函数获取页面中下拉列表展示的选项内容组成的列表对象
        actual_optionsList = map(lambda option: option.text, actual_options)
        # 断言期望列表对象和实际列表对象是否完全一致
        self.assertListEqual(expect_optionsList, actual_optionsList)

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
        
    def test_operateMultipleOptionDropList(self):
        url = "file:///private/etc/apache2/web/test_input_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        from selenium.webdriver.common.keys import Keys
        # element.send_keys("some text")
        self.driver.find_element_by_id("select").clear()

        # 输入的同时按下箭头键
        self.driver.find_element_by_id("select").send_keys("c")
        time.sleep(2)
        self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        self.driver.find_element_by_id("select").send_keys(Keys.ENTER)
        time.sleep(2)

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
        
    def test_operateRadio(self):
        url = "file:///private/etc/apache2/web/test_radio.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用xpath定位获取value属性值为'berry'的input元素对象，也就是“草莓”选项
        berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
        # 点击选择“草莓”选项
        berryRadio.click()
        # 断言“草莓”复选框被成功选中
        self.assertTrue(berryRadio.is_selected(), u"草莓复选框未被选中！")
        if berryRadio.is_selected():
            # 如果“草莓”复选框被成功选中，重新选择“西瓜”选项
            watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelonRadio.click()
            # 选择“西瓜”选项以后，断言“草莓”选项处于未被选中状态
            self.assertFalse(berryRadio.is_selected())
        # 查找所有name属性值为“fruit”的单选框元素对象，并存放在radioList列表中
        radioList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        '''
        循环遍历radioList中的每个单选按钮，查找value属性值为“orange”的单选框，
        如果找到此单选框以后，发现未处于选中状态，则调用click方法选中该选项。
        '''
        for radio in radioList:
            if radio.get_attribute("value") == "orange":
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute("value"), "orange")


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
        
    def test_operateCheckBox(self):
        url = "file:///private/etc/apache2/web/test_checkbox.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用xpath定位获取value属性值为'berry'的input元素对象，也就是“草莓”选项
        berryCheckBox = self.driver.find_element_by_xpath("//input[@value='berry']")
        # 点击选择“草莓”选项
        berryCheckBox.click()
        # 断言“草莓”复选框被成功选中
        self.assertTrue(berryCheckBox.is_selected(), u"草莓复选框未被选中！")
        if berryCheckBox.is_selected():
            # 如果“草莓”复选框被成功选中，再次点击取消选中
            berryCheckBox.click()
            # 断言“草莓”复选框处于未选中状态
            self.assertFalse(berryCheckBox.is_selected())
        # 查找所有name属性值为“fruit”的复选框元素对象，并存放在checkBoxList列表中
        checkBoxList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        # 遍历遍历checkBoxList列表中的所有复选框元素，让全部复选框处于被选中状态
        for box in checkBoxList:
            if not box.is_selected():
                box.click()
        time.sleep(2)
        #取消选择
        for box in checkBoxList:
            if box.is_selected():
                box.click()
        time.sleep(3)

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
        
    def test_dragPageElement(self):
        url = "http://jqueryui.com/resources/demos/draggable/scroll.html"
        # 访问被测试网页
        self.driver.get(url)
        # 获取页面上第一个能拖拽的页面元素
        initialPosition = self.driver.find_element_by_id("draggable")
        # 获取页面上第二个能拖拽的页面元素
        targetPosition = self.driver.find_element_by_id("draggable2")
        # 获取页面上第三个能拖拽的页面元素
        dragElement = self.driver.find_element_by_id("draggable3")
        # 导入提供拖拽元素方法的模块ActionChains
        from selenium.webdriver import ActionChains
        import time
        '''
        创建一个新的ActionChains，将webdriver实例对象driver作为参数值传入
        然后通过WebDriver实例执行用户动作。
        '''
        action_chains = ActionChains(self.driver)
        # 将页面上第一个能被拖拽的元素拖拽到第二个元素位置
        action_chains.drag_and_drop(initialPosition, targetPosition).perform()
        # 将页面上第三个能拖拽的元素，向右下拖动10个像素，共拖动5次
        for i in xrange(5):
            action_chains.drag_and_drop_by_offset(dragElement, 10, 10).perform()
            time.sleep(2)

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
        
    def test_simulateASingleKeys(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页，焦点会自动定位到搜索输入框中
        self.driver.get(url)
        # 导入模拟按键模块Keys
        from selenium.webdriver.common.keys import Keys
        import time
        # 通过id获取搜索输入框的页面元素
        query = self.driver.find_element_by_id("query")
        # 通过WebDriver实例发送一个F12键
        query.send_keys(Keys.F12)
        time.sleep(3)
        # 再次通过WebDriver实例模拟发送一个F12键
        query.send_keys(Keys.F12)
        # 在搜索输入框中输入“selenium”
        query.send_keys("selenium")
        # 通过WebDriver实例模拟发送一个回车键，
        # 或者使用query.send_keys(Keys.RETURN)
        query.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()