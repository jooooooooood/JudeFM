import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler

# Get credentials

scope = ["playlist-modify-public", "user-top-read", "playlist-modify-private", 'user-read-recently-played', 'ugc-image-upload']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                     client_id = 'beb4c4cb4ec54cdb93f6a65a8869b845', 
                     client_secret='a8094423c7434a33bd5164fe018afb84',
                     redirect_uri='http://localhost:2000/callback/',
                     cache_handler=CacheFileHandler(cache_path=".cache")))
userID = sp.current_user()['id']

sp.user_playlist_create(user=userID, name="Shivani Playlist from Jood")

playlist = sp.user_playlists(userID, limit=1)

playlistID = playlist['items'][0]['id']

tracks = sp.current_user_top_tracks()

trackList = []

for i, track in enumerate(tracks['items']):
    trackList.append(track['uri'])

# sp.playlist_add_items(playlistID, trackList, position=None)
    
recs = sp.recommendations(seed_tracks=trackList[:4], limit=10)

sp.playlist_add_items(playlistID, [rec['uri'] for rec in recs['tracks']], position=None)