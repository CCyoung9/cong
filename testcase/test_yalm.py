#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 下午7:42
# @Author  : congcong
# @Site    : 
# @File    : test_yalm.py
# @Software: PyCharm Community Edition
import json
import os
import yaml
#
# def hhh():
#     with open("calc.json",'r') as f:
#         print(f.read())
#
#         # print(json.load(f))
#
#     a=open("calc.json")
#     b=json.load(a)
#     print(b)
#     a.close()
#     print(json.load(open("calc.json")))
#
#     # print(a.read())
#
# if __name__ == '__main__':
#     hhh()



def test_json():
    #d=open("13211.json",mode="x")
    f=open("/Users/miao/Desktop/github/cong/testcase/calc.json")
    print(f.read(),)
    print(os.path.abspath(os.path.dirname(__file__)))

def test_yalm():
    print('哈哈哈哈' + os.getcwd())
    print(yaml.load(open("/Users/miao/Desktop/github/cong/testcase/calc2.yaml")))




