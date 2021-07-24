

# 中转服务器: 通过ajax发送的异步请求：
# https://www.pearvideo.com/videoStatus.jsp?contId=1733373&mrd=0.2664019392601533
# 得到中转的视频连接
# https://video.pearvideo.com/mp4/adshort/20210626/1624765561843-15704680_adpkg-ad_hd.mp4
# 真实的视频链接
# https://video.pearvideo.com/mp4/adshort/20210626/cont-1733373-15704680_adpkg-ad_hd.mp4
import requests


url = "https://www.pearvideo.com/video_1733373"
contId = url.split('_')[1]
videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.04956514080012786'

headers = {
    # referer
    "Referer": url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()

# 这里找到实际的视频链接
srcUrl = dic['videoInfo']["videos"]["srcUrl"]
systemTime = dic['systemTime']
# 把系统时间字段替换成cont-{contId}
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")


with open('pearvideo.mp4', mode='wb') as f:
    f.write(requests.get(srcUrl).content)
f.close()
resp.close()
print('download success!')

# 这里多了一个防盗链的问题，还有就是前端发送请求给一个服务器，另一个服务器就返回响应，相应内容就包括视频的链接
# 这里把返回来的数据编程json格式, 然后把对应的url链接拿过来做替换