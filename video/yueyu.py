"""
    1.拿到主页源代码，找到iframe的链接
    2.拿到iframe链接的页面源码，获取m3u8链接
    3.下载m3u8文件(2层)，过程有些繁琐
    4.对文件进行检索，拿到小视频的链接，进行异步下载
    5.解密合并小的文件切片还原为大的MP4文件仅从播放
"""

import requests
import re
import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup
from Crypto.Cipher import AES  #pycryptodome
# from Crypto import AES
import os


def get_iframe_src(url):
    iframe_resp = requests.get(url)
    main_page = BeautifulSoup(iframe_resp.text, "html.parser")
    src = main_page.find("iframe").get("src")
    print(src)
    # return "https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFp"  # 得到了iframe的src


def get_first_m3u8_url(url):
    resp = requests.get(url)
    # print(resp.text)
    obj = re.compile(r'var main = "(?P<m3u8_url>.*?)"', re.S)
    m3u8_url = obj.search(resp.text).group("m3u8_url")
    # print(m3u8_url)
    return m3u8_url

# 第一层的m3u8文件，找ajax发送的请求，第一词发送的一般在第一条，然后找和resource文件下的源代码匹配
def get_first_m3u8_url(url):
    first_m3u8_resp = requests.get(url)
    obj = re.compile(r'var main="(?P<m3u8_url>.*?)', re.S)
    m3u8_url = obj.search(first_m3u8_resp.text).group("m3u8_url")
    return m3u8_url

# 下载m3u8文件，可复用
def download_m3u8_file(url, name):
    resp =requests.get(url)
    with open(name, mode='wb') as f:
        f.write(resp.content)


async def downlaod_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f'vide2/{name}',mode='wb') as f:
            await f.write(await resp.content.read())
    print('下载完成！')


# 创建一部下载任务
async def aio_download(second_m3u8_url_download):
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("越狱第一季第一集.txt", mode='r', encoding='utf-8') as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()
                ts_url = second_m3u8_url_download + line
                task = asyncio.create_task(downlaod_ts(ts_url, line, session))
                tasks.append(task)
            await asyncio.wait(tasks)

def get_key(key_url):
    resp = requests.get(key_url)
    return resp.text

async def dec_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video2/{name}", mode='rb') as f1, \
        aiofiles.open(f"video2/temp_{name}", mode='wb') as f2:

        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f"{name} 处理完成")



async def aio_dec(key):
    tasks = []
    async with aiofiles.open("越狱第一季第一集2.txt", mode='r', encoding='utf-8') as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            task = asyncio.create_task(dec_ts(line, key))
            tasks.append(task)
        await asyncio.wait(tasks)

def merge_ts():
    "windows: copy /b 1.ts+2.ts+3.ts xxx.mp4"
    lst = []
    with open("越狱第一季第一集2.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            lst.append(f"video2/temp_{line}")
    s = "+".join(lst)
    os.system(f"copy /b {s} movie.mp4")
    print("下载终于完成了")




def main(url):
    # 1.iframe的src
    iframe_url = get_iframe_src(url)
    # 2.第一层的m3u8文件，通过source里面的页面源代码，搜索m3u8然后就在script标签里面找到了该地址
    #这一步操作是为了获取到第一层的m3u8文件的下载链接地址的
    first_m3u8_url = get_first_m3u8_url(iframe_url)
    # iframe的真正下载地址，需要拼接字符串。 split
    # 第二层的m3u8文件，怎么找到呢，看第一层爬下来的m3u8文件，有个链接，然后，
    # 看下面发送的ajax请求，比对一下，找到域名(就是第一次请求iframe的网址的域名
    iframe_domain = iframe_url.split("/share")[0] #就是iframe的url
    first_m3u8_url = iframe_domain + first_m3u8_url #拼接成功了
    download_m3u8_file(first_m3u8_url, "越狱第一季第一集.txt")

    # 下载好了之后就去读取第一个m3u8文件
    with open("越狱第一季第一集.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip() # hls/index.m3u8
                # 准备拼接第二层m3u8的下载路径
                # https://boba.52kuyun.com/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1 这是第一层m3u8文件
                # https://boba.52kuyun.com/20170906/Moh2l9zV/ + hls/index.m3u8
                # https://boba.52kuyun.com/20170906/Moh2l9zV/hls/index.m3u8  第二次m3u8下载路径
                second_m3u8_url = first_m3u8_url.split("/index.m3u8")[0] + line
                download_m3u8_file(second_m3u8_url, "越狱第一季第一集2.txt")
                print('总的m3u8文件下载完成！')
                # cFN8o3436000.ts 第二个m3u8文件的路径
    # https://boba.52kuyun.com/20170906/Moh2l9zV/hls/cFN8o3436000.ts  ts下载路径

    second_m3u8_url_download = second_m3u8_url.replace("index.m3u8", "")

#     异步协程
    asyncio.run(aio_download(second_m3u8_url_download))

    # 这里还是要看xhr请求
    key_url = second_m3u8_url_download + "key.key" #偷懒写法

    key = get_key(key_url)

    # 5.2 解密
    asyncio.run(aio_dec(key))

    # 6. 合并ts文件为mp4文件
    merge_ts()


if __name__ == '__main__':
    url = "https://www.91kanju.com/vod-play/5104-1-1.html"
    main(url)
