#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import pprint
import sys
from datetime import *

import pafy
import requests
from bs4 import BeautifulSoup

from mypackage import Base
from mypackage.model import AllMusic

def getList():
    model = AllMusic()
    return model.getAll()



if __name__ == "__main__":
    songList = getList()
    # print(songList[0][1])
    i = 0
    for song in songList:
        try:
            print("SongName:%s,vid:%s"%(song[3], song[1]))
            Base.download_v3(song[1], song[3])
            i = i +1
            if (i == 10):
                break
        except Exception as e:
            print("Error:%s"%(song[3]))
            print(str(e))

