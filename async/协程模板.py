import asyncio


async def download(url):
    print("开始抓取")
    await asyncio.sleep(3)  # 假装抓取
    print("抓取完毕")
    return "不信"


async def main():
    urls = [
        "url1",
        "url2",
        "url3"
    ]
    # 生成任务列表
    tasks = [download(url) for url in urls]
    done, pedding = await asyncio.wait(tasks)
    for d in done:
        print(d.result())


if __name__ == '__main__':
    asyncio.run(main())
