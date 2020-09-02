#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 下午2:02
# @Author  : congcong
# @Site    : 
# @File    : test_pytest_param.py
# @Software: PyCharm Community Edition

import pytest


@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),("6*9",54)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected


if __name__ == '__main__':
    pytest.main(["-s", "test_pytest_param.py"])