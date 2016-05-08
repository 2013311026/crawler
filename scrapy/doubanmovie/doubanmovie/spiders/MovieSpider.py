#coding:utf-8

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
#导入Selector从而使用xpath
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem

class DoubanMovie(CrawlSpider):
    name = "doubanmovieSpider"
    redis_key = 'douban:start_urls'
    start_urls = ['http://movie.douban.com/top250']

    url = 'http://movie.douban.com/top250'

    def parse(self,response):
        item = DoubanmovieItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for eachmovie in movies:
            title = eachmovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in fullTitle:
                fullTitle += each

            movieInfo = eachmovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachmovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            quote = eachmovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''

            item['title'] = title
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote

            yield item

        nextlink = selector.xpath('//span[@class="next"]/link/@herf').extract()
        if nextlink:
            nextlink = nextlink[0]
            print nextlink
            #Request,并添加一个回调函数，类似递归的操作
            yield Request(self.url + nextlink,callback=self.parse)