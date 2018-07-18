# from __future__ import unicode_literals
#!/usr/bin/python3

import requests
import json
import youtube_dl

#url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCPcF3KTqhD67ADkukx_OeDg&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc'
url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc&type=video&q=于文文 體面&order=viewCount&maxResults=1'
#sg_WE0ToJjM

r = requests.get(url)
json_data = json.loads(r.text)
videoId = json_data['items'][0]['id']['videoId']
print (videoId)

url = 'https://www.youtube.com/watch?v='+videoId
url2 = 'https://www.youtube.com/watch?v=zOEISgh7k_g'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])