from CCZ.PO_Modle.PO import BaiduPase
# from ddt import ddt, data
import unittest
import time

class Test(unittest.TestCase):

    def test01(self):
        web = BaiduPase('Chrome')
        web.open_url('https://www.baidu.com')
        # web.search('QQ邮箱')
        web.get_text('QQ邮箱')
        web.click_button()
        time.sleep(5)

if __name__ == '__main__':
   unittest.main()