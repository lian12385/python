# https://m3api.awenhao.com/index.php?note=kkRn39m56ryc1b4tqe7sh&raw=1&n.m3u8
# 通过查看页面源代码，找到该链接。和一步请求到的m3u8文件一致
# https://m3api.awenhao.com/index.php?note=kkR5s41nctk6rq8bdwpah&raw=1&n.m3u8

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)
url = "https://www.91kanju.com/vod-play/54812-1-1.html"
resp = requests.get(url, headers=headers)
m3u8_url = obj.search(resp.text).group("url")
resp.close()
with open("哲仁王后.m3u8", mode='wb') as f:
    f.write(requests.get(m3u8_url).content)

n = 0
with open("哲仁王后.m3u8", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()  # 去掉空格和换行
        if line.startswith("#"):
            continue
        respVideoContent = requests.get(line)
        f = open(f"videozhe/{n}.ts", mode='wb')
        f.write(respVideoContent.content)
        f.close()
        respVideoContent.close()
        n += 1
        print(f"完成了第{n}个！")
print("全部完成了！")