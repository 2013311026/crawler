# -*- coding: utf-8 -*-

'''
time:2016.04.07
author:Ben
about:关于百度贴吧的一个爬虫，使用XPath+多线程
目标网站：http://tieba.baidu.com/p/3522395718
目标内容：爬取跟帖用户名，跟帖内容以及跟帖时间
使用Request获取网页
使用Xpath提取内容
使用map实现多线程爬虫
'''

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import time

#转码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def towrite(contentdict):
    f.writelines(u'回帖时间：' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容：' + unicode(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人：' + contentdict['user_name'] + '\n\n')

def spider(url):
    html = requests.get(url)
    #使用requests得到一个页面的源码，进而进行相应的解析
    selector = etree.HTML(html.text)
    #print selector
    #得到一个页面不同的回帖列表
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    #print content_field
    #将得到的内容存入字典
    item = {}
    for each in content_field:
        #使用json.loads将json格式的文件解析成字典格式
        reply_info = json.loads(each.xpath('@data-field')[0])
        author = reply_info['author']['user_name']
        #content = each.xpath('div[@class="d_post_content_main"]/div/cc/div/text()')[0].replace(' ','')
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div/text()')
        reply_time = reply_info['content']['date']
        print content
        print reply_time
        print author

        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time

        towrite(item)

if __name__ == '__main__':
    f = open('baidutiebaContent.txt','a')
    page = []
    for i in range(1,2):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)
    pool = ThreadPool(8)
    time1 = time.time()
    results = pool.map(spider,page)
    pool.close()
    pool.join()
    time2 = time.time()
    print u'总共用时：' + str(time2 - time1)
    f.close()



























