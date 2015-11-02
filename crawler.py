##-*- coding: utf-8 -*-
# encoding=utf8  
import sys
reload(sys)
from config import *

import re
import urllib
import urllib2
from bs4 import BeautifulSoup
from ghost import Ghost
import json
import base64
import datetime
# ghost = Ghost()

# url =  'http://mp.weixin.qq.com/s?__biz=MzA4NDU4Nzc2Ng==&mid=400136635&idx=1&sn=6ada0f67d9281876b077d7e26927bba5&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MjM5NjMzNzUwMQ==&mid=206134286&idx=1&sn=98bb144aa4421e81ba9209ed25b90ad9&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MjM5NjMzNzUwMQ==&mid=200472739&idx=1&sn=f34a1d001475152ad32267ee02272523&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MjM5MTIzNjU2Mg==&mid=400037532&idx=1&sn=1ca110c25f36f98fd2e157a03ac2e233&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MzA4MzkyODYyNw==&mid=400153507&idx=3&sn=a0fdb10ad5e86b0017d091c12a139837&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MzAwNTUyNzYzNQ==&mid=400154568&idx=1&sn=20f9bcf04065f5c505daf24943f8d41e&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
# url = 'http://mp.weixin.qq.com/s?__biz=MjM5OTQ0MjM4MA==&mid=400121554&idx=3&sn=db7cb95e6ff274eae5ac9eb048599286&3rd=MzA3MDU4NTYzMw==&scene=6#rd'
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    # soup = BeautifulSoup(html).find_all("div", attrs={"class":"wx-rb bg-blue wx-rb_v1 _item"}, limit=1)[0]["href"]
    # print host + soup[5:]
    # with ghost.start() as session:
    #     page, extra_resources = session.open(host + soup)
    #     assert page.http_status == 200
    #     page,resources = ghost.open(host + soup)
    #     html = page.read()
    #     page.close()
    #     return html
    # page = urllib.urlopen(host + soup[5:])
    # html = page.read()
    # page.close()
    return html

# def innerHTML(element):
    # return 
    # innerhtml = element.decode_contents(formatter="html")
    # innerhtml = "".join([str(x) for x in element.contents])
    # return innerhtml

def getTitle(html):
    # soup = BeautifulSoup(html).find_all("h4", attrs={"class":"news_lst_tab zhz"})
    return html     
def parse(text):
    if (hasKeywords(text)):
        time = ''
        addr = ''
        try:
            m = re.search(u"时间[^\u4e00-\u9fa5\d]*(\d{4}年)?(\d{1,2}月\d{2}日)", text.decode('utf8'))
            if (m == None):
                m = re.search(u"(\d{4}年)?(\d{1,2}月\d{1,2}日\s*\d{2}[:：]\d{2}.{0,2}\d{2}[:：]\d{2})", text.decode('utf8'))
            time = m.group(2)
        except Exception , e:
            print(e)
        try:
            m =  re.search(u"地[点址][^\u4e00-\u9fa5]{0,3}([\u4e00-\u9fa5]{4,10})", text.decode('utf8'))
            addr = m.group(1)
        except Exception , e:
            print(e)
        return (time, addr)
    return ["",""]

def hasKeywords(text):
    key_words_first_class = ["路演"]
    for key in key_words_first_class:
        if (text.find(key) != -1) :
            # print "found keyword " + key
            return True
    key_words_second_class = ["项目", "投资人"]
    for key in key_words_second_class:
        if (text.find(key) == -1) :
            print "no keyword found : " + key
            return False
    return True
def doRun(url):
    sys.setdefaultencoding('utf8')
    html = getHtml(url)
    # print html
    # print getTitle(html)
    # print innerHTML(BeautifulSoup(html))
    html = BeautifulSoup(html,"html.parser")
    title = html.title.text
    [x.extract() for x in html.body.find_all('script')]
    # print html.body.text
    (a,b) = parse(html.body.text)

    if (a != "" or b != ""):
        rel = {}
        rel['time'] = a
        rel['addr'] = b
        rel['title'] = title
        rel['href'] = url
        requrl = "http://119.254.100.198:4502/content/wx/*"
        data = json.dumps(rel,ensure_ascii=False)

        data = urllib.urlencode(rel)
        print data
        req = urllib2.Request(url = requrl,data = data)
        base64string = base64.encodestring('%s:%s' % ('admin', 'admin'))[:-1]
        authheader = "Basic %s" % base64string
        req.add_header("Authorization", authheader)
        # req.add_header("content-type", 'text/html;charset=UTF-8')
        resp = urllib2.urlopen(req)
        print json.dumps(rel,ensure_ascii=False)
    else:
        print 'no found'

def run():
    urls = getLinks()
    for url in urls:
        doRun(url)
        
def getLinks():
    i = datetime.datetime.now()
    fname = './js/data/' + str(i.year) + '-' + str(i.month) + '-' + str(i.day) + '.txt'
    content = open(fname).read().split(',')
    return content



