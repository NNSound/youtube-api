#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import youtube_dl
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

#url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCPcF3KTqhD67ADkukx_OeDg&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc'
url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc&type=video&q=體面&order=viewCount&maxResults=1'
#sg_WE0ToJjM

r = requests.get(url)
json_data = json.loads(r.text)
videoId = json_data['items'][0]['id']['videoId']
print (videoId)

url = 'https://www.youtube.com/watch?v='+videoId
url2 = 'https://www.youtube.com/watch?v=zOEISgh7k_g'

artist = "于文文 - "
name = "體面"
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': artist+name+'.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])