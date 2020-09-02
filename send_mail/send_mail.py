#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 4:11 PM
# @Author  : congcong
# @Site    : 
# @File    : send_mail.py
# @Software: PyCharm Community Edition

import smtplib
from email.mime.text import MIMEText
from email.header import Header



sender = '865088904@qq.com'
psw='rqhkjgdorcacbecf'
receivers = ['yangcongcongccc@163.com','95536264@qq.com']

message = MIMEText('Python 邮件发送测试..邮件正文', 'plain', 'utf-8')

message['From']=sender
message['To']=receivers[0]
print(message['From'],message['To'])

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    #smtpObj = smtplib.SMTP('SMTP.163.com')
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login(sender, psw)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")