from selenium import webdriver
import time
from QQ_Send_Email.QQ_Login import Login
from QQ_Send_Email.Baseclass import Conmon
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        '''
            初始化浏览器对象
        '''
        # 设置浏览器全屏
        self.driver.maximize_window()

    def test(self):
        # 元素定位，写入内容
        con = Conmon(self.driver)
        con.input_date('id', 'kw', 'qq邮箱')
        con.click_element('id', 'su')

        # 断言
        # self.assertEqual(self.driver.find_element_by_xpath('//*[@id="su"]').get_attribute("value"), u'百度', "百度失败")

        time.sleep(1)

        # 点击qq邮箱连接
        con.click_element('xpath', '//*[@id="1"]/h3/a[1]')
        time.sleep(1)

        # 切换窗口
        con.window(-1)

        # 跳到qq邮箱登录页面
        con.frame('id', 'login_frame')

        # 登录qq邮箱
        Login(self.driver).login('2263890318', '187645903friend')

        time.sleep(5)

        # 点击写信
        con.click_element('id', 'composebtn')

        time.sleep(3)

        # 跳到写信页面
        con.frame('id', 'mainFrame')
        # 输入收件人
        con.input_date('xpath', '//*[@id="toAreaCtrl"]/div[2]/input', '3162099337@qq.com')
        # 输入主题
        con.input_date('id', 'subject', '你好')
        # 添加图片
        con.input_date('xpath', '//*[@id="QMEditorToolBarPlusArea"]/span[1]/a/span/input', 'C:\\c.jpg')

        time.sleep(5)

        # 切换到正文页面
        con.frame('a', con.locate_element('class_name', 'qmEditorIfrmEditArea'))
        # 输入内容
        con.input_date('tag_name', 'body', 'hello world!')
        time.sleep(10)

        # 返回前一页面
        con.parent()
        con.frame('id', 'mainFrame')

        # 点击发送
        con.click_element('xpath', '//*[@id="toolbar"]/div/a[1]')
        time.sleep(3)

    # 关闭窗口
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()