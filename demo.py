import requests
import json
YorKey = "AIzaSyDwUr1a8vrEezAggdn4A2KgmoNCvZyDVcc"
WhatYouWantToSearch = "有一種悲傷"
url = 'https://www.googleapis.com/youtube/v3/search'
dic = {'part':'status', 'key':YorKey, 'type':'video', 'q':WhatYouWantToSearch, 'order':'viewCount', 'maxResults':1}
r = requests.get(url, params=dic)
print(r.text)
# And you would get the json about it.
