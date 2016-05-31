# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class PositionInfoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = Field()
    companyName = Field()
    companySize = Field()
    positionName = Field()
    salaryMax = Field()
    salaryMin = Field()
    positionType = Field()
    positionAdvantage = Field()
    companyLabelList = Field()
    keyword = Field()
    formatCreatetime = Field()

