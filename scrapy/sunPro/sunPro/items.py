# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    new_id = scrapy.Field()
    new_title = scrapy.Field()

class DetailItem(scrapy.Item):
    new_num = scrapy.Field()
    new_content = scrapy.Field()
