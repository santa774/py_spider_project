# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy_test.zhihu_project.zhihu_project.items import ZhihuProjectItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "email": "13535234074",
                "origURL": "http%3A%2F%2Fwww.renren.com%2Fhome",
                "domain": "renren.com",
                "key_id": "1",
                "captcha_type": "web_login",
                "password": "233333rr",
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            # self.log("Login failed", level=log.ERROR)
            return

        # continue scraping with authenticated session...
        print response.body
