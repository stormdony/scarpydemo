# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziCarItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()#标题
    time = scrapy.Field()#上牌时间
    milestone = scrapy.Field()#里程数
    GB = scrapy.Field()#外迁查询
    displacement = scrapy.Field()#排量
    get_car_time = scrapy.Field()#提车时间
    price = scrapy.Field()#车主报价
