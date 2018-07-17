#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from mypackage.Base import dothing
from mypackage.kkboxModle import kkboxModle
from datetime import *
import subprocess

import threading, time

class demo(object):
    def __init__(self):
        self.yesterday = datetime.now() - timedelta(days=1)# 昨天
        self.date = self.yesterday.strftime('20%y-%m-%d')
    def callredis(self):
        path = "D:/NNcode/python/beautifulsoup/redis-2.4.5-win32-win64/64bit/redis-server.exe"
        subprocess.call(path)




class MyClass (threading.Thread): # 繼承 Thread 類別
       def __init__(self):
              threading.Thread.__init__(self)
              print('做一些事...')

       def run(self): # 覆載 (Override) Thread 類別的方法(函數)
              for _ in range(0,5): # 迴圈執行五次
                     print('ok') # 輸出 ok
                     time.sleep(1) # 暫停一秒，如果要暫停 0.1秒可寫成 time.seep(0.1)



if __name__ == '__main__':
    # MyClass().start() # 啟動執行緒

    kk = kkboxModle()
    kk.weekly(t='newrelease')
    #kk.search_hot()
    