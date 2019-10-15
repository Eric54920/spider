# -*- coding: utf-8 -*-
import scrapy


class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/', 'http://www.sogou.com']

    def parse(self, response):
        print(response)
