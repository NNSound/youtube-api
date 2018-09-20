#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import re
import sqlite3
import sys
import datetime

import pafy
import requests
import youtube_dl
from bs4 import BeautifulSoup

#reload(sys)
#sys.setdefaultencoding('utf-8')

mysong =[]
def getKey():
    with open('config.json') as f:
        data = json.load(f)
    return data['key']

def getArrMysongs():
    return mysong

def strclear(s=''):
    s = re.sub('\/|\(.*\)|\[.*\]', '', s)
    if '-' in s:  #去除一些不必要的字串
        s = s[0:s.index('-')]
    if '"' in s:  #去除一些不必要的字串
        s = s[0:s.index('"')]
    s = s.rstrip()
    s = s.lstrip()
    return s
def printissue():
    for row in mysong:
        print("\nArtist:"+row[0],"\nSong:"+row[1])

def getLastThursday():
    current_time = datetime.datetime.now()
    last_thursday = (current_time.date()
    - datetime.timedelta(days=current_time.weekday())
    + datetime.timedelta(days=3, weeks=-1))
    return last_thursday.strftime("%Y-%m-%d")

# 根據關鍵字搜尋影片,
# @param string key, Youtube Key
# @param string q, 搜尋關鍵字
# @return string videoId, 影片ID
def search_hot(key,q):
    url = 'https://www.googleapis.com/youtube/v3/search'
    dic = {'part':'snippet','key':key,'type':'video','q':q,'order':'viewCount','maxResults':1}
    r = requests.get(url,params=dic)
    json_data = json.loads(r.text)
    videoId = json_data['items'][0]['id']['videoId']
    return videoId

def download_v2(videoID,artist,name):
    url = 'https://www.youtube.com/watch?v='+str(videoID)
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%Y-%m-%d")
    #TODO 根據曲風分配資料夾
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': "./music/"+current_time+'/'+artist+" - "+name+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
#outtmpl
