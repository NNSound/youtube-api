#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
import json
# from __future__ import unicode_literals
import youtube_dl

#url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCPcF3KTqhD67ADkukx_OeDg&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc'
url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc&type=video&q=于文文 體面&order=viewCount&maxResults=1'


r = requests.get(url)
json_data = json.loads(r.text)
videoId = json_data['items'][0]['id']['videoId']
print (videoId)

url = 'https://www.youtube.com/watch?v='+videoId

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])