import tweepy
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


CONSUMER_KEY = 'amrk2xaiX3gvu8GWAQgcTBfND'
CONSUMER_SECRET = 'CWyDhI9b9iSLKhzXglBtmgp6hpKPTa73CUjHLb9IBzhpj0gKxV'
ACCESS_TOKEN = '1378616618759098368-P2d0BM0uqGQ0SvFAVyHFEjE4O6cO2F'
ACCESS_TOKEN_SECRET = 'bL4ORA2fSzMVKmKrRcVCwN38tPzu8bSF1msdqQxMJDQvm'
username = 'supalups'
scope = 'user-read-currently-playing'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(username='supalups',
                                                    scope='user-read-currently-playing',
                                                    client_id='2b5a2c9b01e4426196eeae9d07b352f7',
                                                    client_secret='da168907b423478d90fed2ae4326de0a',
                                                    redirect_uri='http://localhost:8888/callback'))

while True:
    try:
        current_track = spotify.current_user_playing_track()
        current_track_id = current_track['item']['id']

        if current_track_id is not None:
    

            api.update_status("jelly's currently listening to" + ":" + '\n' + current_track['item']['artists'][0]['name'] + " - " +
                                                                    current_track['item']['name'] + '\n' + str(
                                                                    current_track['item']['external_urls']['spotify']))
            break
        else:
            continue
    except spotipy.client.SpotifyException:
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(username='supalups',
                                                              scope='user-read-currently-playing',
                                                              client_id='2b5a2c9b01e4426196eeae9d07b352f7',
                                                              client_secret='da168907b423478d90fed2ae4326de0a',
                                                              redirect_uri='http://localhost:8888/callback'))
    except (tweepy.TweepError, TypeError) as e:
        pass

while True:
    try:
       new_track = spotify.current_user_playing_track()
       new_track_id = new_track['item']['id']

       if current_track_id is not None and new_track_id != current_track_id:

                                                                                     
           api.update_status("jelly's currently listening to" + ":" + '\n' + new_track['item']['artists'][0]['name'] + " - " +
                                                  new_track['item']['name'] + '\n' + str(
                                                  new_track['item']['external_urls']['spotify']))
           current_track_id = new_track_id
       else:
           continue
    except spotipy.client.SpotifyException:
         spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(username='supalups',
                                                               scope='user-read-currently-playing',
                                                               client_id='2b5a2c9b01e4426196eeae9d07b352f7',
                                                               client_secret='da168907b423478d90fed2ae4326de0a',
                                                               redirect_uri='http://localhost:8888/callback'))
    except (tweepy.TweepError, TypeError)as e:
         pass                                                                    
