from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib import parse

import time
d=wb.Chrome()



def scrach(k,count):
    rwl=[]
    kkk=parse.quote(k)
    url=f'https://shopee.tw/search?keyword={kkk}&is_from_login=false'
    
    d.get(url)
    
    for n in range(0,60):
        print(f'還有{60-n}秒')
    d.implicitly_wait(10)
    llist=[]
    def mk_item():
       
        items=d.find_elements('xpath','//div[@class="ie3A+n bM+7UW Cve6sh"]')
        items_price=d.find_elements(By.XPATH,'//span[@class="ZEgDH9"]')
        item_url=d.find_elements(By.XPATH,'//a[@data-sqe="link"]')
        d.implicitly_wait(10)
        for n, f, u in zip(items, items_price, item_url):
            j = n.text
            t = f.text
            p = u.get_attribute('href')
            h=u.text
            llist.append([j,t,p,h])
            
            
        nextt=d.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/button[4]')
        nextt.click()
        return llist
    
    for b in range(0,count):
        f=mk_item()
        rwl.append(f)
    return rwl
s=scrach('書',50)
print(s)