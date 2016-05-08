#coding:utf-8

'''
about:爬取知乎上Python话题下的999个精华问题，通过提取关键词分析。比如爬虫啊，学习书籍，博客，项目，web开发，
        希望可以将不同关键词下的回答保存为一个文档中。最后肯定是要存在数据库中。
time:2016.04.27
@author:Ben
'''

import urllib2
from BeautifulSoup import BeautifulSoup

#转码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#保存文件
file = open('ZhihuPython.txt','w')

url = "http://www.zhihu.com"
#精华问题有50页
for pagenum in range(1,51):
    strpagenum = str(pagenum)
    print "Getting data for Page " + strpagenum
    start_urls = "http://www.zhihu.com/topic/19552832/top-answers?page="+strpagenum  #网址
    page = urllib2.urlopen(start_urls)     #打开网页
    soup = BeautifulSoup(page)

    #首先爬取所有的问题和回答的链接
    question = soup.findAll("a",attrs={'class':['question_link']})
    for each in question:
        file.write("问题: ")
        file.write(each.string)
        file.write("\n")
        answer = each.get('href')
        answer_url = url + answer
        file.write("问题链接：")
        file.writelines(answer_url)
        file.write("\n")
        # #根据问题链接爬取相应内容
        # answer_page = urllib2.urlopen(answer_url)
        # answer_soup = BeautifulSoup(answer_page)
        # vote = answer_soup.findAll(attrs={'class':['zm-votebar goog-scrollfloater']})
        # print vote

    #减慢爬取速度
    download_delay = 1








