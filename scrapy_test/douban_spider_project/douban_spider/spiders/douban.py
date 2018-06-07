# -*- coding: utf-8 -*-
import scrapy
from scrapy_test.douban_spider_project.douban_spider.items import DoubanSpiderItem
# from scrapy_test.douban_spider.douban_spider_module.items import DoubanSpiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        # 此处的response 是请求start_urls的响应结果
        # 使用scrapy自带的xpath模块来筛选数据，xpath返回的都是列表
        # 首先获取所有的电影列表
        movies = response.xpath('//div/ul/li[contains(@class, "ui-slide-item")]')

        for movie in movies:
            item = DoubanSpiderItem()
            titles = movie.xpath('./@data-title').extract()
            directors = movie.xpath('./@data-director').extract()
            rates = movie.xpath('./@data-rate').extract()

            try:
                # print titles[0]
                # print directors[0]
                # print rates[0]
                item["title"] = titles[0]
                item["director"] = directors[0]
                item["rate"] = rates[0]
                yield item  # 返回给pipeline文件
            except Exception, e:
                pass

