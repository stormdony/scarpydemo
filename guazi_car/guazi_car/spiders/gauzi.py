# -*- coding: utf-8 -*-
import scrapy

from guazi_car.items import GuaziCarItem
import re

class GauziSpider(scrapy.Spider):
    name = 'gauzi'
    allowed_domains = ['www.xin.com']
    start_urls = ['https://www.xin.com/guangzhou/s/']

    def parse(self, response):
        num = len(response.xpath('//li[@class="con caritem conHeight"]').extract())
        for i in range(1, num+1):
            url = response.xpath('//li[{}]/div/a[@class="aimg"]/@href'.format(i)).extract_first()
            real_url = "https:"+str(url)
            yield scrapy.Request(url=real_url, callback=self.parse_detail)

        next_url = response.xpath('//div[@class="con-page search_page_link"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url:
            yield scrapy.Request(url="https://www.xin.com"+next_url, callback=self.parse)

    # 下一页
    # // div[@class="con-page search_page_link"]/a[contains(text(),"下一页")]

    def parse_detail(self, response):
        car_detail = response.xpath('/html/body/div[2]/div[2]')
        if car_detail:
            # 标题
            title = response.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/span/text()').extract_first()
            # 上牌时间
            time = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[1]/span[2]/text()').extract_first()
            # 里程数
            milestone = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[2]/a/text()').extract_first()
            # 外迁查询
            GB = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[3]/span[1]/text()').extract_first()
            # 排量
            displacement = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[4]/span[1]/text()').extract_first()
            # 提车时间
            get_car_time = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[5]/span[1]/text()').extract_first()
            # 车主报价
            price = response.xpath('//span[@class="cd_m_info_jg"]/b/text()').extract_first()
            real_price = re.findall(r'\d+.\d+',price)

            item = GuaziCarItem()
            item['title'] = title.strip()
            item['time'] = time.strip()
            item['milestone'] = milestone.strip()
            item['GB'] = GB.strip()
            item['displacement'] = displacement.strip()
            item['get_car_time'] = get_car_time.strip()
            item['price'] = real_price[0]
            print("ok")
            yield item

