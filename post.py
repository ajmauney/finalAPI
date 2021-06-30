import requests
import spotipy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
auth_url = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
artist_id = '7dGJo4pcD2V6oG8kP0tJRR'
data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}

#post throws no errors
#url valid
#data valid
#json format is correct
#status code is given
#status code is 200
#access token is valid
#headers with token are valid
def getResponse(url,data):
  auth_response = requests.post(url, data)
  auth_response_data = auth_response.json()
  print(auth_response.status_code)
  access_token = auth_response_data['access_token']
  print(access_token)
  headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
  }
  return headers

header = getResponse(auth_url,data2)

#valid url
#valid artist id
#valid header
#can convert to json
#.get throws no errors
def fillDict(url,artist,header):
  r = requests.get(url + 'artists/' + artist + '/albums', headers = header)
  d = r.json()
  sample = {}
  i = 0
  for album in d['items']:
    #print(album['name'], '---', album['total_tracks'])
    #sample[album['name']] = album['total_tracks']
    sample[i] = [i, album['name'], album['total_tracks']]
    i+=1
  return sample

dict1 = fillDict(BASE_URL,artist_id,header)
df = pd.DataFrame.from_dict(dict1, orient = 'index')
engine = create_engine('mysql://root:codio@localhost/tester')
df.to_sql('albums', con=engine, if_exists='replace', index=False)
