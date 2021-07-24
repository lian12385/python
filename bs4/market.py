import csv

import requests
from bs4 import BeautifulSoup
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)
page = BeautifulSoup(resp.text, 'html.parser')
# 这一步就是把爬取下来的文件交给bs4来处理, BeautifulSoup("url",'html.parser'),然后就是用find或者find_all方法来获取
# 到相应的属性对应的标签
# print(page)
# find
# find_all
# class是关键字
# table = page.find("table", class_="hq_table")

table = page.find("table", attrs={"class": "hq_table"})
# print(table)
trs = table.find_all("tr")[1:]
f = open('price.csv', 'w', newline='', encoding='utf-8')
CsvWrite = csv.writer(f)
for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low_price = tds[1].text
    average_price = tds[2].text
    high_price = tds[3].text
    size = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    # print(name, low_price, average_price, high_price, size, kind, date)
    CsvWrite.writerow([name, low_price, average_price, high_price, size, kind, date])
print("over")
resp.close()

# test = open('test.csv', 'w', newline='', encoding='utf-8')
# CsvWriter = csv.writer(test)
