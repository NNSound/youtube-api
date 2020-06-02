# youtube-api  

I'm trying to use youtube-dl and youtube-api to do this crawler.  
(Yes, it is a crawler)  
It can get the list from kkbox and hito, then use those word to search youtube video(use youtube-api)  
這個專案使用了youtube-dl 的套件, 與youtube 提供的api 來實做網路爬蟲, 算是整合別人的api ,只有音樂網站爬蟲的部份是自己寫的, 相關文件可以參考上面的連結。  

**Start this project:**  
pip install -r requirement.txt  
or  
pip3 install -r requirement.txt  

And you need a key to use Google Cloud Platform  
Docs  
https://cloud.google.com/docs/authentication/api-keys  
For simply step:  
https://console.cloud.google.com/apis/credentials  

1. Login your Google Cloud Platform.
2. Create a API key.
3. make a json file name config.json and paste your key.  
```
{
    "key" : "paste your key here"
}
```
And that all.  

Example:  
https://github.com/NNSound/youtube-api/blob/master/demo.py
```
import requests
import json
YorKey = ""              #Put your API key here
WhatYouWantToSearch = "" #Put what you want to search
url = 'https://www.googleapis.com/youtube/v3/search'
dic = {'part':'snippet', 'key':YorKey, 'type':'video', 'q':WhatYouWantToSearch, 'order':'viewCount', 'maxResults':1}
r = requests.get(url, params=dic)
print(r.text)
#And you would get the info json
```
How to run demo:  
```
python demo.py
```
or  
```
python3 demo.py
```

Docs:
https://developers.google.com/youtube/v3/getting-started


You don't need to do this(it only my note):  
sudo apt install python-pyqt5
pip install mu-editor
sudo apt install pacman  

TODO:  
進行各種操作的時候要寫log  
GUI視窗界面  
根據音樂類型區分資料夾  

sudo apt-get install ffmpeg