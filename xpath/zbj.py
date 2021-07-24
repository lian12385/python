import requests
from lxml import etree
# 一生之敌
# 有一个广告界面导致了有一个空数据
url = "https://zhanjiang.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
# print(resp.text)
# 把页面内容拉进来
html = etree.HTML(resp.text)
# 解析响应对数据
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    # price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')[0].strip('￥')
    title = 'saas'.join(div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[1].strip("\n\n")
    location = div.xpath('./div/div/a[2]/div[1]/div/span/text()')
    print(com_name)
resp.close()

# xpath就是根据xml标签名来到对应的数据, 可以到浏览器Copy xpath下来再慢慢对比是否正确
# html = etree.HTML(resp.text),然后利用这个对象的xpath方法找，参数就是xpath路径


