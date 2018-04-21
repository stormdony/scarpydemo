# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetIpDemoItem(scrapy.Item):
    # define the fields for your item here like:
    ip = scrapy.Field()
    port = scrapy.Field()
    alive = scrapy.Field()#存活时间
    province = scrapy.Field()#位置
    active = scrapy.Field()#验证时间

