#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import pprint
import sys
from datetime import *

import re
import pafy
import requests
from bs4 import BeautifulSoup

from mypackage import Base
from mypackage.model import AllMusic

#url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang=tc&terr=tw&type=song'
#唯一JSON檔案，告知各種語言歌曲之 category_id 下方會GET['category']之編號

class kkbox(object):
    yesterday = datetime.now() - timedelta(days=1)# 昨天
    date = yesterday.strftime('20%y-%m-%d')
    def __init__(self):
        self.mysongs = Base.getArrMysongs()

        #華語=297,西洋=390
    def daily(self,day=None,cid=297):
        if (day == None):
            day = self.date
        url = 'https://kma.kkbox.com/charts/api/v1/daily'
        dic = {'date':day, 'type':'song', 'category':cid, 'lang':'tc', 'limit':50, 'terr':'tw'}
        res = requests.get(url,params=dic)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts']['song']
        for song in songs:
            self.mysongs.append([Base.strclear(song['artist_name']), Base.strclear(song['song_name'])])
        Base.printissue()

        #cid: 華語=297,西洋=390 
        #t: 新歌:newrelease 、 單曲 song
    def weekly(self,yesterday=yesterday,cid=297,t="song"):
        self.date = str(Base.getLastThursday())
        #https://kma.kkbox.com/charts/api/v1/weekly?category=297&date=2018-03-08&lang=tc&limit=50&terr=tw&type=newrelease 每周新歌榜單
        #一樣由上面的網址決定，榜單只存兩周
        url = 'https://kma.kkbox.com/charts/api/v1/weekly'
        dic = {'date':self.date, 'type':t, 'category':cid, 'lang':'tc', 'limit':50,'terr':'tw'}
        res = requests.get(url,params=dic)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts'][t]
        #TODO 要判斷是否存在元素
        for song in songs:
            self.mysongs.append([Base.strclear(song['artist_name']), Base.strclear(song['song_name'])])
        Base.printissue()


class hito(object):
    
    def __init__(self):
        self.mysongs = Base.getArrMysongs()
    def hitoweekly(self):
        url = "http://www.hitoradio.com/newweb/chart_1_1.php"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        chart_bottom = soup.find('div', 'chart_bottom')
        ul = chart_bottom.find('ul')
        lis = ul.find_all('li')
        for li in lis:
            td5 = li.find_all('td')
            print (td5[5].get_text())
    def topyear(self):
        for i in range(0,2):
            url = "http://www.hitoradio.com/newweb/chart_2.php?ch_year=2017&pageNum_rsList="+str(i)
            print (url)
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "lxml")
            content  = soup.find('div',id="content")
            
            table = content.find('tbody')
            songs = table.find_all('tr')
            for song in songs:
                line = song.find_all('td')
                print ("Artist:",line[3].get_text())
                print ("song:",line[1].get_text())            
                self.mysongs.append(line[3].get_text()+"+"+line[1].get_text())
        #Base.search_hot(self.mysongs)
        #print (song[0])

class mojim(object):
    def __init__(self):
        self.mysongs = Base.getArrMysongs()
    
    def getlist(self):
        url = "http://mojim.com/twzhot-song.htm"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        table  = soup.find('td',id="mx45_M").find('table')
        tagList = table.find_all('div')
        tagList.remove(tagList[7])
        for tag in tagList:
            songs = tag.find_all('td')
            for song in songs:
                item = song.find('a')
                artist = song.find('a', class_="X1")
                if item is not None:
                    item = re.split('[0-9]+\.', item.get_text())
                    artist = re.split('[<](.*)[>]', artist.get_text())
                    self.mysongs.append([Base.strclear(artist[1].strip()), Base.strclear(item[1])])
        Base.printissue()
    
# if __name__ == '__main__':

#     kk = kkbox()

#     kk.daily()
#     kk.weekly()#297華語
#     kk.weekly(cid=390)#西洋
#     kk.weekly(cid=324)
#     kk.weekly(cid=352)

#     key = Base.getKey()
#     model = AllMusic()
#     model.createtable()

#     mylist = Base.getArrMysongs()
#     for row in mylist:
#         vid = Base.search_hot(key,row[0]+" "+row[1])
#         sql = "video_id = '" + vid + "'"
#         model = AllMusic()
#         if (model.getOne(sql) == None):
#             model.artist = row[0]
#             model.song = row[1]
#             model.video_id = vid
#             model.is_download = 0
#             # Base.download_v2(vid,row[0],row[1])
#             model.is_download = 1
#             model.insert()
#         else:
#             print("Already has:"+row[0]+"-"+row[1])


if __name__ == '__main__':

    mm = mojim()
    mm.getlist()

    key = Base.getKey()
    mylist = Base.getArrMysongs()
    for row in mylist:

        try:
            vid = Base.search_hot(key,row[0]+" "+row[1])
            sql = "video_id = '" + vid + "'"
            model = AllMusic()
            if (model.getOne(sql) == None):
                model.artist = row[0]
                model.song = row[1]
                model.video_id = vid
                model.is_download = 0
                # Base.download_v2(vid,row[0],row[1])
                model.insert()
            else:
                print("Already has:"+row[0]+"-"+row[1])
        except:
            print("[Error]:%s - %s"%(row[0], row[1]))

        