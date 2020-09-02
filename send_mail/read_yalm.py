#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 2:56 PM
# @Author  : congcong
# @Site    : 
# @File    : read_yalm.py
# @Software: PyCharm Community Edition
import yaml
import json

#f1=yaml.load('receiver.yalm')
#print(f1)

#file=open('receiver.yalm','r')
# for f in file:
#     print(yaml.load(f))
#     print('信息：'+f)
# file.close()

# with open('receiver.yalm','r') as file:
#     f2=yaml.load(file,Loader=yaml.FullLoader)
#     print(f2)

with open('data','r') as file:
    line=file.readline()
    user=line.split(' ')
    # print(file.readline())
    print(user)




