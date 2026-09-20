# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from os import name
import scrapy
import scrapy.item

class DefenseItem(scrapy.Item):
    id = scrapy.Field()
    status = scrapy.Field()
    values = scrapy.Field()
    publications = scrapy.Field()
    rada = scrapy.Field()


class DisItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    university = scrapy.Field()
    date = scrapy.Field()


class TopicItem(scrapy.Item):
    topic = scrapy.Field()
    topic_url = scrapy.Field()


class DynamicItem(scrapy.Item):
    # define the fields for your item here like:
    #  name = scrapy.Field()
    # url = scrapy.Field()
    # file_urls = scrapy.Field()
    # image_urls = scrapy.Field()

    # price = scrapy.Field()
    # text = scrapy.Field()
    # location = scrapy.Field()
    # date = scrapy.Field()
    # year = scrapy.Field()
    # run = scrapy.Field()

    name = scrapy.Field()
    shop = scrapy.Field()
    city = scrapy.Field()
    price = scrapy.Field()
