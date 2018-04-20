# -*- coding: utf-8 -*-
import scrapy

from imgscrapydemo.items import ImgscrapydemoItem


class ImgdemoSpider(scrapy.Spider):
    name = 'imgdemo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/p/4023230951']

    def parse(self, response):
        item = ImgscrapydemoItem()
        img_url = response.xpath('//*[@id="post_content_75283192143"]/img/@src').extract()
        print('the urls:/n')
        print(img_url)
        item['img_url'] = img_url
        return item
