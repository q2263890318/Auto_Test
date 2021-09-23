from selenium import webdriver
import time
from CCZ.QQ_Send_Email.QQ_Login import Login

class Conmon(object):

    def __init__(self, brower):
        # self.driver = driver
        if brower == 'Chrome':
            self.driver = webdriver.Chrome()
        elif brower == 'Firefox':
            self.driver = webdriver.Firefox()
        elif brower == 'PhantomJS':
            self.driver = webdriver.PhantomJS()
        self.driver.maximize_window()

    def delay(self):
        '''
            延迟等待
        '''
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        '''
            访问网站
        '''
        self.driver.get(url)
        self.delay()
        print('访问:%s成功'%url)

    def locate_element(self, locate_type, value):
        '''
            通过参数定位一个元素，并返回
        '''
        el = None
        # el = self.driver.find_element(locate_type, value)
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class_name':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'tag_name':
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == 'link_text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'partial_link_name':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)

        # 返回定位到的元素
        if el is not None:
            return el

    def click_element(self, locate_type, value):
        '''
            直接点击某一元素
        '''
        el = self.locate_element(locate_type, value)
        el.click()

    def input_date(self, locate_type, value, data):
        '''
            定位到输入框，并且输入数据
        '''
        el = self.locate_element(locate_type, value)
        el.send_keys(data)

    def frame(self, locate_type, value):
        '''
            切换表单
        '''
        if locate_type == 'id':
            self.driver.switch_to.frame(value)
        elif locate_type == 'name':
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(value)

    # 返回表单最外层
    def parent(self):
        self.driver.switch_to.default_content()

    def window(self, num):
        '''
            切换窗口
        '''
        self.driver.switch_to.window(self.driver.window_handles[num])

    # QQ登录
    def QQlogin(self, username, pwd):
        Login(self.driver).login(username, pwd)

    # 浏览器后退
    def back(self):
        self.driver.back()
        self.delay()
        print('后退到:%s'%self.driver.current_url)

    # 浏览器前进
    def forward(self):
        self.driver.forward()
        self.delay()
        print('前进到:%s' % self.driver.current_url)

    # 关闭窗口
    def __del__(self):
        time.sleep(5)
        self.driver.quit()

