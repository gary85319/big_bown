import csv
import yt_scrach
import os
import random
次數=1000
import tqdm

kkey=['荒野料峭','阿滴','佑哥','嘿兄弟','dream','阿神','小光']


for n in tqdm.tqdm(range(0,次數)):
    a=yt_scrach.yt_find(random.choice(kkey))
   

        
    with open('youtube.csv','r+',encoding='utf-8',errors='ignore',newline='')as f:
        ccc=csv.writer(f)
        f.seek(0)
        da=f.read()
        
        if '觀看次數,幾天前,訂閱次數' not in da:

            ccc.writerow(['觀看次數','幾天前','訂閱次數'])
        ccc.writerows(a)


  