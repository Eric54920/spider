# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class SunproPipeline(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='sunPro', charset='utf8')
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        if item.__class__.__name__ == 'SunproItem':
            self.cursor.execute(f'insert into sun(id, title) values({item["new_id"]},{item["new_title"]})')
        # else:
        #     num = int(item['new_num'])
        #     print(type(num), num)
        #     self.cursor.execute('insert into content(id, content) values(%d, "%s")', (num, item['new_content']))
        # return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()