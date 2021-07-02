import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests, os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib
import matplotlib.pyplot as plt


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
 # print(auth_response.status_code)
  access_token = auth_response_data['access_token']
  #print(access_token)
  headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
  }
  return headers

#valid url
#valid artist id
#valid header
#can convert to json
#.get throws no errors
def fillDict(url,artist,header):
  r = requests.get(url + 'artists/' + artist + '/albums', headers = header)
  d = r.json()
  sample = []
  
  for album in d['items']:
    #fill sample list with the key as name and the value as the num tracks
    sample.append([album['name'], album['total_tracks']])
  return sample

def createBarChart(df,x,y):
  chart = df.plot.bar(x=x, y =y)
  plt.show()

def biggestAlbums(dataframe,numAlbums):
  print('The biggest ' , str(numAlbums), ' albums: ')
  dataframe.sort_values(by='Number of Tracks', inplace = True, ascending = False)
  for i in range (0,numAlbums):
    print('#', str(i+1), ' is ', dataframe.iloc[i,0], ' with ', dataframe.iloc[i,1], ' songs')
    
    
#def main():
CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
auth_url = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
print('Enter an Artist ID: ')
artist_id = input()
data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
header = getResponse(auth_url,data2)
dict1 = fillDict(BASE_URL,artist_id,header)
#print(dict1)
column_names = ['Album Title', 'Number of Tracks']
df = pd.DataFrame(dict1, columns = column_names)
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS tester; "')
engine = create_engine('mysql://root:codio@localhost/tester')
os.system("mysqldump -u root -pcodio tester > post.py")
os.system("mysql -u root -pcodio tester < post.py")
df.to_sql('albums', con=engine, if_exists='replace', index=False)
#createBarChart(df,'Album Title', 'Number of Tracks')
print('Mean Number of tracks: ',df["Number of Tracks"].mean())
biggestAlbums(df,5)
