#!/usr/bin/python 

# -*- coding: utf-8 -*- 

# encoding: utf-8 

import os 
from get_page_v2 import add
from get_page_v2 import end
  

if __name__ == '__main__': 
    i = 1
    #先执行一次，建立data2文件夹
    cmd = 'python get_page_v2.py'    
    os.system(cmd)
    while i < 60:
#   while True:
        flag = os.listdir(os.path.join(os.path.abspath('.'), add))[-1]
        id_num = os.path.splitext(flag)[0]
        if end == int(id_num) + 1:
            print('爬取完毕！')
            break
        else:
            i += 1 
            os.system(cmd)
