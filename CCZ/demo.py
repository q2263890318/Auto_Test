# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.cnblogs.com/yoyoketang/")
# 用一个参数flag判断元素是否存在
def is_element_exist():
    try:
        driver.find_element_by_id("blog_nav_sitehome11")
        return True
    except NoSuchElementException as msg:
        print (u"未找到元素：%s"%msg)
        return False
    except Exception as msg:
        print (u"其它异常：%s"%msg)
        return False
print (is_element_exist())
