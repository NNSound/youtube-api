import sqlite3
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
    sql = ""
    print('connect success')
def getValue():
    


