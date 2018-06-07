# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_test.tencent_hr_project.tencent_hr_project.items import TencentHrProjectItem


class TencentHRSpider(CrawlSpider):
    name = 'tencentHR'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["https://hr.tencent.com/position.php?keywords=&tid=0&start=0"]

    linkExtractor = LinkExtractor(allow=("start=\d+"))
    rules = [
        Rule(linkExtractor, callback="parse_tencentHR", follow=True),
    ]

    def parse_tencentHR(self, response):
        # 此处的response 是请求start_urls的响应结果
        # 使用scrapy自带的xpath模块来筛选数据，xpath返回的都是列表
        # 首先获取所有的电影列表
        jobs = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for job in jobs:
            item = TencentHrProjectItem()
            job_names = job.xpath('./td[1]/a/text()').extract()
            job_categorys = job.xpath('./td[2]/text()').extract()
            job_counts = job.xpath('./td[3]/text()').extract()
            job_addresses = job.xpath('./td[4]/text()').extract()
            job_times = job.xpath('./td[5]/text()').extract()

            try:
                # print job_names[0]
                # print job_categorys[0]
                # print job_counts[0]

                item["job_name"] = job_names[0]
                item["job_category"] = job_categorys[0]
                item["job_count"] = job_counts[0]
                item["job_address"] = job_addresses[0]
                item["job_time"] = job_times[0]
                yield item  # 返回给pipeline文件
            except Exception, e:
                pass

            # if self.page < 3970:
            #     self.page += 10
            # # 继续访问下一页
            # yield scrapy.Request(self.base_url + str(self.page), callback=self.parse)



