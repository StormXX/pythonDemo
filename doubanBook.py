# -*- coding: utf-8 -*-  
#---------------------------------------
#   程序：豆瓣图书相关API
#   版本：0.1
#   作者：南昌大学-网工111-廖肇兴-gintama
#   日期：2014-08-18
#   语言：Python 2.7
#   功能：豆瓣图书相关API使用
#---------------------------------------

import httplib2
import urllib
import json

class doubanBook:

    def __init__(self):
        self.bookname=''

    def getBookByISBN(self,isbn):
        conn=httplib2.Http()
        url='https://api.douban.com/v2/book/isbn/'+isbn
        (res,content)=conn.request(url)
        self.deal_json(content)

    def deal_json(self,jsonStr):
        jsonDic=json.loads(jsonStr)
        print jsonDic['title']


#-------- 程序入口处 ------------------
print u"""#---------------------------------------
#---------------------------------------
#   程序：豆瓣图书相关API
#   版本：0.1
#   作者：南昌大学-网工111-廖肇兴-gintama
#   日期：2014-08-18
#   语言：Python 2.7
#   功能：豆瓣图书相关API使用
#---------------------------------------
"""
print u'请输入13位ISBNS:'
isbn=raw_input()
d=doubanBook()
d.getBookByISBN(isbn)
