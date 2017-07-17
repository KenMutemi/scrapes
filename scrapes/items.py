# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, Compose, TakeFirst, Compose


class BusinessItem(Item):
    """Scrapes Business container for scraped data"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field(output_processor=Compose(lambda v: v[0]))
    email = Field(output_processor=Compose(lambda v: v[3]))
    phone_number = Field(output_processor=Compose(lambda v: v[2]))
