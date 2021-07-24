from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time

# 无头浏览器配置
# 就5句
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_argument('---headless')
opt.add_argument('disable-gpu')

web = Chrome(options=opt)
# 无头浏览器配置

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

time.sleep(3)
print(web.page_source)# 打印element里面的源码

# sel = Select(web.find_element_by_xpath('//*[@id="OptionDate"]'))
#
#
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(1)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table')
#
#     print("1111111111111111111111")
#     print(table.text)
# print('done')

'''1111111111111111111111
  影片名称 类型 总票房(万) 平均票价 场均人次 国家及地区 上映日期
1
你好，李焕英
喜剧 541,330 45 24 中国 2021-02-12
2
唐人街探案3
喜剧 451,505 48 31 中国 2021-02-12
3
速度与激情9
动作 139,233 39 13 美国 2021-05-21
4
哥斯拉大战金刚
动作 123,262 37 9 美国 2021-03-26
5
送你一朵小红花
剧情 119,592 37 10 中国 2020-12-31
6
悬崖之上
剧情 118,915 39 12 中国 2021-04-30
7
刺杀小说家
奇幻 103,521 47 16 中国 2021-02-12
8
我的姐姐
剧情 86,018 37 9 中国 2021-04-02
9
你的婚礼
爱情 78,924 38 15 中国 2021-04-30
10
人潮汹涌
剧情 76,248 41 10 中国 2021-02-12
11
拆弹专家2
动作 71,250 39 8 中国 2020-12-24
12
温暖的抱抱
喜剧 66,954 37 9 中国 2020-12-31
13
熊出没·狂野大陆
动画 55,989 44 19 中国 2021-02-12
14
新神榜：哪吒重生
动画 45,648 44 14 中国 2021-02-12
15
扫黑·决战
剧情 40,548 34 9 中国 2021-05-01
16
阿凡达
科幻/动作 37,556 35 8 美国 2010-01-04
17
我要我们在一起
爱情 32,621 37 9 中国 2021-05-20
18
1921
剧情 29,887 35 10 中国 2021-07-01
19
心灵奇旅
动画 29,798 38 8 美国 2020-12-25
20
侍神令
奇幻 27,409 46 15 中国 2021-02-12
21
哆啦A梦：伴我同行2
动画 27,290 34 7 日本 2021-05-28
22
寂静之地2
惊悚 24,950 35 7 美国 2021-05-28
23
追虎擒龙
动作 24,362 38 10 中国/中国香港 2021-05-01
24
大红包
喜剧 23,533 33 6 中国 2021-01-22
25
当男人恋爱时
爱情 23,076 32 7 中国台湾/中国香港 2021-06-11
1111111111111111111111'''