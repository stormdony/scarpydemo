# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        for info in response.xpath('//div[@class="item"]'):
            item = DoubanmovieItem()
            item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
            item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            yield item

        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)