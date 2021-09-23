from selenium import webdriver
import time
import xlrd
from CCZ.QQ_Send_Email.Baseclass import Conmon


# driver = webdriver.Chrome()
# 窗口最大化
# driver.maximize_window()
#读取文件
data = xlrd.open_workbook("E:\pycharm\图片爬虫\CCZ\Data_Leave\Data\\data.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for j in range(2):
    for i in range(j,table.nrows):
        # 读取excel第一行
        list = table.row_values(i)
        break
    print(list)
    time.sleep(3)
    #通过索引在excel表中获取百度URL
    con = Conmon('Chrome')
    con.open_url(list[0])

    time.sleep(3)
    #通过索引在excel表中获取百度输入框元素并输入要搜索的字段
    con.input_date(list[1], list[2], list[4])
    # driver.find_element_by_id(list[2]).send_keys(list[4])
    time.sleep(3)
    #通过索引在excel表中获取百度点击“百度一下”元素并点击
    con.click_element(list[5], list[7])
    # driver.find_element_by_id(list[7]).click()
    time.sleep(3)
# list=[]
# for i in range (1,table.nrows):
#     # 读取excel第二行
#     list = table.row_values(i)
#     break
# print(list)
# #跳转到“百度首页”
# driver.find_element_by_class_name(list[0]).click()
# time.sleep(3)
