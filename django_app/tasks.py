from celery import shared_task
from scrapy.crawler import CrawlerProcess
from mycrawler.mycrawler.spiders.product_spider import ProductSpider
from billiard import Process

@shared_task
def run_spider():
    process = CrawlerProcess(settings={
        'FEEDS': {'oupt.json': {'format': 'json',
                                  'ensure_ascii': False}}
    })
    
    process.crawl(ProductSpider)
    process.start()
    
@shared_task
def run_scrapy_task():
    p = Process(target=run_spider)
    p.start()
    p.join()