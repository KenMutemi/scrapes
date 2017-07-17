# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Businesses, db_connect, create_businesses_table


class ScrapesPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """

        engine = db_connect()
        create_businesses_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save businesses in database.

        This method is called for every item component.
        """
        session = self.Session()
        business = Businesses(**item)

        try:
            session.add(business)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
