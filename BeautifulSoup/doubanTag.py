#!/usr/bin/env python
# encoding: utf-8

import time
import requests
from bs4 import BeautifulSoup
import random

# 把str编码由ascii改为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#建立文件
file_name = 'book_List.txt'
file_content = ''
file_content += '生成时间：' + time.asctime()

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]

def book_spider(book_tag):
    global file_content, headers

    url = "http://www.douban.com/tag/%s/book" % book_tag

    source_code = requests.get(url, headers=random.choice(headers))

    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    title_divide = '\n' + '*' * 50 + '\n'
    file_content += title_divide + '\t' * 4 + \
        book_tag + '：' + title_divide
    count = 1

    # 得到书籍列表的soup对象
    list_soup = soup.find('div', {'class': 'mod book-list'})
    for book_info in list_soup.findAll('dd'):
        print 'tag: %s, count: %d' % (book_tag, count)
        title = book_info.find('a', {'class': 'title'}).string.strip()
        desc = book_info.find('div', {'class': 'desc'}).string.strip()
        desc_list = desc.split('/')
        author_info = '作者/译者： ' + '/'.join(desc_list[0:-3])
        pub_info = '出版信息： ' + '/'.join(desc_list[-3:])
        try:
            rating = book_info.find('span', {'class': 'rating_nums'}).string.strip()
        except AttributeError:
            rating = "无"
        file_content += "%d\t《%s》\t评分：%s\n\t%s\n\t%s\n\n" % (
            count, title, rating, author_info.strip(), pub_info.strip())
        count += 1


def do_spider(book_lists):
    for book_tag in book_lists:
        book_spider(book_tag)

if __name__ == "__main__":
    book_lists = ['巴黎','吃货','街拍','发型','美女','护肤','化妆','猫','健身']
    do_spider(book_lists)

    # 将最终结果写入文件
    f = open(file_name, 'w')
    f.write(file_content)
    f.close()