import sqlite3
import time
from datetime import datetime


class Model(object):
    #TODO sql need to fix
    def __init__(self, tableName):
        self.conn = sqlite3.connect('db.music')
        self.cur = self.conn.cursor()
        self.tableName = tableName
        # print('connect to db.music success')

#select
    def getAll(self):
        sql = "SELECT * FROM "+self.tableName+";"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def getOne(self, sql):
        sql = "SELECT * FROM "+self.tableName+" WHERE "+sql+";"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def exists(self, sql):
        sql = "SELECT * FROM "+self.tableName+" WHERE "+sql+";"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if (result == None):
            return False
        else:
            return True

class AllMusic(Model):
    tableName = "AllMusic"
    def __init__(self, video_id="", artist="", song="", is_download=0):
        self.tableName = "AllMusic"
        super().__init__(self.tableName)
        
        self.video_id = video_id
        self.artist = artist
        self.song = song
        self.is_download = is_download
        self.create_at = int(time.mktime(datetime.now().timetuple()))

    def insert(self):
        self.created_at = int(time.mktime(datetime.now().timetuple()))
        sql = ("INSERT INTO " + self.tableName +" (video_id, artist, song, created_at, is_download)VALUES (?,?,?,?,?);")
        self.cur.execute(sql, [self.video_id, self.artist, self.song, self.create_at, self.is_download,])
        self.conn.commit()

    def createtable(self):
        #TODO sql need to fix
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + self.tableName + "';")
        if(self.cur.fetchone()):
            print("already has table " + self.tableName)
            return
        sql = "create table AllMusic (\
                    id           INTEGER PRIMARY KEY  autoincrement   NOT NULL,\
                    video_id     text                NULL,\
                    artist       text                NULL,\
                    song         text                not null,\
                    created_at   INTEGER             not null,\
                    is_download  INTEGER             null);"
        print("create table success")
        self.cur.execute(sql)
