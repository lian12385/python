import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", newline='', encoding='utf-8')
csvWrite = csv.writer(f)

def down_loadOnePage(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    trs = table.xpath("./tr[position()>1]")
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # print(txt)
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        csvWrite.writerow(txt)
        # print(list(txt))
    print('提取完毕')


if __name__ == '__main__':
    # 效率极其低下的一种方式,这是单线程的
    # for x in range(1, 3):
    #     down_loadOnePage(f'http://www.xinfadi.com.cn/marketanalysis/0/list/{x}.shtml')
    # f.close()

    # # 线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 500):
            t.submit(down_loadOnePage, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    # # @test
    # with ThreadPoolExecutor(30) as w1:
    #     for i in range(1, 100):
    #         w1.submit(down_loadOnePage, f"http://www.baiducom{i}")

    print("全部提取完成")
