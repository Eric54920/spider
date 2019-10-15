# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyixinwen.items import WangyixinwenItem

class XinwenSpider(scrapy.Spider):
    name = 'xinwen'
    # allowed_domains = ['www']
    start_urls = ['https://news.163.com']
    models_urls = []

    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        index = [3,4,6,7,8]
        for i in index:
            self.models_urls.append(li_list[i].xpath('./a/@href').extract_first())

        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)
    
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyixinwenItem()
            item['title'] = title
            try:
                yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item':item})
            except Exception:
                continue
    
    def parse_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item['content'] = content.strip()
        yield item

    def closed(self, spider):
        self.bro.quit()