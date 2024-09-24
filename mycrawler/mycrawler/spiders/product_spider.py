from pathlib import Path
import logging
import scrapy
from django_app.models import ScrapedProducts

logger = logging.getLogger('error_log')


class ProductSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        urls = [
            "https://netmall.hardoff.co.jp/search/?pricedown=1"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for _response in response.css('div.itemcolmn_item.itemcolmn_item--pricedown'):        
            try:
                s = ScrapedProducts(
                    name=_response.css('div.item-infowrap div.item-name::text').get(),
                    details=_response.css('div.item-infowrap div.item-brand-name::text').get(),
                    description=_response.css('div.item-infowrap div.item-code::text').get(),
                    condition=_response.css('div.item-infowrap li.item-taglist_item img::attr(alt)').get(),  
                    selling_status=(_response.css('div.item-img-square span.soldout-text::text').get() or 'AVAILABLE')
                )
                s.save()
            except Exception as e:
                logger.error(f"Error while scraping {response.url}: {e}")
            
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)