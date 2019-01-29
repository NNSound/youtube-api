import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import file, client, tools
import json
import re

from mypackage import Base
from mypackage.model import AllMusic

class UserPlaylists(object):

    # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
    # the OAuth 2.0 information for this application, including its client_id and
    # client_secret.
    CLIENT_SECRETS_FILE = "client_secret.json"

    # This OAuth 2.0 access scope allows for full read/write access to the
    # authenticated user's account and requires requests to use an SSL connection.
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    def __init__(self):
        self.mysongs = Base.getArrMysongs()

    def get_authenticated_service(self):
        store = file.Storage('token.json')
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRETS_FILE, self.SCOPES)
            credentials = tools.run_flow(flow, store)

        # flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        # credentials = flow.run_console()
        return build(self.API_SERVICE_NAME, self.API_VERSION, credentials = credentials)

    def playlists_list_mine(self,client, **kwargs):
        # See full sample for function
        kwargs = self.remove_empty_kwargs(**kwargs)

        response = client.playlists().list(
            **kwargs
        ).execute()

        return response

    # Remove keyword arguments that are not set
    def remove_empty_kwargs(self, **kwargs):
        good_kwargs = {}
        if kwargs is not None:
            for key, value in kwargs.items():
                if value:
                    good_kwargs[key] = value
        return good_kwargs

    def playlist_items_list_by_playlist_id(self, client, **kwargs):
        # See full sample for function
        kwargs = self.remove_empty_kwargs(**kwargs)

        response = client.playlistItems().list(
            **kwargs
        ).execute()

        return response

    def getMusic(self, vid, title):
        sql = "video_id = '" + vid + "'"
        model = AllMusic()
        if (model.getOne(sql) == None):
            model.artist = ''
            model.song = title
            model.video_id = vid
            model.is_download = 0
            Base.download_v3(vid, title)
            model.is_download = 1
            model.insert()
        else:
            print("Already has:"+ title)


if __name__ == '__main__':

    model = AllMusic()
    model.createtable()

    userPlaylists = UserPlaylists()

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = userPlaylists.get_authenticated_service()

    playLists =  userPlaylists.playlists_list_mine(service,
        part='snippet',
        mine=True,
        maxResults=50,
        onBehalfOfContentOwner='',
        onBehalfOfContentOwnerChannel='')

    for listID in playLists['items']:
        if (re.search('MUSIC', listID['snippet']['title'])):            
            print('Title:' + listID['snippet']['title'] + ', ID: ' + listID['id'])
            playList = userPlaylists.playlist_items_list_by_playlist_id(service,
                part='snippet',
                maxResults=25,
                playlistId=listID['id'])
            for item in playList['items']:
                print('Title:' + item['snippet']['title'] + '\nvid:' + item['snippet']['resourceId']['videoId'])
                userPlaylists.getMusic(item['snippet']['resourceId']['videoId'], item['snippet']['title'])