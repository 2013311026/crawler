# -*- coding: utf-8 -*-

#将得到的结果保存在mysql中

from scrapy import Item,Field

class Cnblog3Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    desc = Field()
    listUrl = Field()
