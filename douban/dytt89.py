# 有瑕疵,也得页面的源码不一样。
import re
import requests

domain = "https://dytt89.com"
# verity = false
resp = requests.get(domain)
# 国标码，国标码
resp.encoding = "gb2312"
# 预编译正则表达式，re.compile(), 生成的obj对象, 使用finditer()方法就可以找到html文档内匹配到正则表达式的内容
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word.*?<a href="(?P<ma>.*?)">', re.S)
obj4 = re.compile(r'◎片　　名(?P<movie>.*?)</p>.*?<td style="WORD-WRAP: break-word.*?<a href="(?P<ma>.*?)">', re.S)
result = obj1.finditer(resp.text)
children_href_list = []

# 遍历结果
for it in result:
    ul = it.group('ul')
    result2 = obj2.finditer(ul)
    for it2 in result2:
        # print(it2.group('href'))
        children_href = domain + it2.group('href')
        children_href_list.append(children_href)
# resp.close()

for href in children_href_list:
    children_resp = requests.get(href)
    children_resp.encoding = 'gbk'
    href = obj3.search(children_resp.text)
    print(href.group("movie").strip())
    print(href.group("ma"))
