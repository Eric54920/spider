# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem, DetailItem

# scrapy genspider -t crawl sun www.ccc.xom

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.cc.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']

    rules = (
        Rule(LinkExtractor(allow=r'question/report\?page=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'), callback='parse_detail')
    )

    def parse_item(self, response):
        new_list = response.xpath('/html/body/div[8]/table[2]//tr')
        for i in new_list:
            new_id = i.xpath('./td[1]/text()').extract_first()
            new_title = i.xpath('./td[3]/a/text()').extract_first()
            item = SunproItem()
            item['new_id'] = new_id
            item['new_title'] = new_title
            yield item

    def parse_detail(self, response):
        new_num = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        # new_num = new_num.split(':')[-1]
        new_content = response.xpath('/html/body/div[9]/table[2]//tr[1]/td/text()').extract()
        new_content = ''.join(new_content)
        item = DetailItem()
        item['new_num'] = new_num
        item['new_content'] = new_content
        yield item