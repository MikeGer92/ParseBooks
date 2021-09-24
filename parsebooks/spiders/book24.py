import math
import scrapy
from scrapy.http import HtmlResponse

class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F']

    books_links = []

    def get_pages_list(self, resp: HtmlResponse):
        pages_list = []
        pages_list.append(self.start_urls[0])
        quant_books = str(resp.xpath('//div[@class="search-page__desc"]').extract())
        quant_books = int("".join(filter(str.isdigit, quant_books)))
        links = resp.xpath('//div[@class="product-card__content"]/a/@href').extract()
        quant_pages = math.ceil((int(quant_books) / len(links))/100)
        while quant_pages > 1:
            next_page = (self.get_next_page(self.start_urls, quant_pages)).replace("'", "")
            pages_list.append(next_page)
            quant_pages -= 1
        return pages_list

    def get_next_page(self, url, num):
        next_link = str(url).split('?')
        next_page = f'{next_link[0]}page-{num}/?{next_link[1]}'.replace('[', '').replace(']', '')
        return next_page

    def parse(self, response: HtmlResponse):
        pages = (self.get_pages_list(response))
        self.get_books_list(response, pages)

    def get_books_list(self, response: HtmlResponse, lst):
        print(lst)
        for page in lst:
            print(page)
            yield response.follow(page, callback=self.get_fin_links)

    def get_fin_links(self, response):
        links = response.xpath('//div[@class="product-card__content"]/a/@href').extract()
        for link in links:
            self.books_links.append(link)
        print(len(self.books_links))
        print(len(set(self.books_links)))








