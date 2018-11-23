# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import file, client, tools
import json



# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  store = file.Storage('token.json')
  credentials = store.get()
  if not credentials or credentials.invalid:
      flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
      credentials = tools.run_flow(flow, store)

  # flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  # credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()
  
  print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.items():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def playlists_list_mine(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlists().list(
    **kwargs
  ).execute()

  return response
  # return print_response(response)

def playlist_items_list_by_playlist_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().list(
    **kwargs
  ).execute()

  return print_response(response)

def print_response(response):
  print(response)

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.

  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()

  # channels_list_by_username(service,
  #     part='snippet,contentDetails,statistics',
  #     forUsername='GoogleDevelopers')
  playList =  playlists_list_mine(service,
    part='snippet,contentDetails',
    mine=True,
    maxResults=25,
    onBehalfOfContentOwner='',
    onBehalfOfContentOwnerChannel='')

  playlist_items_list_by_playlist_id(service,
    part='snippet,contentDetails',
    maxResults=25,
    playlistId='PLBkfHJJm7DdrXGVI2A1OOD-Os_uoYCDCd')

  # print(playList['items'][0]['id'])
  # for listID in playList['items']:
  #   print(listID['id'])