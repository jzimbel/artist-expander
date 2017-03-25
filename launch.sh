#!/bin/bash
# get secret env vars
. secrets.sh

export SPOTIFY_USER_ID='128300609'
export SPOTIFY_PLAYLIST_ID='2MdKgm5jVxuf0r1oSm3Un1'
export SPOTIFY_TRACK_ID='0IoDFIs15h0GpTpr5Iy38I'

# start the server
python flask_app.py $SPOTIFY_USER_ID $SPOTIFY_PLAYLIST_ID $SPOTIFY_TRACK_ID
