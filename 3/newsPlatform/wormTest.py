#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import time
import sys

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","newsPlatform.settings")

import django
django.setup()

from newsApp.models import news

def parse(idStr):
        global html,bsObj
        html = urlopen("http://cs.whu.edu.cn/news_show.aspx?id="+idStr)
        bsObj = BeautifulSoup(html, "html.parser")


def parsePage(idStr):

        # get type
        try:
                parse(idStr)
                pageType = typeDic[bsObj.find("div", {"class": "title"}).get_text()]
        except:
                print("该页面不存在！")
                return

        # get time
        parse(idStr)
        dateListPre = re.findall("[0-9]+", bsObj.find("div", {"class": "info"}).find("span").get_text())
        dateListNow = [int(x) for x in dateListPre]
        #pageTime = time.mktime(datetime.datetime(dateListNow[0], dateListNow[1], dateListNow[2]).timetuple())
        pageTime= time.strftime('%Y-%m-%d',datetime.datetime(dateListNow[0], dateListNow[1], dateListNow[2]).timetuple())

        # get title
        parse(idStr)
        pageTitle = bsObj.find("div", {"class": "sp1"}).get_text()

        # get content
        parse(idStr)
        for divTag in bsObj.find("div", {"class": "sp2"}).next_siblings:
                try:
                        rawContent = divTag.get_text()
                        pageContent = "".join(rawContent.split())
                except:
                        pass

        #infoList.append({"id": int(idStr), "type": pageType, "time": pageTime, "title": pageTitle, "content": pageContent, })
        news.objects.create(type=pageType,date=pageTime,title=pageTitle,content=pageContent)

messageType=0
typeDic={"学院通知":"1","公示公告":"2","学院新闻":"3","学术讲座":"4"}
infoList=[]
for id in range(1200):
        parsePage(str(id))
        time.sleep(1)
#print(infoList)
