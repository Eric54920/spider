# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text']

    # 基于终端
    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content-left"]/div')
    #     lst = []
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract可以将Selector对象中存储在data中的字符串提取出来
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a/div/span[1]//text()').extract()
    #         content = ''.join(content)
    #         print(author, content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         lst.append(dic)
    #     return lst


    # 基于管道
    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中存储在data中的字符串提取出来
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()').extract_first().strip()
            content = div.xpath('./a/div/span[1]//text()').extract()
            content = ''.join(content)
            content = content.strip()
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            yield item