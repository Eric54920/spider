# -*- coding: utf-8 -*-
import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://ilovepapers.com/?s=sexy']

    def parse(self, response):
        li_list = response.xpath('/html/body/div/div[2]/div[4]/ul/li')

        for li in li_list:
            img_src = li.xpath('./div/a/div/img/@src').extract_first()
            item = ImgsproItem()
            item['src'] = img_src
            yield item
