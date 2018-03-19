# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixiCrawlspiderItem(scrapy.Item):
    post = scrapy.Field()
    urls = scrapy.Field()
    place = scrapy.Field()
    time = scrapy.Field()
    money = scrapy.Field()