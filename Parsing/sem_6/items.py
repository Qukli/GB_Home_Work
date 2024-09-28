# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyimageItem(scrapy.Item):
    img_url = scrapy.Field()
    img_folder = scrapy.Field()
    img_name = scrapy.Field()
    img_category = scrapy.Field()

