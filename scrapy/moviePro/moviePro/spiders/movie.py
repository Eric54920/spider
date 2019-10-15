# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem

class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.ccc.com']
    start_urls = ['https://www.4567tv.tv/frim/index1.html']

    rules = (
        Rule(LinkExtractor(allow=r'frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )

    conn = Redis(host='127.0.0.1', port=6379)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            detail_url = 'https://www.4567tv.tv' + li.xpath('./div/a/@href').extract_first()
            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('这条url没有请求过，可以请求')
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            else:
                print('这条url已经请求过')
        
    def parse_detail(self, response):
        name = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]//text()').extract()
        desc = ''.join(desc)
        item = MovieproItem()
        item['name'] = name
        item['desc'] = desc
        yield item


