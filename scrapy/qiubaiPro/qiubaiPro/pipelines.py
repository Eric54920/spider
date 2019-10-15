# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QiubaiproPipeline(object):
    fp = None
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')

        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()

class MysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306, user='root', passwd='admin', db='qiubaiPro', charset='utf8')
    
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            sql = 'insert into qiubai values("%s", "%s")'
            self.cursor.execute(sql, (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()