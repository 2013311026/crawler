#coding:utf-8

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
#导入Selector从而使用xpath
from scrapy.selector import Selector
from ZhihuPython.items import ZhihupythonItem

class PythonSpider(CrawlSpider):
    name = 'ZhihuPythonSpider'
    allowed_domains = ["http://www.zhihu.com"]
    redis_key = 'zhihu:start_urls'
    start_urls = ['http://www.zhihu.com/topic/19552832/top-answers?page=']
    url = 'http://www.zhihu.com/topic/19552832/top-answers?page='

    def parse(self, response):
        item = ZhihupythonItem()
        #selector = Selector(response)
        question_Field = response.xpath('//div[@class="feed-main"]')
        for each in question_Field:
            question = each.xpath('div[@class="content"]/h2/a/text()')
            print question
            item['Question'] = question
            yield item


