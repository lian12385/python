import time

import requests
from bs4 import BeautifulSoup

base_url = "https://www.umei.net/bizhitupian/meinvbizhi/"
url = "https://www.umei.net"
resp = requests.get(base_url)
resp.encoding = 'utf-8'
# print(resp.text)
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("div", class_="TypeList").find_all('a')
# main_page = main_page.find('div', attrs={"class": "TypeList"})
for it in alist:
    href = url + it.get("href")
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_main_page = BeautifulSoup(child_page_resp.text, 'html.parser')
    img = child_main_page.find('div', class_="ImageBody").find('img')
    # img_list = child_main_page.find('p', align='center')
    # print(img)
    link = img.get('src')
    print('"'+link+ '",')
    break
    print(link)
    real_img = requests.get(link)
    name = link.split("/")[-1]
    # 文件操作
    with open("img/" + name, 'wb') as f:
        f.write(real_img.content)
    print(name, "over")
    time.sleep(1)
resp.close()
print('down is over! ')
