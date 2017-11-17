#!/usr/bin/python
#-*-coding:utf-8 -*-
import requests
import time
import pymysql
from bs4 import BeautifulSoup
import pafy

global mysongs
global artists
global href
global hrefs
global looks
mysongs = []
artists = []
hrefs = []
looks = []
def search_top():
    url = "https://www.kkbox.com/tw/tc/charts/western-monthly-song-latest.html"
    #url = "https://www.kkbox.com/tw/tc/charts/hokkien-monthly-song-latest.html"#中文月榜
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')  #取得網頁原始碼
    articles = soup.find_all('div', 'item')
    #=====================================
    i = 0
    for article in articles:
        try:
            meta = article.find('a')  #取得article中的<a>標籤
            link = meta.get('title')  #取得meta得文字;歌名
            if '(' in link:  #去除一些不必要的字串
                link = link[0:link.index('(')]
            if '-' in link:  #去除一些不必要的字串
                link = link[0:link.index('-')]
            artist = article.find('span').getText()  #歌手
            if '(' in artist:  #去除一些不必要的字串
                artist = artist[0:artist.index('(')]
            if '-' in artist:  #去除一些不必要的字串
                artist = artist[0:artist.index('-')]            
        except:
            print ("something rong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continue  # 下次試試H4 H5 裡面的text           
        mysongs.append(link)
        artists.append(artist)
        print(i, mysongs[i], "\n<Artist>", artists[i])
        i += 1



def search_youtube():#this is the old method
    url_search_query = 'https://www.youtube.com/results?search_query='
   
    err = 0
    for name in mysongs:  #直接從全域變數拿資料
        url_find = url_search_query + name
        response = requests.get(url_find)
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            div_stan = soup.find('div', "yt-lockup-content")
            href = div_stan.a.get('href')
            url_song = 'https://www.youtube.com' + href
            print("Key word:", name, "\n", url_song)
            hrefs.append(url_song)
        except:
            print("*********coultn't find url*********")
            hrefs.append("")
            err += 1
    print("error time:", err)
def search_hot():
    url_look = 'https://www.youtube.com/results?search_query='
    err = []
    for name in mysongs:  #直接從全域變數拿資料
        try:
            url_find = url_look + name
            response = requests.get(url_find)
            soup = BeautifulSoup(response.text, 'lxml')
            div_lockup = soup.find_all('div', "yt-lockup-content")#查找所有觀看紀錄
        except:
            print ("*********soup error*********")
            err.append(name)
            continue
        arr = []
        try:
            hot_music = 0
            for i in range(0, 3):
                li=div_lockup[i].a.get('href')
                myvid = pafy.new("http://www.youtube.com"+li)                
                times = myvid.viewcount
                arr.append(times)
            hot_music = arr.index(max(arr))
            looks.append(max(arr))
        except:
            print ("*********hot_music error*********")
            print("Key word:", name,)
            err.append(name)
            continue
        try:
            div_stan = soup.find_all(
                'div', "yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix")
            href = div_stan[hot_music].a.get('href')
            url_song = 'https://www.youtube.com' + href
            print("Key word:", name, "\nLook:", max(arr), "\n","hot index:",hot_music, url_song)
            hrefs.append(url_song)
        except:   
            print ("*********get href error*********")
            err.append(name)
    print("error time:",len(err))
    print (err)


def ins_db():
    err = []
    try:
        conn = pymysql.connect(
                host="myfirstdb.cmuovhawvgvz.us-west-2.rds.amazonaws.com",
                port=3306,
                db="test",
                user="nn",
                passwd="wl01994570",
                charset='utf8' 
                )
        cur = conn.cursor()
    except:
        err.append("db fail")
    i = 0
    for line in mysongs:
        try:
            sql = "SELECT * FROM `english_song` WHERE `url` LIKE %s"
            if cur.execute(sql,(hrefs[i])):  #有找到東西 =1
                print("Already have this song")
                print(mysongs[i], artists[i], hrefs[i])
            elif hrefs[i] is "":  # cur.execute(sql)=0
                print("did not have url")
            else:  # cur.execute(sql)=0, hrefs[i] is not null
                sql = 'INSERT INTO `english_song` (`song`, `artist`, `Look`, `origin`, `url`, `download_time`)VALUES (%s, %s,%s, %s,%s, CURRENT_TIMESTAMP);'
                print(cur.mogrify(sql,(mysongs[i], artists[i], looks[i], "KKBOX",  hrefs[i])))                
                cur.execute(sql,(mysongs[i], artists[i], looks[i], "KKBOX",  hrefs[i]))
                print("INSERT success")
                conn.commit()
        except:
            print("sql error")
            err.append("sql error")
        i += 1
    print("error time:", len(err),"\n",err)
    cur.close()


if __name__ == "__main__":
    search_top()
    search_hot()
    ins_db()
