# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmethystItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    identificador = scrapy.Field()
    tipo = scrapy.Field()
    poblacion = scrapy.Field()
    superficie = scrapy.Field()
    precio = scrapy.Field()
    compra = scrapy.Field()
    alquiler = scrapy.Field()
    web = scrapy.Field()
    last_update = scrapy.Field()
    maps = scrapy.Field()
    pass
