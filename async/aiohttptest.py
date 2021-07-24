import asyncio
import time

import aiohttp
import requests


# 用了32.71643686294556秒
def download(url):
    name = url.split("/")[-1]
    resp = requests.get(url)
    content = resp.content
    with open(name, mode="wb") as f:
        f.write(content)

# 协程用了9.352867841720581秒
async def aiodownload(url, session):
    name = url.split("/")[-1]
    async with session.get(url) as resp:
        content = await resp.content.read()
        with open("img/"+name, mode="wb") as f:
            f.write(content)


async def main():
    # 这里同名了。。。
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(aiodownload(url, session)) for url in urls]
        await asyncio.wait(tasks)


urls = [
    "http://kr.shanghai-jiuxin.com/file/2021/0524/cdbb43e819d3bb2bacc29e84deb4bff2.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/c08399ed43eda51e4a59431ca881b6b5.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/3f381541926e01ece21fd210f59af6d2.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/7c3ecc8fec6582fd504cf4df32236505.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/11a56f6cbc984b11c49c6cfe3f755adc.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/2c7deaca39bcb879a748076335e80b75.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/34dbcddeea33c791a3537899cf75e3c0.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/242c4ef41acc2e21215b27d89132e76d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/9f99a203cd305da6215d4144d84f2b0b.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/1d5d70d4a41614e157e47085f565e40d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/40da1fe46bfea8a7ffe05a3827e0fe91.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/08a288a1f647046be896e5d44cdd7607.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/355da8c5690c647a1883c99804ec78ad.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/18f9a3a4eb4825797e3e826d59aab5e1.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/bb07fc423cf73326a162c1257f43457c.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201608/5/h3lnu1zp5jp.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/d1a5464ba48dfcca284e1e938444c460.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/19279ccce470aebe5845768a299ad624.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/8707a6ad13f7776e2098a0d20a62fde0.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/bb3f28e53c089bc6512c49c4580627ad.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/03e452774291cd62f5788236a3e5c78b.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/56251c4fc058c403ce199c93f0223c8e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/1e16c77048687baea60c99b51975b7bc.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/8a8acd0e6c12e00415e0b3c5ab335378.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/2d9d7cefca1a93141c03b34291c62e6f.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0401/6c5ff0eadf820a8a29701269f3f7c768.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0330/719f9c91b683b023c56310fde5be0ed4.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0330/a867fe70ef6aa387da05ca41394796e2.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0324/88e5971fd1dc879babae975ebd032907.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0324/d181b5f9734f651f0d7633467ebc81dd.jpg",
]

if __name__ == '__main__':
    t2 = time.time()
    # aiodownload(url, session) for url in urls

    # for url in urls:
    #     download(url)

    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
    print(time.time() - t2)
