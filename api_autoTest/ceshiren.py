#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 9:41 AM
# @Author  : congcong
# @Site    : 
# @File    : ceshiren.py
# @Software: PyCharm Community Edition

import requests
import urllib3
import json
import yaml

class AutoTest:
    def __init__(self,url):
        self.url=url


    def query(self):
        headers = {"authority": "ceshiren.com", "x-requested-with": "XMLHttpRequest",
                   "accept": "application/json, text/javascript, */*; q=0.01", "discourse-present": "true",
                   "x-csrf-token": "undefined", "referer": "https://ceshiren.com/search?q=python",
                   "accept-language": "zh-CN,zh;q=0.9",
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                   "sec-fetch-site": "same-origin"}

        #res=requests.get(self.url,headers=headers)

        # if res.status_code==200:
        #     print("接口请求成功！")

        f=open('term.yml','r')
        terms=yaml.load(f)
        for term in terms:
            print(self.url+term)
            res=requests.get(self.url+term,headers=headers)
            print(res.content.decode())
            json_res=json.loads(res.content)
            print(json_res)

        # print(r)
        #
        # print(res.json())
        # print(res.json()['posts'])




if __name__ == '__main__':
    test=AutoTest('https://ceshiren.com/search/query?term=')
    test.query()
