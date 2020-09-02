#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 上午10:58
# @Author  : congcong
# @Site    : 
# @File    : test_pytest_2.py
# @Software: PyCharm Community Edition

import pytest
import logging



class TestPytestObject:
    logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def setup_class(cls):
        logging.info("setup_class")
    def setup_method(self):
        logging.info("setup")

    @pytest.mark.run(order=2)
    def test_two(self):
        assert 1==2

    @pytest.mark.run(order=1)
    def test_one(self):
        assert True==False

    def teardown_method(self):
        logging.info("teardown")

    @classmethod
    def tear_down(cls):
        logging.info("teardown_class")