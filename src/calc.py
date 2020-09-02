#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 下午4:03
# @Author  : congcong
# @Site    : 
# @File    : calc.py
# @Software: PyCharm Community Edition

class Calc:
    def add(self, a, b):
        return a+b
    def div(self , a, b):
        return  a/b
    def above(self, a, b):
        if (a>b):
            return True
        else:
            return False