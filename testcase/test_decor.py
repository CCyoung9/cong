#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 下午5:08
# @Author  : congcong
# @Site    : 
# @File    : test_decor.py
# @Software: PyCharm Community Edition


def before(func):
    def new_now():
        print("setup")
        print("again")
        func()

    return new_now

@before
def now():
    print("20192")

def test_demo():
    now()