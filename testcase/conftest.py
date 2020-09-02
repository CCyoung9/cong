#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 12:58 PM
# @Author  : congcong
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm Community Edition

import pytest
import logging
import requests

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture()
def topics():
    url="https://testerhome.com/api/v3/topics.json?limit=2"
    yield requests.get(url).json()
    logging.info("after yield")