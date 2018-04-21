# -*- coding: utf-8 -*-
import telnetlib

import scrapy

from get_ip_demo.items import GetIpDemoItem

class GetIpSpider(scrapy.Spider):
    name = 'get_ip'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        ip_list = response.css('.odd')
        for each_ip in ip_list:
            ip = each_ip.xpath('td[2]/text()').extract_first()
            port = each_ip.xpath('td[3]/text()').extract_first()
            province = each_ip.xpath('td[4]/text()').extract_first()
            alive = each_ip.xpath('td[7]/text()').extract_first()
            active = each_ip.xpath('td[8]/text()').extract_first()
            item = GetIpDemoItem()
            item['ip'] = ip
            item['port'] = port
            item['province'] = province
            item['alive'] = alive
            item['active'] = active
            try:
                telnetlib.Telnet(ip, port=port, timeout=20)#验证是否可用
            except:
                print('connect failed')
            else:
                print('success')
                yield item
