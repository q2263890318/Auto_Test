from CCZ.PO_Modle.BasePase import BasePase

class BaiduPase(BasePase):

    # 定位元素，页面操作
    def get_text(self, value):
        # ele = self.locate_element('id', 'kw')
        # return ele
        self.input_date('id', 'kw', value)

    def click_button(self):
        # ele = self.locate_element('id', 'su')
        # return ele
        self.click_element('id', 'su')

    # 页面操作
    # def search(self, value):
    #     self.get_text().send_keys(value)
    #     self.click_button().click()