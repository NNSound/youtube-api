from AllWeb import mojim
from mypackage import Base
from mypackage.model import AllMusic

mm = mojim()
mm.getlist()

key = Base.getKey()
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
            # Base.download_v2(vid,row[0],row[1])
            model.insert()
        else:
            print("Already has:"+row[0]+"-"+row[1])
    except:
        print("[Error]:%s - %s"%(row[0], row[1]))
