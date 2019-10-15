# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MovieproPipeline(object):
    conn = None
    def open_spider(self, spider):
        self.conn = spider.conn
    def process_item(self, item, spider):
        dic = {
            'name':item['name'],
            'desc':item['desc']
        }
        self.conn.lpush('movieData', dic)
        return item
