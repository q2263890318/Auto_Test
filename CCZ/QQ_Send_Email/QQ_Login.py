
class Login():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        self.driver.find_element_by_id('u').send_keys(username)
        self.driver.find_element_by_id('p').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        # time.sleep(3)




