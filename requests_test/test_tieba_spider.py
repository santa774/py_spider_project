# -*- coding: utf-8 -*-
import requests
import urllib2
import urllib
import time
from lxml import etree


class Spider:

    def __init__(self, tieba_name, start_page, end_page):
        self.tieba_name = tieba_name
        self.start_page = start_page
        self.end_page = end_page
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
        }

    def load_tieba_page(self):
        proxies = {
            "http": "180.101.205.253:8888",
            "https": "180.101.205.253:8888"
        }
        url = "http://tieba.baidu.com/f?"
        for page in range(int(self.start_page), int(self.end_page)):
            page = (page - 1) * 50
            param = {"kw": self.tieba_name, "pn": str(page)}

            # urllib2方式请求数据
            # request = urllib2.Request(url + urllib.urlencode(param), headers=header)
            # tieba_response = urllib2.urlopen(request)
            # html = tieba_response.read()

            # requests方式请求数据
            tieba_response = requests.get(url, params=param, headers=self.header)
            html = tieba_response.content
            # 以上获取的内容为贴吧一整页的html，包含了帖子的列表
            # 获取每一个帖子的链接
            xpath_result = etree.HTML(html)
            with open("G:\\tieba\\" + str(page) + ".html", "w") as f:
                f.write(html)
            tiezi_list = xpath_result.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
            self.load_tiezi_page(tiezi_list)
        print "done"

    def load_tiezi_page(self, tiezi_list):
        for tiezi_url in tiezi_list:
            url = "http://tieba.baidu.com" + tiezi_url
            tiezi_response = requests.get(url, headers=self.header)
            html = tiezi_response.content
            # 以上获取的内容为帖子一整页的html
            # 获取每一个帖子的图片链接
            xpath_result = etree.HTML(html)
            tiezi_img_list = xpath_result.xpath('//img[@class="BDE_Image"]/@src')
            self.load_image(tiezi_img_list)

    def load_image(self, tiezi_ima_list):
        for img_url in tiezi_ima_list:
            img_response = requests.get(img_url, headers=self.header)
            img_name = img_url[-7:]
            with open("G:\\tieba\\" + img_name, "wb") as f:
                f.write(img_response.content)


if __name__ == "__main__":
    tieba_name = raw_input("请输入要爬取的贴吧：")
    start_page = raw_input("请输入起始页：")
    end_page = raw_input("请输入结束页：")
    star_time = time.time()
    spider = Spider(tieba_name, start_page, end_page)
    spider.load_tieba_page()
    print "耗时：" + str(time.time() - star_time)
