from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from parsebooks import settings
from parsebooks.spiders.labirint import LabirintSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabirintSpider)

    process.start()