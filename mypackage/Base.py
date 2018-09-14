#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pafy
import os
import re
import json
import youtube_dl
import sys
import sqlite3

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
    return s
def printissue():
    for row in mysong:
        print("\nArtist:"+row[0],"\nSong:"+row[1])

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
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': "./music0914/"+artist+" - "+name+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
#outtmpl