# -*- coding: utf-8 -*-
import scrapy
import json
from positionInfo.items import PositionInfoItem
import os

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class LagoupositonSpider(scrapy.Spider):
    name = "LagouPositon"

    totalPageCount = 0
    curpage = 1
    cur = 0

    keywords = [json.loads(line) for line in open(basedir + '/data/KeyWords.json')]
    myurl = "http://www.lagou.com/jobs/positionAjax.json?"

    kds = keywords[0][u'技术'][0]

    kd = kds[0]

    def start_requests(self):
        return [scrapy.http.FormRequest(self.myurl,
                                        formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]

    def parse(self, response):

        item = PositionInfoItem()
        jdict = json.loads(response.body)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        self.totalPageCount = jposresult['totalCount'] /15 + 1

        for each in jresult:
            item['city']=each['city']
            item['companyName'] = each['companyName']
            item['companySize'] = each['companySize']
            item['positionName'] = each['positionName']
            item['positionType'] = each['positionType']
            sal = each['salary']
            sal = sal.split('-')
            print sal
            if len(sal) == 1:
                item['salaryMax'] = int(sal[0][:sal[0].find('k')])
            else:
                item['salaryMax'] = int(sal[1][:sal[1].find('k')])
            item['salaryMin'] = int(sal[0][:sal[0].find('k')])
            item['positionAdvantage'] = each['positionAdvantage']
            item['companyLabelList'] = each['companyLabelList']
            item['formatCreatetime'] = each['formatCreateTime']
            item['keyword'] = self.kd
            yield item
        if self.curpage <= self.totalPageCount:
            self.curpage += 1
            yield scrapy.http.FormRequest(self.myurl,
                                        formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
        elif self.cur < len(self.kds)-1:
            self.curpage = 1
            self.totalPageCount = 0
            self.cur += 1
            self.kd = self.kds[self.cur]
            yield scrapy.http.FormRequest(self.myurl,
                                        formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)

