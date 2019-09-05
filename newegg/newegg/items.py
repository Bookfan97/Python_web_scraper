# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggItem(scrapy.Item):
    # define the fields for your item here like:
    ram_title = scrapy.Field()
    ram_price = scrapy.Field()
    ram_image = scrapy.Field()
    pass
