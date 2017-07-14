import scrapy

class BizSpider(scrapy.Spider):
    name = 'bizspider'
    start_urls = ['https://www.kenyaplex.com/business-directory/?start=1']

    def parse(self, response):
        for detail in response.css('div.c-detail'):
            try:
                yield {'title': detail.css('a::text').extract_first(),
                 'email': detail.css('::text').extract()[3]}
            except IndexError:
                pass

        for next_page in response.css('a[title="Next page"]'):
            yield response.follow(next_page, self.parse)

