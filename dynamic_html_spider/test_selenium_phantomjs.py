# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 设置浏览器对象
# driver = webdriver.PhantomJS(executable_path='D:\\phantomjs\\bin\\phantomjs.exe')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
starttime = time.time()
driver = webdriver.Chrome('C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe',
                          chrome_options=chrome_options)
print "加载ChromeDriver耗时：" + str(time.time() - starttime)
# 设置访问网址，加载网站内容
driver.get("https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=1")
# 查找具体的内容
driver.find_element_by_class_name("img_land_next").click()
# 截取当前显示的内容
driver.save_screenshot("one_punch_1.png")
# 打印网页源码内容
with open("one_puch.html", "w") as f:
    f.write(driver.page_source.encode("utf-8"))
