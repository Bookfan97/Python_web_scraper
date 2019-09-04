# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbooksItem


class AmazonBooksSpider(scrapy.Spider):
    name = 'amazon_books'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?k=harry+potter&i=stripbooks&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        items = AmazonbooksItem()
        book_title = response.css('.a-color-base.a-text-normal::text').extract()
        book_author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        book_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
        book_cover = response.css('.s-image-fixed-height .s-image::attr(src)').extract()
        items['book_title'] = book_title
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['book_cover'] = book_cover
        yield items
