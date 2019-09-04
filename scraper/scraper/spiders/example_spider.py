import scrapy
from scrapy.spiders import Spider
from ..items import ScraperItem

# scrapy crawl example_spider
class Example_Spider(Spider):
    name = "example_spider"
    page_number = 2
    max_page_count = 3 #11
    start_urls = [
        'http://quotes.toscrape.com/page/1'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        print(token)
        items = ScraperItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
       # next_page = response.css('li.next a::attr(href)').get()
        next_page = 'http://quotes.toscrape.com/page/' + str(Example_Spider.page_number) + '/'
        if Example_Spider.page_number < Example_Spider.max_page_count:
            Example_Spider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
