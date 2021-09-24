import scrapy
from scrapy.http import HtmlResponse


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F/?available=1&paperbooks=1&ebooks=1']

    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@class="product-title-link"]/@href').extract()
        for link in links:
            print(link)
        pass
