#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午7:56
# @Author  : congcong
# @Site    : 
# @File    : unitest.py
# @Software: PyCharm Community Edition

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

def fun(*args):
    print (args)

if __name__ == '__main__':
    unittest.main
    fun("hello")