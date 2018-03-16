# -*- coding:utf-8 -*-
import redis

class dothing(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379)

        #self.r.set('name', 'saneri') #创建一个键值对
        #print (self.r.get('name'))
    def strclear(self,s=''):
        if '(' in s:  #去除一些不必要的字串
            s = s[0:s.index('(')]
        if '-' in s:  #去除一些不必要的字串
            s = s[0:s.index('-')]
        return s
    def addsong(self,song):
        self.strclear("aaa")
        self.r.sadd('songList', song) #创建一个键值对

    def printissue(self,Artist,song):
        print ("Artist:",Artist)
        print ("song:",song)


    
    

    def settsting(self):
        self.r.set('name', 'saneri') #创建一个键值对
    def savetesting(self):
        self.r.save()
    def loadtesting(self):
        self.r.get('songList')
        print (self.r.get('name'))
    def deltest(self):
        self.r.flushdb()
        
    def ggg(self):
        print (self.r.smembers('songList'))
