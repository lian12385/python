from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
import time

chaojiying = Chaojiying_Client('1421eeq', 'Qwertyu88', '919628')

option = Options()

option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

time.sleep(2)
web.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
time.sleep(3)
verify_img = web.find_element_by_xpath('//*[@id="J-loginImg"]')
result = chaojiying.PostPic(verify_img.screenshot_as_png, 9004)

points_str_lst = result['pic_str'].split("|")
for p in points_str_lst:
    p_temp = p.split(",")
    p_x = int(p_temp[0])
    p_y = int(p_temp[1])

ActionChains(web).move_to_element_with_offset(verify_img, p_x, p_y).click().perform()

time.sleep(1)
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("123456789@qq.com")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys("123456789@qq.com")
time.sleep(1)
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()

print('测试成功！')


