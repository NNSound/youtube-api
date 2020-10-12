
from AllWeb import kkbox
from mypackage import Base
from mypackage.model import AllMusic

kk = kkbox()

# kk.daily()
kk.weekly()#297華語
kk.weekly(cid=390)#西洋
# kk.weekly(cid=324)
# kk.weekly(cid=352)

key = Base.getKey()
model = AllMusic()
model.createtable()

mylist = Base.getArrMysongs()
for row in mylist:

    try:
        vid = Base.search_hot(key,row[0]+" "+row[1])
        sql = "video_id = '" + vid + "'"
        model = AllMusic()
        if (model.getOne(sql) == None):
            model.artist = row[0]
            model.song = row[1]
            model.video_id = vid
            model.is_download = 0
            fileName = "%s - %s"%(row[0],row[1])
            Base.download_v3(vid, fileName)
            model.is_download = 1
            model.insert()
            print("[INSERT] %s-%s"%(row[0], row[1]))
        else:
            print("[PASS]Already has:%s-%s"%(row[0], row[1]))

    except Exception as e:
        if (str(e) == "youtube-search-error"):
            print("youtube-search-error")
            break

        print(str(e))
        continue
