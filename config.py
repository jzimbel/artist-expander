import os

class Config(object):
    SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
    SPOTIFY_ACCESS_SCOPE = 'playlist-modify-private playlist-read-private user-library-read'
