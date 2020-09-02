#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 5:23 PM
# @Author  : congcong
# @Site    : 
# @File    : choujiang.py
# @Software: PyCharm Community Edition

#选择恐惧症，帮选助手 ，100以内选多个
import random

class select:
    def __init__(self,count_all=2,count_slct=1):
        self.count_all=count_all
        self.count_slct=count_slct
    def to_select(self):
        if self.count_slct>self.count_all:
            return "数据错误"
        if self.count_all>100:
            return "总数超限"
        res=[]

        for i in range(self.count_slct):
            randoma=int(random.random()*100)
            #print(randoma)
            selected=randoma%self.count_all
            #print("第",i,"轮，选择",selected)
            if selected not in res:
                res.append(selected)
        return res

if __name__ == '__main__':
    s=select(200,6)
    print(s.to_select()   )
