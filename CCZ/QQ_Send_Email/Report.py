import HTMLTestRunnerCN
import unittest

Testcase_dir = 'D:\Python+Selenium\CCZ\QQ_Send_Email'
dis = unittest.defaultTestLoader.discover(Testcase_dir, 'Send_email.py')
# 定义报告存放路径
filename = "D:\Python+Selenium\CCZ\QQ_Send_Email\\result1.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
fp.close()