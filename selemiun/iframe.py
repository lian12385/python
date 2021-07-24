# from webbrowser import Chrome <自动导入的>
from selenium.webdriver import Chrome

web = Chrome()
web.get("https://www.91kanju.com/vod-play/541-2-1.html")
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe)

# #  获取元素标签的内容
# att01 = a_href.get_attribute('textContent')
# text_01 = a_href.text
#
# # # 获取元素内的全部HTML
# att02 = a_href.get_attribute('innerHTML')
#
# # # 获取包含选中元素的HTML
# att03 = a_href.get_attribute('outerHTML')
#
# # 获取该元素的标签类型
# tag01 = a_href.tag_name

val = web.find_element_by_xpath('/html/body/div[2]').get_attribute("textContent")
print(val)
# 切换到原本的html中
web.switch_to.default_content()