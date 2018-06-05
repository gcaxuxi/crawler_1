## 一.中医组方之爬虫
----
### 1. Objective：抓取药智网（ https://www.yaozh.com/login ）中的药物数据集
### 2. step：
  1) 环境：python3.5 + selenium
  
  2) 操作：get_page_v2.py包含抓取网页的主函数。因为目标网站多次抓取后会断连，所以在main.py里采用多次重启程序的操作。
