import sys
import pafy
import os

url = "https://www.youtube.com/watch?v=kfXdP7nZIiE"
video = pafy.new(url)
best = video.getbestaudio(preftype="m4a")
directory = "test.m4a"

best.download(filepath=directory, quiet=False,meta=True)
print("download success")