# -*- coding: utf-8 -*-
import scrapy
from xiaohuaPro.items import XiaohuaproItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')

        for li in li_list:
            dic = XiaohuaproItem()
            title = li.xpath('./a[2]/text() | ./a[2]/b/text()').extract_first()
            dic['title'] = title
            yield dic

        if self.page_num < 12:
            new_url = self.url%self.page_num
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

