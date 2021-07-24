import requests
import re
import csv
# 用for循环来遍历豆瓣top250
url = "https://movie.douban.com/top250?start="
start = 0
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
}
while start < 250:
    NewUrl = url + str(start)
    resp = requests.get(NewUrl, headers=headers)
    page_content = resp.text
    # 关闭请求
    resp.close()
    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)'
                     r'&nbsp.*?<span class="rating_num" property="v:average">(?P<average>.*?)'
                     r'</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(page_content)
    f = open("data.csv", mode="a+", newline="", encoding="utf-8")
    CsvWriter = csv.writer(f)
    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("average"))
        # print(it.group("num"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        CsvWriter.writerow(dic.values())
    print("over")
    f.close()
    start = int(start) + 25

# 关于如何使用csv模块如何写入数据:用csv的writer->然后到writerow方法
# csv.writer(f)
