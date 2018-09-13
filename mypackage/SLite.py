import sqlite3
import time
from datetime import datetime
from mypackage.models.AllMusic import AllMusic as model
'''
db.music.AllMusic
-------------------------------
|id         |int    |pk       |
|-----------+-------+---------|
|video_id   |string |null     |
|-----------+-------+---------|
|artist     |string |null     |
|-----------+-------+---------|
|song       |string |not null |
|-----------+-------+---------|
|created_at |int    |not null |
|-----------+-------+---------|
|is_download|int    |not null |
|-----------------------------|
'''
def connect():
    conn = sqlite3.connect('db.music')
    cur = conn.cursor()
    print('connect success')
    return cur 

def createtable():
    cur = connect()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='AllMusic';")
    if(cur.fetchone()):
        print("already has table")
        return
    sql = "create table AllMusic (\
                id           INTEGER PRIMARY KEY  autoincrement   NOT NULL,\
                video_id     text                NULL,\
                artist       text                NULL,\
                song         text                not null,\
                created_at   INTEGER                 not null,\
                is_download  INTEGER                 null);"
    print("create table success")
    cur.execute(sql)

def getAll():
    cur = connect()
    sql = "SELECT * FROM AllMusic;"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getOne(q = '1'):
    cur = connect()
    sql = "SELECT * FROM AllMusic WHERE "+str(q)+";"
    result = cur.fetchone()
    return result

def insert():
    conn = sqlite3.connect('db.music')
    cur = conn.cursor()
    model.created_at = int(time.mktime(datetime.now().timetuple()))

    cur.execute("INSERT INTO AllMusic (video_id, artist, song, created_at, is_download)\
            VALUES (?,?,?,?,?);", [model.video_id, model.artist, model.song, model.created_at, model.is_download])
    conn.commit()
    print("insert success")

# if __name__ == '__main__':
    # createtable()
    # model.artist = "MEE"
    # model.song = "test"
    # model.video_id = "123456"
    # insert()
    # if (getOne('id = 102') == None) :
    #     print ('nothing')
    # else:
    #     print(getOne('song = test'))

    # cur = connect()
    # cur.execute("drop table AllMusic;")
