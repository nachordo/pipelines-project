import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests



 
def get_artist_id(spotify,artist):
    results = spotify.search(q='artist:' + artist, type='artist')
    id_artist = results['artists']['items'][0]["id"]
    return id_artist

 
def get_artist_top(spotify,artist,country):
    toptracks = spotify.artist_top_tracks(get_artist_id(spotify,artist), country=country)
    top_list = [x['name'].split(" -")[0] for x in toptracks['tracks']]
    return top_list

def get_track_id(spotify,song):
    results = spotify.search(q='track:' + song, type='track') 
    try:
    	id_song = results['tracks']['items'][0]["id"]
    	return id_song
    except:
        return "NONE"

def get_track_album(spotify,song):
    track = spotify.track(get_track_id(spotify,song))
    return track["album"]["name"]


def get_album_id(spotify,album):
    album_id = spotify.search(q='album:' + album, type='album')
    return album_id['albums']['items'][0]["id"]

def get_tracks_from_album(spotify,album):
    album_tracks=spotify.album_tracks(get_album_id(spotify,album), limit=50, offset=0, market=None)
    track_list=[x["name"].split(" -")[0] for x in album_tracks["items"]]
    return track_list


def get_song_features(spotify,song):
    audio = spotify.audio_features(get_track_id(spotify,song))
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    audio_features={feat:audio[0][feat] for feat in features}
    return audio_features

def get_album_features(spotify,album):
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    songs = get_tracks_from_album(spotify,album)
    audio_features={feat:[] for feat in features}
    for song in songs:
        audio = spotify.audio_features(get_track_id(spotify,song))
        for feat in features:
            audio_features[feat].append(audio[0][feat])
    
    return audio_features

def get_album_features_median(spotify,album):
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    songs = get_tracks_from_album(spotify,album)
    audio_features={feat:[] for feat in features}
    for song in songs:
    	if get_track_id(spotify,song) != "NONE":
        	audio = spotify.audio_features(get_track_id(spotify,song))
        	for feat in features:
            		audio_features[feat].append(audio[0][feat])
    
    audio_features_median = {feat:np.median(np.array(audio_features[feat])) for feat in features}
    return audio_features_median

def get_album_features_stdv(spotify,album):
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    songs = get_tracks_from_album(spotify,album)
    audio_features={feat:[] for feat in features}
    for song in songs:
        audio = spotify.audio_features(get_track_id(spotify,song))
        for feat in features:
            audio_features[feat].append(audio[0][feat])
    
    audio_features_median = {feat:np.std(np.array(audio_features[feat])) for feat in features}
    return audio_features_median


def get_wiki_views(lang,page,ini_year,ini_month,ini_day,end_year,end_month,end_day):
    try:
        wiki_url_1="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"+lang.lower()
        wiki_url_2=".wikipedia/all-access/all-agents/"+page.replace(" ","_")
        wiki_url_3="/monthly/"+str(ini_year)+str(ini_month).zfill(2)+str(ini_day).zfill(2)+"/"+str(end_year)+str(end_month).zfill(2)+str(end_day).zfill(2)
        wiki_url=wiki_url_1+wiki_url_2+wiki_url_3
        data = requests.get(wiki_url)
        data=data.json()['items']
        views = [x['views'] for x in data]
        return np.median(views)
    except:
        return 0
