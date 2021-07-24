from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()
web.get("http://www.chaojiying.com/user/login/")

code_img = web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/div/img")

png_code_img = code_img.screenshot_as_png

chaojiying = Chaojiying_Client('1421eeq', 'Qwertyu88', '919628')

result = chaojiying.PostPic(png_code_img, 1902)

web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input").send_keys("1421eeq")
web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input").send_keys("Qwertyu88")
web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input").send_keys(result['pic_str'])
time.sleep(5)
web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()

