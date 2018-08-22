import time
from datetime import datetime

class AllMusic():
    video_id = ""
    artist = ""
    song = ""
    created_at = int(time.mktime(datetime.now().timetuple()))
    is_download = 0
