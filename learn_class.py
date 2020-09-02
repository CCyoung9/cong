#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 下午3:30
# @Author  : congcong
# @Site    : 
# @File    : learn_class.py
# @Software: PyCharm Community Edition
import sys

class A:
    t=1
    def m_a(self):
        print "A.m_a"
    @classmethod
    def c_a(cls):
        print ("cls_t")
        print (cls.t)
class B:
    def m_b(self):
        print ("B.m_b")

print (A)
print (B)
a=A()
a.m_a()

a1=A()
a2=A()
a1.t=2
print (a1.t)
print (a2.t)

a2.t=3
print (a.t)
print (a1.t)
print (a2.t)

A.t=4

print (a.t)
print (a1.t)
print (a2.t)

print (A.c_a())

print (sys.path)