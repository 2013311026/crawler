---
title: Xpath学习
date: 2016-04-23 12:47:27
tags: 爬虫
---
学习使用XPath，总结Xpath的常见应用。

以上是摘要
<!--more-->
以下是余下全文

Xpath是在XML文档中查找信息的语言。
## Xpath节点
Xpath中，有七种类型的节点：元素，属性，文本，命名空间，注释及文档节点（根节点）。

## XPath语法
使用路径或者步来选取节点。

| 路径表达式       | 结果          |
| ------------ |:-------------:|
| nodename  | 选取此节点的所有子节点|
| /   | 从根节点选取     |  
| //	 | 从匹配的当前节点选择文档的节点，不考虑它们的位置|
| .    |   选取当前节点|
|.. | 选取当前节点的父节点|
|@  |选取属性

### 选取未知节点
| 路径表达式       | 结果          |
| ------------ |:-------------:|
|*    |   匹配任何元素节点|
|@*  |匹配任何属性节点|
|node()|匹配任何类型的节点|

在路径表达式中通过使用"|"运算符，选取若干个路径。

### 练习
如下的XML代码：
```html
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
| 路径表达式       | 结果          |
| ------------ |:-------------:|
| bookstore | 选取bookstore的所有子节点|
| /bookstore  | 选取根元素bookstore     | 
| bookstore/book| 选取属于bookstore的子元素中的所有book元素| 
| //book	 | 选取所有的book子元素，而不考虑它们的位置|
| bookstore//book    |  选取属于bookstore元素的后代中所有的book元素，不管它位于bookstore中的什么位置|
|@lang|选取所有的lang属性|
|/bookstore/book[1]|选取属于bookstore子元素中的第一个book元素|
|/bookstore/book[last()]|选取属于bookstore子元素中的最后一个book元素|
|/bookstore/book[last()-1]|选取属于bookstore子元素中的倒数第二个book元素|
|/bookstore/book[position()<3]|选取最前面的两个属于bookstore子元素中的book元素|
|//title[@lang]|选取所有所有属性为lang的title元素|
|//title[@lang='eng']|选取所有的拥有eng的lang属性的title元素|
|/bookstore/book[price>35.00]|选取bookstore的所有price元素大于35的book属性|
|/bookstore/book[price>35.00]/title|选取bookstore中的book元素的所有title元素，且其中的price元素值大于35|
|/bookstore/*   |选取bookstore元素的所有子元素|
|//*    |选取文档中的所有元素|
|//title[@*]|选取所有带属性的title元素|
|//book/title | //book/price] 选取book元素的所有title和price元素|

## XPath的轴
轴可以定义相对于当前节点的节点集

| 轴名称       | 结果          |
| ------------ |:-------------:|
|ancestor|选取当前节点的先辈|
|ancestor-or-self|选取当前节点的所有先辈以及当前节点本身|
|attribute|选取当前节点的所有属性|
|child|选取当前节点的所有子元素|
|descendant|选取当前节点的所有后代元素|
|descendant-or-self|选取当前节点的所有后代元素以及当前节点的本身|
|following|选取文档中当前节点的结束标签之后的所有节点|
|namespace|选取当前节点的所有命名空间|
|parent|选取当前节点的父节点|
|preceding|选取文档中当前节点的开始标签之前的所有节点|
|preceding-sibling|选取当前节点之前的所有同级节点|
|self|选取当前节点|

## XPath运算符
Xpath表达式中的运算符

| 运算符      | 描述        |实例    |结果
| ------------ |:-------------:|:-------------:|:-------------:|
|div|除法|8 div 4|2|
|mod|计算除法的余数|5 mod 2|1|




