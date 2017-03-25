import pprint
import sys
import spotipy
import spotipy.util as util
from flask import Flask

app = Flask(__name__)

username = None
playlist_id = None
track_ids = None

@app.route("/login")
def login():
    import ipdb; ipdb.set_trace()
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print results
    else:
        print "Can't get token for", username

@app.route("/application")
def application():
    return "Good job you did it"

if __name__ == "__main__":
    if len(sys.argv) > 3:
        username = sys.argv[1]
        playlist_id = sys.argv[2]
        track_ids = sys.argv[3:]
    else:
        print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
        sys.exit()
    app.run()
