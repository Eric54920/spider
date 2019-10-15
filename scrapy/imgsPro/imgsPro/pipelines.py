# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImgsproPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])
    
    def file_path(self, request, response=None, info=None):
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        return item