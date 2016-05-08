# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class ZhihupythonItem(Item):

    Question = Field()
    Answer = Field()
    Author = Field()
    vote = Field()
