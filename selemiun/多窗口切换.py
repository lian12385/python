from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get("http://www.lagou.com")

el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[4]/a').click()
time.sleep(2)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("java", Keys.ENTER)
time.sleep(2)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
time.sleep(1)

# 要手动切换窗口，
web.switch_to.window(web.window_handles[-1])
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
# job_detail
'''
岗位职责:
我们需要您：
1、主要负责公司业务平台及周边系统的部分业务功能。
2、参与需求并根据现有架构进行业务逻辑设计。
3、对代码质量输出，有规范，可读性好。
任职资格:
我们希望您：
1、计算机相关专业，本科及以上学历。
2、至少三年以上Java开发经验，并熟悉软件开发流程。
3、JAVA 基础扎实，熟悉Java集合框架，熟练掌握各类常用数据结构和相关算法,并对多线程编程有较好的了解。
4、掌握一定程度的Java语言程序调优方法。
5、熟练使用MYSQL等数据库系统。
6、对常见的Web业务场景有通用的解决方法和能力。


如果您拥有以下相关技能,则更好:
1.熟悉主流开源应用框架，如 Spring、Springboot、Mybatis、JPA。
2.熟悉网络通信协议（ UDP/TCP、HTTP/HTTPS ），熟悉关系型数据库（ MySQL、Oracle 等）以及相应数据库调优、SQL 优化，熟悉 Redis、MongoDB等 NOSQL 。
3.对开源项目,不限语言或者是领域,有热忱,并投入过相应成本学习。

（入职后公司提供免费班车在万胜围地铁口接送！）
'''