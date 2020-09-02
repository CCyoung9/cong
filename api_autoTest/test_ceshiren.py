#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 2:56 PM
# @Author  : congcong
# @Site    : 
# @File    : test_ceshiren.py
# @Software: PyCharm Community Edition
import requests
import pytest
import yaml
import json

# print(open('/Users/miao/Desktop/github/cong/api_autoTest/term.yml','r').read())
# r=open('/Users/miao/Desktop/github/cong/api_autoTest/term.yml','r')
# print(r.read())
# #rr=json.load(r)

#@pytest.mark.parametrize('param',['java','python','jmeter'])
@pytest.mark.parametrize('param',yaml.load(open('/Users/miao/Desktop/github/cong/api_autoTest/term.yml','r')))
def test_ceshiren(param):

    url='https://ceshiren.com/search/query?term'
    headers = {"authority": "ceshiren.com", "x-requested-with": "XMLHttpRequest",
               "accept": "application/json, text/javascript, */*; q=0.01", "discourse-present": "true",
               "x-csrf-token": "undefined", "referer": "https://ceshiren.com/search?q=python",
               "accept-language": "zh-CN,zh;q=0.9",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
               "sec-fetch-site": "same-origin"}

    #pytest.xfail(reason="测试xfail功能")
    res=requests.get(url+param,headers)
    assert res.status_code==200