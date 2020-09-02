#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").sendkey("杨聪聪")
driver.find_element_by_id("su").click
x = driver.find_elements_by_class_name("c-showurl").text
for i in range(x):
    print(i)
