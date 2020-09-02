#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 3:53 PM
# @Author  : congcong
# @Site    : 
# @File    : study_selenium.py
# @Software: PyCharm Community Edition
from time import sleep

import selenium
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import  WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class testSlenium:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def teardown(self):
        self.driver.close()


    def test_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

        assert "百度" in self.driver.title
        #ele=browser.find_element_by_name("wd")
        ele=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input[@id='kw']")
        ele.clear()
        ele.send_keys("新纽")
        ele.send_keys(Keys.ENTER)

        #butten=self.driver.find_element_by_xpath("//*[@id='su']")
        xinniu=self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/h3/a")
        xinniu.click()





        #self.browser.find_element(By.XPATH,)


        #ele.send_keys(Keys.RETURN)
        sleep(20)
        assert "No results found." not in self.browser.page_source

    def xinniu(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.xnewtech.com/")
        ele=self.driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/ul/li[6]/a")
        
        ele2=self.driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/ul/li[6]/ul/li[1]/a")
        ele2.click()



if __name__ == '__main__':
    s=testSlenium
    testSlenium.xinniu(s)



