# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XiaohuaproPipeline(object):
    fp = None
    def open_spider(self, spider):
        print('start...')
        self.fp = open('./xiaohua.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        self.fp.write(title+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('over!!!')
