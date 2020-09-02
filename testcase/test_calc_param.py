#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 下午4:07
# @Author  : congcong
# @Site    : ${SITE}
# @File    : test_calc.py
from unittest import TestCase
from src.calc import Calc
#from ddt import ddt,data,file_data,unpack
import pytest
import json
import yaml

# @Software: PyCharm Community Edition

class TestCalc():

    def setup(self):
        self.calc=Calc()
    #print(json.load(open("calc.json")))
    @pytest.mark.parametrize(" a, b, c",yaml.load(open("/Users/miao/Desktop/github/cong/testcase/calc2.yaml")))
    def test_add(self,a,b,c):
        print(a,b,c)
        #self.fail()
       # fail calc=Calc()
       #  result=calc.add(a,b)
        #assert result==2
        assert self.calc.add(a,b)==c
        #self.assertEqual(self.calc.add(a,b),c)

    #
    # @file_data("calc.yaml")
    # def test_div(self , a,b,c):
    #     calc=Calc()
    #     result=calc(a,b)
    #     self.assertEqual(result,c)

    def test_above(self):
        calc=Calc()
        result=calc.above(1,1)
        self.assertFalse(result)

        result=calc.above(2,1)
        self.assertTrue(result)

        result=calc.above(1,2)
        self.assertFalse(result)

        result=calc.above(-1,-2)
        self.assertTrue(result)

        result=calc.above(3.2,2.2)
        self.assertTrue(result)

        result=calc.above(2.2,3.2)
        self.assertFalse(result)
