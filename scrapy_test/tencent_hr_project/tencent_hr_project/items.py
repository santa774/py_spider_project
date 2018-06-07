# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentHrProjectItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_category = scrapy.Field()
    job_count = scrapy.Field()
    job_address = scrapy.Field()
    job_time = scrapy.Field()
    pass
