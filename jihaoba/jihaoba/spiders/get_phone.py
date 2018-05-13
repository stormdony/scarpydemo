# -*- coding: utf-8 -*-
import scrapy

from jihaoba.items import JihaobaItem


class GetPhoneSpider(scrapy.Spider):
    name = 'get_phone'
    allowed_domains = ['www.jihaoba.com']
    start_urls = ['http://www.jihaoba.com/escrow/?&page=1']

    def parse(self, response):
        for numbershow in response.css('.numbershow'):
            href = numbershow.css('.hmzt > a::attr(href)').extract_first()
            phone = href[-15:-4]
            price = numbershow.css('.numbershow .price .red::text').extract_first()[1:]
            call_charge = numbershow.css('ul > li.price::text').extract_first()[2:]
            location = numbershow.css('.brand::text').extract_first()
            linkman = numbershow.css('.law::text').extract_first()[-7:-4]

            item = JihaobaItem()
            item['href'] = href
            item['phone'] = phone
            item['price'] = price
            item['call_charge'] = call_charge
            item['location'] = location
            item['linkman'] = linkman
            yield item

        next_url = response.css('.m-pages-next::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request(url="http://www.jihaoba.com" + next_url, callback=self.parse)
