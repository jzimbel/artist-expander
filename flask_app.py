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

        maybe_create_playlist(sp)
        single_track_artists = build_single_track_artist_dict(sp)
        populate_playlist(sp, single_track_artists)
        return 'All done! Look for a playlist called "Artist Expander". It will take a few minutes to appear.'
        sys.exit()
    else:
        print "Can't get token for", Config.USER_ID
        return "Something went wrong and I don't feel like fixing it."


@app.route("/auth_code")
def auth_code():
    return "Thanks Spotify"


def maybe_create_playlist(sp):
    user_playlists = sp.user_playlists(Config.USER_ID)
    # check if a playlist named "Artist Expander" already exists
    for item in user_playlists['items']:
        if item['name'] == 'Artist Expander':
            Config.PLAYLIST_ID = item['id']
            print 'Existing "Artist Expander" playlist found.'
            return
    # no existing playlist. Let's make a new one.
    print 'Creating a new "Artist Expander" playlist.'
    result = sp.user_playlist_create(Config.USER_ID, 'Artist Expander', public=False)
    Config.PLAYLIST_ID = result['id']


def build_single_track_artist_dict(sp):
    '''
    Sometimes naming things is hard. This builds a dictionary of the form
    {artist_id: track_id} from artists for which the user has saved only 1 track.
    Only looks at the first 10,000 tracks in the user's library.
    If your library is bigger than that... it might be time to downsize.
    '''
    print 'Finding artists with only one song saved...'
    saved_track_dict = {}
    # 50 * 200 = 10,000. Probably enough for most people
    iterations = 200

    results = sp.current_user_saved_tracks(limit=50)
    for i in range(iterations):
        tracks = results['items']
        for item in tracks:
            track = item['track']
            track_id = track['id']
            # tracks can be associated with multiple artists
            artist_ids = map(lambda x: x['id'], track['artists'])
            for artist_id in artist_ids:
                artist_tracks = saved_track_dict.setdefault(artist_id, [])
                artist_tracks.append(track_id)
        if results['next'] == None:
            break
        # let us never speak of this
        next_offset = int(filter(lambda x: x.startswith('offset'), results['next'].split('?')[1].split('&'))[0].split('=')[1])
        results = sp.current_user_saved_tracks(limit=50, offset=next_offset)

    # remove all artists for which more than one track is saved,
    # and unpack the track ids from lists (since there's only 1 id now)
    single_track_dict = {k: v[0] for k, v in saved_track_dict.iteritems() if len(v) == 1}
    print 'Done.'
    return single_track_dict


def populate_playlist(sp, single_track_artists):
    print 'Populating "Artist Expander" playlist...'
    playlist = []
    for artist_id, track_id in single_track_artists.iteritems():
        # endpoint returns top 10 tracks by default, ordered by popularity descending.
        # throw away everything but the track ids.
        # throw away track that's already saved if it's one of the top 10.
        # just get the top 5 of the remaining tracks
        top_tracks = [
            track['id']
            for track in sp.artist_top_tracks(artist_id)['tracks']
            if track['id'] != track_id
        ][0:5]
        playlist.extend(top_tracks)

    # clear the existing playlist out (literally "replace all tracks with nothing")
    result = sp.user_playlist_replace_tracks(Config.USER_ID, Config.PLAYLIST_ID, [])

    # can only add 100 tracks to a playlist at a time, so split playlist
    # into a list of lists, each up to 100 elements long
    final_playlist = []
    count = 0
    i = -1
    for track_id in playlist:
        if count%100 == 0:
            final_playlist.append([])
            i += 1
        final_playlist[i].append(track_id)
        count += 1

    # populate the playlist in 100-track chunks
    for chunk in final_playlist:
        result = sp.user_playlist_add_tracks(Config.USER_ID, Config.PLAYLIST_ID, chunk)
    print 'Done!'

if __name__ == "__main__":
    Config.USER_ID = raw_input('Enter your Spotify User ID: ')
    app.run()
