
import sys
# from PyQt4.QtGui import QApplication
import requests
from bs4 import BeautifulSoup
import json
from datetime import *
import pprint
import pafy
import os

#唯一JSON檔案，告知各種語言歌曲之 category_id 下方會GET['category']之編號
#url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang=tc&terr=tw&type=song'

class kkbox(object):
    yesterday = datetime.now() - timedelta(days=1)# 昨天
    date = yesterday.strftime('20%y-%m-%d')
    def __init__(self):
        self.mysongs = []
        self.looks = []
        self.hrefs = []
        
    def daily(self,day,category_id=297):
        #華語=297,西洋=390
        cid = str(category_id)
        url = 'https://kma.kkbox.com/charts/api/v1/daily?category='+cid+'&date='+day+'&lang=tc&limit=50&terr=tw&type=song'

        res = requests.get(url)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts']['song']
        for song in songs:
            self.mysongs.append(song['artist_name']+"+"+song['song_name'])
            print ("Artist:",song['artist_name'])
            print ("song:",song['song_name'])
    def weekly(self,yesterday=yesterday,cid=297,t="song"):#周四更新榜單
        yesterday_weekday = int(yesterday.strftime('%w')) #昨天星期幾
        
        while yesterday_weekday !=4:
            yesterday = yesterday - timedelta(days=1)
            yesterday_weekday = int(yesterday.strftime('%w'))
            date = yesterday.strftime('20%y-%m-%d')
        self.date = str(date)
        self.cid = str(cid) #華語=297,西洋=390
        self.type = t  #新歌:newrelease 、 單曲 song
        #https://kma.kkbox.com/charts/api/v1/weekly?category=297&date=2018-03-08&lang=tc&limit=50&terr=tw&type=newrelease 每周新歌榜單
        #一樣由上面的網址決定，榜單只存兩周，category_id type有 新歌:newrelease ， 單曲 song
        url = 'https://kma.kkbox.com/charts/api/v1/weekly?category=&date=&lang=tc&limit=50&terr=tw&type='
        dic = {'date':self.date,'type':self.type,'category':self.cid}
        res = requests.get(url,params=dic)
        stock_dict = json.loads(res.text)
        songs = stock_dict['data']['charts'][self.type]
        for song in songs:
            self.mysongs.append(song['artist_name']+"+"+song['song_name'])
            print ("Artist:",song['artist_name'])
            print ("song:",song['song_name'])
    def search_hot(self):
        url_look = 'https://www.youtube.com/results?search_query='
        err = []
        for name in self.mysongs:#直接從全域變數拿資料
            try:
                url_find = url_look + name
                response = requests.get(url_find)
                soup = BeautifulSoup(response.text, 'lxml')
                div_lockup = soup.find_all('div', "yt-lockup-content")#查找所有觀看紀錄
                arr = []
                hot_music = 0
                for i in range(0, 3):
                    li=div_lockup[i].a.get('href')
                    #print (li)
                    myvid = pafy.new("http://www.youtube.com"+li)
                    times = myvid.viewcount
                    arr.append(times)
                div_stan = soup.find_all(
                    'div', "yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix")
                href = div_stan[hot_music].a.get('href')
                url_song = 'https://www.youtube.com' + href
                print("Key word:", name, "\nLook:", max(arr), "\n","hot index:",hot_music, url_song)
                #下載音樂
                video = pafy.new(url_song)
                best = video.getbestaudio(preftype="m4a")
                directory = "music_0218E"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                best.download(filepath=directory, quiet=True)
                print("download success")
            except:
                print ("error:something wrong in search_hot")
                err.append(name)
                self.looks.append("")
                self.hrefs.append("")
                continue
        self.looks.append(max(arr))
        self.hrefs.append(url_song)



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
    def strclear(self,s):
        if '(' in s:  #去除一些不必要的字串
            s = s[0:link.index('(')]
        return s

    
if __name__ == '__main__':
    

    #yesterday = datetime.now() - timedelta(days=1)# 昨天
    
    #date = yesterday.strftime('20%y-%m-%d')
    
  
    kk = kkbox()
    kk.weekly(yesterday,cid=297)
    #kk.search_hot()
    #kk.hitoweekly()
    

