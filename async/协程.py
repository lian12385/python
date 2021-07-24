# input() 程序处于阻塞状态,
# requests.get()也是，
# 程序处于I/O操作也会
import asyncio

# async def func():
#     print("协程")
#
# if __name__ == '__main__':
#     coroutine = func()
#
#     asyncio.run(coroutine)
#     # 这两种方式是一样的
#     lop = asyncio._get_running_loop()
#     lop.run_until_complete(coroutine)
import time


async def func1():
    print("func1 start")
    await(asyncio.sleep(3))
    print("func1 end")


async def func2():
    print("func2 start")
    await(asyncio.sleep(2))
    print("func2 end")


async def func3():
    print("func3 start")
    await(asyncio.sleep(4))
    print("func3 end")


async def main():
    print("start")
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),#3.8之后的写法。
        asyncio.create_task(func3())
        # func1(),
        # func2(),
        # func3()
    ]
    done, pedding = await asyncio.wait(tasks)
    print("end")


if __name__ == '__main__':
    start = time.time()
    # 方式1
    # tasks = [
    #     func1(),
    #     func2(),
    #     func3()
    # ]
    # lop = asyncio.get_event_loop()
    # lop.run_until_complete(asyncio.wait(tasks))
    # print(time.time() - start)

    asyncio.run(main())
    print(time.time() - start)
