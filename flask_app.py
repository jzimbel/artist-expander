import pprint
import sys
import spotipy
import spotipy.util as util
from flask import Flask

from config import Config

app = Flask(__name__)

@app.route("/login")
def login():
    token = util.prompt_for_user_token(Config.USER_ID, Config.SPOTIFY_ACCESS_SCOPE)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(Config.USER_ID, Config.PLAYLIST_ID, [Config.TRACK_ID])
        print results
    else:
        print "Can't get token for", Config.USER_ID
    return "Logged in or something, I guess"

@app.route("/auth_code")
def auth_code():
    return "Good job you did it"

if __name__ == "__main__":
    app.run()
