#coding:utf-8

import scrapy

class LagouPositionSpider(scrapy.Spider):
    name = "lagouposition"
    start_urls = (
        'http://www.lagou.com/zhaopin//',
    )

    def parse(self,response):
        print response.body

