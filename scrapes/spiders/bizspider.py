from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst, Compose
from scrapy.selector import Selector
from scrapy.spiders import Spider

from scrapes.items import BusinessItem

class BizSpider(Spider):
    """Spider for regularly updated kenyaplex.com site business directory"""

    name = 'bizspider'
    start_urls = ['https://www.kenyaplex.com/business-directory/?start=1']

    def parse(self, response):

        for business in response.css('div.c-detail'):

            try:
                loader = ItemLoader(item=BusinessItem(), selector=business)

                loader.add_css('title', 'a::text')
                loader.add_css('phone_number', '::text')
                loader.add_css('email', '::text')

                yield loader.load_item()
            except (IndexError, ValueError):
                pass

        for next_page in response.css('a[title="Next page"]'):
            yield response.follow(next_page, self.parse)
