# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem

class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.ccc.com']
    # start_urls = ['http://www.ccc.com/']

    redis_key = 'sun'

    rules = (
        Rule(LinkExtractor(allow=r'question/report\?page=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'), callback='parse_detail')
    )

    def parse_item(self, response):
        new_list = response.xpath('/html/body/div[8]/table[2]//tr')
        for i in new_list:
            new_id = i.xpath('./td[1]/text()').extract_first()
            new_title = i.xpath('./td[3]/a/text()').extract_first()
            item = FbsproItem()
            item['new_id'] = new_id
            item['new_title'] = new_title
            yield item