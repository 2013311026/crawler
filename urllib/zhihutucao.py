#coding:utf-8

import urllib2
from BeautifulSoup import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


f = open('ZhiHuTuCao.txt','w')

for pagenum in range(1,21):
    strpagenum = str(pagenum)
    print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
    url = "http://www.zhihu.com/collection/27109279?page="+strpagenum  #网址
    page = urllib2.urlopen(url)     #打开网页
    soup = BeautifulSoup(page)      #用BeautifulSoup解析网页

    #找到所有的问题和回答
    content_Field = soup.findAll(attrs = {'class' : ['zm-item-title','zh-summary summary clearfix'] })
    for each in content_Field:
        if each.name == 'h2':
            print each.a.string     #问题中还有一个<a..>，所以要each.a.string取出内容
            if each.a.string:       #如果非空，才能写入
                f.write(each.a.string)
            else:
                f.write("No Answer")
        else:
            print each.string
            if each.string:
                f.write(each.string)
            else:
                f.write("No Answer")
f.close()                           #关闭文件

