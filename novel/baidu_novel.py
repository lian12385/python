import asyncio

import requests
import aiohttp
from bs4 import BeautifulSoup


# async def download(gid, cid, title, session):
#     params = {
#         "book_id": gid,
#         "cid": f"{gid}|{cid}",
#         "need_bookinfo": 1
#     }
#     url = f'http://dushu.baidu.com/api/pc/getChapterContent?data{json.dumps(params)}'
#     async with session.get(url) as resp:
#         dic = await resp.json()
#         with open(f"novel/{title}.txt", mode='w', encoding="utf-8") as f:
#             f.write(dic['data']['novel']['content'].replace("\n",""))
#             return f"{title}, download ok!"

async def download(href, session):
    url = "https:" + href
    # print(url)
    async with session.get(url) as resp:
        mainpage2 = await resp.text()
        # print(mainpage2)
        # breakpoint()
        mainpage3 = BeautifulSoup(mainpage2, 'html.parser')
        # print(mainpage3)
        content = mainpage3.find("div", class_="read-content j_readContent").find('p')
        title = mainpage3.find("span", class_="content-wrap")
        # print(content)
        p = content.find_all("p")
        with open(f"novel/{title.text}.txt", mode='w', encoding='utf-8') as f:
            # for item in p:
            #     print(item)
            #     f.write(item.text)
            f.write(p[0].text)
            return f'{content[0]}, download ok!'


async def main():
    url = "https://book.qidian.com/info/1024997264#Catalog"
    # 随便上网找的一个网站,
    '''
    https://book.qidian.com/info/1024997264#Catalog
    https://read.qidian.com/chapter/elqC0KCezksVDwQbBL_r1g2/JvyGcaagxjNOBDFlr9quQA2
    '''

    # gid = '4306063500'
    # 十分可惜，百度小说做了处理，我找不到那个ajax请求，看不到他的数据在哪
    # url = f'http://dushu.baidu.com/api/pc/getCatalog?data{{"book_id":"{gid}"}}'

    resp = requests.get(url)
    main_page = BeautifulSoup(resp.text, 'html.parser')
    hreflist = main_page.find("ul", class_="cf").find_all('a')
    # print(hreflist)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for href in hreflist:
            # print(href.get('href'))
            tasks.append(asyncio.create_task(download(href.get('href'), session)))
        done, pedding = await asyncio.wait(tasks)
        for item in done:
            print(item.result())


if __name__ == '__main__':
    asyncio.run(main())

