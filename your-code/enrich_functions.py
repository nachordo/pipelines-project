 
def get_wiki_views(lang,page,ini_year,ini_month,ini_day,end_year,end_month,end_day):
    wiki_url_1="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"+str(lang)
    #.wikipedia/all-access/all-agents/The_Beatles/monthly/20200101/20201001
    wiki_url_2=".wikipedia/all-access/all-agents/"+page.replace(" ","_")
    wiki_url_3="/monthly/"+str(ini_year)+str(ini_month).zfill(2)+str(ini_day).zfill(2)+"/"+str(end_year)+str(end_month).zfill(2)+str(end_day).zfill(2)
    wiki_url=wiki_url_1+wiki_url_2+wiki_url_3
    data = requests.get(wiki_url)
    data=data.json()['items']
    views = [x['views'] for x in data]
    return np.median(views)
 
def get_artist_id(artist):
    results = spotify.search(q='artist:' + artist, type='artist')
    id_artist = results['artists']['items'][0]["id"]
    return id_artist

 
def get_artist_top(artist,country):
    toptracks = spotify.artist_top_tracks(get_artist_id(artist), country=country)
    top_list = [x['name'].split(" -")[0] for x in toptracks['tracks']]
    return top_list

def get_track_id(song):
    results = spotify.search(q='track:' + song, type='track')
    id_song = results['tracks']['items'][0]["id"]
    return id_song

def get_track_album(song):
    track = spotify.track(get_track_id(song))
    return track["album"]["name"]


def get_album_id(album):
    album_id = spotify.search(q='album:' + album, type='album')
    return album_id['albums']['items'][0]["id"]

def get_tracks_from_album(album):
    album_tracks=spotify.album_tracks(get_album_id(album), limit=50, offset=0, market=None)
    track_list=[x["name"].split(" -")[0] for x in album_tracks["items"]]
    return track_list


def get_song_features(song):
    audio = spotify.audio_features(get_track_id(song))
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    audio_features={feat:audio[0][feat] for feat in features}
    return audio_features

def get_album_features(album):
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    songs = get_tracks_from_album(album)
    audio_features={feat:[] for feat in features}
    for song in songs:
        audio = spotify.audio_features(get_track_id(song))
        for feat in features:
            audio_features[feat].append(audio[0][feat])
    
    return audio_features

def get_album_features_mean(album):
    features = ['danceability', 'energy',  'loudness',  'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    songs = get_tracks_from_album(album)
    audio_features={feat:[] for feat in features}
    for song in songs:
        audio = spotify.audio_features(get_track_id(song))
        for feat in features:
            audio_features[feat].append(audio[0][feat])
    
    audio_features_mean = {feat:np.mean(np.array(audio_features[feat])) for feat in features}
    return audio_features_mean
