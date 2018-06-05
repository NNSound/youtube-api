# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pafy
import os


mysong =[]
looks =[]
hrefs =[]
youtubeURL =[]
def getArrMysongs():
    return mysong
def getArrLooks():
    return looks
def getArrHrefs():
    return hrefs
def getArrYoutubeURL():
    return youtubeURL

def strclear(s=''):
    if '(' in s:  #去除一些不必要的字串
        s = s[0:s.index('(')]
    if '-' in s:  #去除一些不必要的字串
        s = s[0:s.index('-')]
    if '"' in s:  #去除一些不必要的字串
        s = s[0:s.index('"')]
    return s
def printissue(Artist,song):
    print ("Artist:",Artist)
    print ("song:",song)
def search_hot(songs):
    url_look = 'https://www.youtube.com/results?search_query='
    err = []
    for name in songs:#直接從全域變數拿資料
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
            self.download()
        except:
            print ("error:something wrong in search_hot")
            err.append(name)
            looks.append("")
            hrefs.append("")
            continue
    looks.append(max(arr))
    hrefs.append(url_song)


def download():
    #下載音樂
    for name in getArrMysongs():
        video = pafy.new(url_song)
        best = video.getbestaudio(preftype="m4a")
        directory = "2017/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        best.download(filepath=directory+name+".m4a",meta=True, quiet=True)
        print("download success")
