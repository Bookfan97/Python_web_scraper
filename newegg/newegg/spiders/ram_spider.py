# -*- coding: utf-8 -*-
import scrapy
from ..items import NeweggItem


class RamSpiderSpider(scrapy.Spider):
    name = 'ram_spider'
    page_number = 2
    max_page_count = 3 #100
    allowed_domains = ['newegg.com']
    start_urls = ['https://www.newegg.com/p/pl?d=ram&page=1']

    def parse(self, response):
        items = NeweggItem()
        ram_title = response.css('.item-title::text').extract()
        ram_price = response.css('.price-current').css('::text').extract()
        ram_image = response.css('.is-grid .item-img img::attr(src)').extract()
        items['ram_title'] = ram_title
        items['ram_price'] = ram_price
        items['ram_image'] = ram_image
        yield items
        next_page = 'https://www.newegg.com/p/pl?d=ram&Page=' + str(RamSpiderSpider.page_number)
        if RamSpiderSpider.page_number < RamSpiderSpider.max_page_count:
            RamSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
