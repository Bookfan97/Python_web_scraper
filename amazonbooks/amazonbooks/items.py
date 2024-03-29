# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonbooksItem(scrapy.Item):
    # define the fields for your item here like:
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    book_cover = scrapy.Field()
    pass
