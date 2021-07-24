import requests

url = "https://passport.17k.com/ck/user/login"
# requests.session().post(url,data=data)
# (1)用Session来获取相应的对象
# 用session来做请求
# session = requests.session()
# data = {
#     "loginName": "18614075987",
#     "password": "q6035945"
# }
#
# session.post(url, data=data)


# resp = session.get("https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919")
# print(resp.json())
# resp.close()

# (2)两种方式获取到cookie值
headers = {
    "Cookie": "GUID=0a87c71a-6270-4454-be68-a4eaddd883f9; sajssdk_2015_cross_new_user=1; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F16%252F16%252F64%252F75836416.jpg-88x88%253Fv%253D1610625030000%26id%3D75836416%26nickname%3DIT%25E5%25A4%25A7%25E5%25B8%2588%25E5%2593%25A5%25E6%2598%25AF%25E5%25B8%2585%25E6%25AF%2594%26e%3D1640315291%26s%3D266eeb0845a946c5; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2275836416%22%2C%22%24device_id%22%3A%2217a4b6c206a108-045c82787563d5-7a697d63-921600-17a4b6c206b2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%220a87c71a-6270-4454-be68-a4eaddd883f9%22%7D"
}
resp = requests.get('https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919', headers=headers)
resp.encoding = 'utf-8'
print(resp.json())

