import os
import time

while 1:
    now_time = time.strftime("%H:%M")
    if now_time == '15:12' or now_time == '17:03':
        os.chdir(r'D:\Python+Selenium\CCZ\QQ_Send_Email')
        os.system('Send_email.py')
        print (u'运行完成退出!')
        break
    else:
        time.sleep(3)
        print(now_time)