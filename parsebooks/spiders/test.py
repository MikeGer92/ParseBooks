import math

from scrapy.http import HtmlResponse

next_page_a = ['https://book24.ru/search/?q=%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F']
name = 'book24'
allowed_domains = ['book24.ru']
start_urls = ['https://book24.ru/search/?q=%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F']
quant_pages = 3


def get_next_page(url, num):
    for i in range(2, num+1):
        next_link = str(url).split('?')
        next_page = f'{next_link[0]}page-{i}/?{next_link[1]}'.replace('[', '').replace(']', '')
        print(next_page)

get_next_page(start_urls, quant_pages)

