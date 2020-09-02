#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 下午1:33
# @Author  : congcong
# @Site    : 
# @File    : test_fixture.py
# @Software: PyCharm Community Edition

import pytest
import logging

import requests
def test_1():
    json=requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
    print(json)
    assert json != None

def test_2():
    json=requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
    assert len(json["topics"])==2

