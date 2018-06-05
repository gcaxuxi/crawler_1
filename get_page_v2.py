import time
import re
import random
from selenium import webdriver
import os
#登录获取并保持cookies
def login(username, password):
    url = 'https://www.yaozh.com/login'

    browser = webdriver.PhantomJS()
    # driver = webdriver.Firefox()
    browser.get(url)
    # print driver.title
    name_input = browser.find_element_by_id('username')  # 找到用户名的框框
    pass_input = browser.find_element_by_id('pwd')  # 找到输入密码的框框
    login_button = browser.find_element_by_id('button')  # 找到登录按钮

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    time.sleep(0.2)
    login_button.click()            # 点击登录
    time.sleep(1)
    # time.sleep(0.2)
    browser.get('https://db.yaozh.com/')
    browser.get('https://db.yaozh.com/zhongyaocai')
    return browser
#爬取页面




def spider(browser,url = 'https://db.yaozh.com/fangji/', start_num = 10002000, end_num = 10003000):
    i = 1
    try:
        for i in range(start_num, end_num):
            while True:
                #time.sleep(int(random.uniform(5, 15)))
                print(i)
                browser.get(url + str(i)+'.html')
                if ('<title>跳转提示</title>' in browser.page_source) or('暂无权限' in browser.page_source) or('<body onload="challenge();">' in browser.page_source):
                    print("错误！")
                    continue
                f = open(os.path.join(os.path.abspath('.'),add) +'\\' + str(i)+'.txt','a',encoding='utf-8')
                f.write(browser.page_source)
                f.close()
                break
        print(type(browser.page_source))
    except Exception as e:
        print(e)        
    
def mkdir_if_not_exist(path):
    if not os.path.exists(os.path.join(os.path.abspath('.'),path)):
        os.mkdir(os.path.join(os.path.abspath('.'),path))

add = 'data_2'  
end = 10003000
if __name__ == "__main__":
    user = "xuxi123"
    pw = "xuxi123"
    #url = 'https://db.yaozh.com/fangji/'
    browser = login(user, pw)
    mkdir_if_not_exist(add)
    
    if os.listdir(os.path.join(os.path.abspath('.'),add)) == []:
        spider(browser)
        
    else:
        flag = os.listdir(os.path.join(os.path.abspath('.'),add))[-1] #the address your file saved 
        id_num = os.path.splitext(flag)[0]
        spider(browser, start_num = int(id_num)+1)