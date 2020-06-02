import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

def insert():

    doc = {
        'artist': "111",
        'song': "111",
        'created_at': "111",
        'is_download': True,
        'video_id': "111",
    }
    doc_ref = db.collection("MusicList").document("aaa")
    doc_ref.set(doc)

def select():
    doc_ref = db.collection("MusicList").document("aaa")
    try:
        doc = doc_ref.get()
        print(doc.to_dict())
    except Exception as e:
        print("Nodata")

select()
