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

  playList =  playlists_list_mine(service,
    part='snippet,contentDetails',
    mine=True,
    maxResults=25,
    onBehalfOfContentOwner='',
    onBehalfOfContentOwnerChannel='')

  # playlist_items_list_by_playlist_id(service,
  #   part='snippet,contentDetails',
  #   maxResults=25,
  #   playlistId='PLBkfHJJm7DdoXZuoJ-bchwt_cyTcVx63Y')

  # print(playList['items'][0]['snippet']['title'])
  for listID in playList['items']:
    print('Title:' + listID['snippet']['title'] + ', ID: ' + listID['id'])