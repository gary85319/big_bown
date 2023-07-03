from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

import requests
def cm(tett):
    tet = re.search(r'\d+\.?\d*', tett)
    
    if '萬' in tett:
        tet = float(tet.group()) * 10000
    elif '億' in tett:
        tet = float(tet.group()) * 100000000
    else:
        tet = float(tet.group())
    
    return tet


def yt_find(search_query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    d = webdriver.Chrome(options=chrome_options)
    d.implicitly_wait(10)
    d.get(f"https://www.youtube.com/results?search_query={search_query}")
    d.implicitly_wait(10)
    url_list = d.find_elements(By.XPATH, '//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')

    see_list = d.find_elements(By.XPATH, '//span[@class="inline-metadata-item style-scope ytd-video-meta-block"]')
    
    yt_view_count_=d.find_element(By.XPATH,'/html[1]/body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-channel-renderer[1]/div[1]/div[2]/a[1]/div[1]/div[1]/span[3]')
    print('url:', len(url_list))

    print('see:', len(see_list))

    try:
         yt_view_count_=d.find_element(By.XPATH,'/html[1]/body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-channel-renderer[1]/div[1]/div[2]/a[1]/div[1]/div[1]/span[3]')
    except:
        print('錯誤:不是一位youtube!!!!!')
    new = []
    yt_view_count=yt_view_count_.text
    new_tuples = [see_list[i:i+2] for i in range(0, len(see_list), 2)]
    for url, see in zip(url_list, new_tuples):

        title = url.get_attribute('title')
        cleaned_title = (title.replace('"', ''))  # 去除双引号
        cll = cleaned_title.replace(",", "")  # 移除"豇豆號"
            
        see_text = see[0].text
        day = see[1].text
        try:
            day = see[1].text
        except:
            print('錯誤:機數位，已自動修補')
            day = see[0]
        numbers = re.findall(r'\d+\.?\d*', see_text)
        dday = re.findall(r'\d+\.?\d*', day)
        watched_count = float(numbers[0]) if numbers else 0
        ddday = float(dday[0]) if day else 0

        if '萬' in see_text:
            watched_count = watched_count * 10000
        if '年' in day:
            dday=dday*360
        if '月' in day:
            dday=dday*30
        elif '周'  in day:
            dday=dday*7
        yt_v_iew_count=re.findall(r'\d+\.?\d*', yt_view_count)
        new.append(( watched_count, ddday,cm(yt_view_count)))
    return new


