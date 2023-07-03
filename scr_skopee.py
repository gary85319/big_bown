import re
import requests
dat=requests.get(r'https://shopee.tw/%E5%8F%AF%E9%80%9A%E8%A9%B1-%E7%A3%81%E5%90%B8%E5%85%85%E9%9B%BB-%E9%9B%99%E8%80%B3-%E7%84%A1%E7%B7%9A%E8%97%8D%E7%89%99%E8%80%B3%E6%A9%9F-%E8%97%8D%E7%89%99%E8%80%B3%E6%A9%9F-%E8%80%B3%E6%A9%9F-%E8%80%B3%E9%BA%A5-%E7%84%A1%E7%B7%9A%E8%80%B3%E6%A9%9F-%E9%81%8B%E5%8B%95%E8%80%B3%E6%A9%9F-%E8%97%8D%E8%8A%BD%E8%80%B3%E6%A9%9F-%E5%AE%89%E5%8D%93-%E8%98%8B%E6%9E%9C-%E9%80%9A%E7%94%A8-i.6064348.2308625483?sp_atk=64df70b3-8a12-4491-bae1-bcdf4364b3f5&xptdk=64df70b3-8a12-4491-bae1-bcdf4364b3f5')

html_code = dat.text
pattern = r'\$\d{1,3}(,\d{3})*'
number_pattern = re.compile(pattern)
price = number_pattern.findall('$25626525255knkbujuvbgjkvgghbjhgvfdctfgbhnjkhgctyfghnkjhbdcfgv5625126')
print(price)