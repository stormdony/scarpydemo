# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JihaobaItem(scrapy.Item):
    # define the fields for your item here like:
    phone = scrapy.Field()#号码
    price = scrapy.Field()#价格
    call_charge = scrapy.Field()#话费
    location = scrapy.Field()#归属地
    linkman = scrapy.Field()#联系人
    href = scrapy.Field()#链接
