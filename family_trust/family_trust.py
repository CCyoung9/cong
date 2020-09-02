#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 11:17 AM
# @Author  : congcong
# @Site    : 
# @File    : family_trust.py
# @Software: PyCharm Community Edition

from time import sleep

import selenium
from selenium import  webdriver
import logging

class testSlenium:

    def setup(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://10.69.101.178:8080/logout.do")

    def teardown(self):
        self.browser.close()


    def test_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://10.69.101.178:8080/logout.do")

        #assert "百度" in self.browser.title
        #ele=browser.find_element_by_name("wd")
        ele=self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/form/div/div[1]/div/input")
        ele.clear()
        ele.send_keys("admin")
        pw=self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/form/div/div[2]/div/input")
        pw.clear()
        pw.send_keys("000000")
        butn=self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/form/input[2]")
        butn.click()






        #self.browser.find_element(By.XPATH,)


        #ele.send_keys(Keys.RETURN)
        sleep(20)
        assert "No results found." not in self.browser.page_source

if __name__ == '__main__':
    s=testSlenium
    testSlenium.test_browser(s)

