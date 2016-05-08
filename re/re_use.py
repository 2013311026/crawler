#coding:utf-8

'''
使用re模块实现简单的文本抓取
要合理的使用findall方法和search方法：
在确定抓取的内容只有一个时，使用search
'''

#导入re库文件
import re


f = open('qiubaiSpider1.txt'','r')
html = f.read()
f.close()

#爬取标题
# title = re.search('<title>(.*?)</title>',html,re.S).group(1)
# print title

#爬取链接
# links = re.findall('href="(.*?)"',html,re.S)
# for each in links:
#     print each

#抓取部分文字,先大再小
# text_fied = re.findall('<ul>(.*?)</ul>',html,re.S)[0]
# the_text = re.findall('">(.*?)</a>',text_fied,re.S)
# for every_text in the_text:
#     print every_text

#sub实现翻页
for i in range(2,total_page+1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print new_link

