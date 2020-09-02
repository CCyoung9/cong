#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 1:34 PM
# @Author  : congcong
# @Site    : 
# @File    : test_family.py
# @Software: PyCharm Community Edition



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_family_t:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://10.69.101.178:8080/logout.do")
    def teardown(self):
        self.driver.close()

    def test_log_in(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://10.69.101.178:8080/logout.do")
        user=self.driver.find_element(By.id,"userId")
        user.clear()
        user.send_keys("admin")
        pass_word=self.driver.find_element(By.id,"pass")
        pass_word.clear()
        pass_word.send_keys("000000")
        button=self.driver.find_element(By.xpath,"/html/body/div[2]/div[1]/form/input[2]")
        button.click()
        time.sleep(20)
        assert 1==1

if __name__ == '__main__':
    f=test_family_t
    test_family_t.test_log_in(f)