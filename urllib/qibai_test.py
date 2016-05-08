#coding:utf-8

'''
3.19 20.27
爬虫实现一页保存点赞数
'''

import urllib
import urllib2
import re
import time


#生成文件
file_name = 'qiubaiSpider1.txt'
file_content = ''
# 最终要写到文件里的内容
file_content += '生成时间：' + time.asctime()
title_divide = '\n' + '--' * 5 + '\n'

# 把str编码由ascii改为utf8（或gb18030）
import sys
reload(sys)
sys.setdefaultencoding('utf8')

myUrl = "http://m.qiushibaike.com/hot/page/1"
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101'
headers = {'User-Agent' : user_agent}
req = urllib2.Request(myUrl, headers = headers)
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()
#编码
unicodePage = myPage.decode("utf-8")

myItems = re.findall('<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',unicodePage,re.S)
# vote = re.findall('<i class="number">(.*?)</i>',unicodePage,re.S)
# print vote
# name = re.findall('<h2>(.*?)</h2>',unicodePage,re.S)
# print name

for item in myItems:
    file_content += title_divide + '作者:' + item[0] + '\t' + '点赞数:' + item[2] + item[1]

if __name__ == "__main__":

    # 将最终结果写入文件
    f = open(file_name, 'w')
    f.write(file_content)
    f.close()

