# -*- coding: utf-8 -*-

'''
time:2016.0508
about:爬取拉勾上所有的职位信息
author:ben
'''

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class CrawldetailsItem(Item):
    kd = Field()
    title = Field()
    description = Field()
    tag = Field()
    company = Field()
    city = Field()
    salary = Field()
    experience = Field()
    education = Field()
    url = Field()
    address = Field()
    industry = Field()
    scale = Field()
    phase = Field()
    published = Field()
