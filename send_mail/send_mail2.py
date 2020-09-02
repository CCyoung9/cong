#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 10:42 AM
# @Author  : congcong
# @Site    : 
# @File    : send_mail2.py
# @Software: PyCharm Community Edition
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

class send_mail:
    def __init__(self,sender,psw,content,subject):
        self.sender = sender
        self.psw = psw
        self.content = content
        self.subject=subject
        #print(sender,psw,content,subject)
    def send_mail_methd(self):
        receivers = []
        to_user=[]

        with open('data','r') as file:
            for line in file:
                user = line.split(' ')
                receivers.append(user[0])
                to_user.append([user[1],user[0]])
        print(self.sender)

        message=MIMEText('测试邮件正文vvvv','plain','utf-8')
        print(message)
        message['From']=self.sender
        message['To']=formataddr(receivers,'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        #message['Subject']=self.subject
        #print('sssss'+str(message))
        try:
            smtpObj=smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtpObj.login(self.sender,self.psw)
            smtpObj.sendmail(self.sender, receivers, str(message))

            print('发送邮件成功。。')
        except smtplib.SMTPException:
            print('ERRO:无法发送邮件。。')

if __name__ == '__main__':
    mail=send_mail('865088904@qq.com','rqhkjgdorcacbecf','邮件正文。。','邮件标题')
    mail.send_mail_methd()



