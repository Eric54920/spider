# -*- coding: utf-8 -*-
import scrapy
from photoPro.items import PhotoproItem

class PhotoSpider(scrapy.Spider):
    name = 'photo'
    # allowed_domains = ['http://ilovepapers.com/daily-best/']
    start_urls = ['http://ilovepapers.com/daily-best/']

    def parse(self, response):
        li_list = response.xpath('/html/body/div/div[2]/div[4]/ul/li')
        for li in li_list:
            href = li.xpath('./div//div/img/@src').extract_first()
            item = PhotoproItem()
            item['href'] = href
            yield item