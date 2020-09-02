#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 上午10:50
# @Author  : congcong
# @Site    : 
# @File    : tutrial.py
# @Software: PyCharm Community Edition

def fun(*args):
    print args




a=[1,2,3]
#print ("dir",dir(a))

d={"a":1,"b":2}
for k,v in d.items():
    print ("key:" + k + " value:"+ str(v))



if __name__ == '__main__':
    fun("hello",)