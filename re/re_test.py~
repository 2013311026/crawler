#-*-coding:utf8-*-

'''
上学期对正则表达式有过了解，具体说来就是子啊爬虫的时候有过使用，
最近开始想好好的学习爬虫，scrapy框架想更好的使用，在此先将正则
继续练习掌握了。
python正则表达式中常用的组合是(.*?)
常用的方法有：findall,search,sub
'''

import re

#.的使用（可以匹配任意字符，换行符除外)
# a = 'abc123'
# b = re.findall('a..',a)
# print b

#re.S可以使得.匹配换行符
# a = '''whcdcnXXhello
#     XXjsksdXXnujsXXcjdk'''
# b = re.findall('XX(.*?)XX',a)
# print b
# c = re.findall('XX(.*?)XX',a,re.S)
# print c
#.*?非贪心算法，(.*?)是将括号中的内容作为结果输出

#*的使用（匹配钱一个字符0或无限次)
# a = 'ccdncdjc'
# b = re.findall('c*',a)
# print b

#？匹配前一个字符0或1次
# a = 'ccdncdc'
# b = re.findall('c?',a)
# print b

#.*的使用，贪心算法
# a = 'aabbaanbbcjdbbbcdcmkd'
# b = re.findall('bb.*bb',a)
# print b

#.*?的使用,非贪心算法
# a = 'aabbaanbbcjbbdbbbcdcmkd'
# b = re.findall('bb.*?bb',a)
# print b

#(.*?)的使用，将匹配到的括号中的结果输出
# a = 'aabbaanbbcjbbdbbbcdcmkd'
# b = re.findall('bb(.*?)bb',a)
# print b
# for item in b:
#     print item

#对比findall和search的区别，这两种方法得到的对象是不一样的
#对于search()方法而言，其后的group括号中的数字与正则匹配中的括号分组相对应
#这种情况下的findall得到的是一个列表，列表中的每一个元素相应的为元组形式
# s2 = 'asdfxxIxx123xxlovexxdfd'
# f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
# print f
# f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# print f2
# print f2[0][1]


#sub的使用举例(替换)
# s = '123rrrrr123'
# output = re.sub('123(.*?)123','123%d123'%789,s)
# print output


#匹配数字，使用\d
# a = 'asdfasf1234567fasd555fas'
# b = re.findall('(\d+)',a)
# print b