# -*- coding: utf-8 -*-
import scrapy
from zhipinPro.items import ZhipinproItem

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=']

    page_num = 2
    href = 'https://www.zhipin.com/c101010100/?query=python&page=%d'
    def detail_parse(self, response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc
        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:
            item = ZhipinproItem()
            job_name = li.xpath('./div/div[1]/h3/a/div[1]/text()').extract_first()
            detail_url = 'https://www.zhipin.com' + li.xpath('./div/div[1]/h3/a/@href').extract_first()
            item['job_name'] = job_name
            yield scrapy.Request(detail_url, callback=self.detail_parse, meta={'item':item})

        if self.page_num <= 3:
            new_href = self.href%self.page_num
            self.page_num += 1
            yield scrapy.Request(new_href, callback=self.parse)