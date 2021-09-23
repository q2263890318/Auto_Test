import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 发送邮箱
sender = '443887994@qq.com'
port=465
# 接收邮箱
receiver = '1427157647@qq.com'
# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/授权码
username = "443887994@qq.com"
password = ""
# 邮件类型，获取各种附件需要用到
msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = '自动化测试报告'
#构造附件
att = MIMEText(open('D:\Python+Selenium\CCZ\QQ_Send_Email\\result.html', 'rb').read(), 'base64',
'utf-8')
# 在响应类型为application/octet- stream情况下使用了这个头信息的话，那就意味着不直接显示内容，而是弹出一个”文件下载”的对话框
att["Content-Type"] = 'application/octet-stream'
# Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
att["Content-Disposition"] = 'attachment; filename="result.html"'
# 读取附件
msgRoot.attach(att)
# 开启发信服务
smtp = smtplib.SMTP_SSL(smtpserver,port)
# 发件人邮箱账号、邮箱授权码
smtp.login(username, password)
# msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str
smtp.sendmail(sender, receiver,msgRoot.as_string())
# 发件人邮箱中的SMTP服务器
smtp.connect('smtp.qq.com')
# 关闭服务器
smtp.quit()