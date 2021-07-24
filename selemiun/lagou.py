from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time
web = Chrome()
web.get("http://lagou.com")


el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[4]/a')
el.click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys("java", Keys.ENTER)
time.sleep(1)

f = open("lagou.txt", mode="w", newline='', encoding='utf-8')
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    job_company = li.find_element_by_xpath('./div/div[2]/div/a').text
    f.write(job_name+", "+job_price+", "+job_company+"\n")
    print(job_name, job_price, job_company)
f.close()
print("done")
