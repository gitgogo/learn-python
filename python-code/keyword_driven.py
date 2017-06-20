#encoding=utf-8
from selenium import webdriver
import time
import logging, traceback
from selenium.common.exceptions import NoSuchElementException
import re

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %Y-%m-%d %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'e:/dataDriveRreport.log',
    # 打开日志文件的方式
    filemode = 'w'
)

driver=""
def browser(brower_name):
    global driver
    if brower_name.lower()=="ie":
        driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
    elif brower_name.lower()=="chrome":
        driver = webdriver.Chrome(executable_path = "e:\\chromedriver")
    else:
        driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
def visit(url):
    global driver
    driver.get(url)

def input(xpath,word):
    global driver 
    driver.find_element_by_xpath(xpath).send_keys(word)  

def click(xpath):
    global driver
    driver.find_element_by_xpath(xpath).click()

def sleep(seconds):
    time.sleep(float(seconds))

def assert_word(word):
    global driver
    assert True==(word in driver.page_source)

def close():
    global driver
    driver.quit()


if __name__=="__main__":
    result=[]
    elapse_time=-1
    with open("testdata.txt",'r') as fp:
        for testdata in fp.readlines()[1:]:
            search_word=testdata.split("||")[0].decode("gbk")
            expected_word=testdata.split("||")[1].decode("gbk")
            with open("e:\\b.txt",'r') as fp:
                for line in fp:
                    step=line.split("||")
                    case_description=step[0]
                    #print step
                    if len(step)==2:
                        step=step[1].strip()+"()"
                    elif len(step)==3:
                        if re.search("\${(.*)}",step[2].strip()):
                            if re.search("\${(.*)}",step[2].strip()).group(1)=="expected_word":
                                step=step[1].strip()+"(u\""+expected_word.strip()+"\")"
                                #print re.search("\${(.*)}",step[3].strip()).group(1)
                        else:
                            step=step[1].strip()+"(\""+step[2].strip()+"\")"
                        print step
                    elif len(step)==4:
                        if re.search("\${(.*)}",step[3].strip()):
                            if re.search("\${(.*)}",step[3].strip()).group(1)=="search_word":

                                step=step[1].strip()+"(\""+step[2].strip()+"\",u\""+search_word+"\")"
                                #print re.search("\${(.*)}",step[3].strip()).group(1) 
                        else:
                            step=step[1].strip()+"(\""+step[2].strip()+"\",\""+step[3].strip()+"\")"
                        print step
                    try:
                        time1=time.time()
                        exec(step)
                        time2=time.time()
                        elapse_time=time2-time1
                    except NoSuchElementException, e:
                        logging.error(u"查找的页面元素不存在，异常堆栈信息："\
                          + str(traceback.format_exc()))
                        result.append(line.strip()+u"||执行耗时：".encode("gbk")+str(elapse_time).encode("gbk")+u"||失败\n".encode("gbk"))
                    except AssertionError, e:
                        logging.info(u"断言错误")
                        result.append(line.strip()+u"||执行耗时：".encode("gbk")+str(elapse_time).encode("gbk")+u"||失败\n".encode("gbk"))
                    except Exception, e:
                        logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
                        result.append(line.strip()+u"||执行耗时：".encode("gbk")+str(elapse_time).encode("gbk")+u"||失败\n".encode("gbk"))
                    else:
                        print u"测试用例描述：",case_description
                        logging.info(u"当前测试步骤：%s，测试执行成功" %case_description.strip().decode("gbk"))
                        result.append(line.strip()+u"||执行耗时：".encode("gbk")+str(elapse_time).encode("gbk")+u"||成功\n".encode("gbk"))

            with open("e:\\c.txt",'w') as fp:
                fp.writelines(result)