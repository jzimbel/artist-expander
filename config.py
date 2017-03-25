import os

class Config(object):
    USER_ID = os.environ['SPOTIFY_USER_ID']
    PLAYLIST_ID = os.environ['SPOTIFY_PLAYLIST_ID']
    TRACK_ID = os.environ['SPOTIFY_TRACK_ID']
    SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
    SPOTIFY_ACCESS_SCOPE = 'playlist-modify-private playlist-modify-public user-library-read'
