#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
# from PyQt4.QtGui import QApplication
import requests
from bs4 import BeautifulSoup
import json
from datetime import *
import pprint
import pafy
import os
from mypackage import Base


#唯一JSON檔案，告知各種語言歌曲之 category_id 下方會GET['category']之編號
#url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang=tc&terr=tw&type=song'

class kkbox(object):
    yesterday = datetime.now() - timedelta(days=1)# 昨天
    date = yesterday.strftime('20%y-%m-%d')
    def __init__(self):
        self.mysongs = Base.getArrMysongs()

    def daily(self,day=date,category_id=297):
        #華語=297,西洋=390
        # cid = str(category_id)
        url = 'https://kma.kkbox.com/charts/api/v1/daily'
        dic = {'date':day,'type':'song','category':category_id,'lang':'tc','limit':50,'terr':'tw'}
        res = requests.get(url,params=dic)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts']['song']
        for song in songs:
            self.mysongs.append([Base.strclear(song['artist_name']),Base.strclear(song['song_name'])])
        Base.printissue()

    def weekly(self,yesterday=yesterday,cid=297,t="song"):#周四更新榜單
        yesterday_weekday = int(yesterday.strftime('%w')) #昨天星期幾
        while yesterday_weekday !=4:
            yesterday = yesterday - timedelta(days=1)
            yesterday_weekday = int(yesterday.strftime('%w'))
            date = yesterday.strftime('20%y-%m-%d')
        # self.date = str(date)
        # self.cid = str(cid) #華語=297,西洋=390
        # self.type = t  #新歌:newrelease 、 單曲 song
        #https://kma.kkbox.com/charts/api/v1/weekly?category=297&date=2018-03-08&lang=tc&limit=50&terr=tw&type=newrelease 每周新歌榜單
        #一樣由上面的網址決定，榜單只存兩周，category_id type有 新歌:newrelease ， 單曲 song
        url = 'https://kma.kkbox.com/charts/api/v1/weekly'
        dic = {'date':date,'type':t,'category':cid,'lang':'tc','limit':50,'terr':'tw'}
        res = requests.get(url,params=dic)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts'][t]
        for song in songs:
            self.mysongs.append([Base.strclear(song['artist_name']), Base.strclear(song['song_name'])])
            # self.mysongs[0].append()
            # self.mysongs[1].append()
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
    
if __name__ == '__main__':

    kk = kkbox()
    #kk.daily(date)
    kk.weekly()
    key = 'AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc'
    mylist = Base.getArrMysongs()
    for row in mylist:
        vid = Base.search_hot(key,row[0]+" "+row[1])
        Base.download_v2(vid,row[0],row[1])
    #kk.search_hot()
    # hh =hito()
    # hh.topyear()
    # Base.search_hot()
    # print(Base.getArrMysongs())
