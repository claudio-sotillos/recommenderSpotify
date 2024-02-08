from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random
import pickle




load_dotenv()
# Access environment variables
clientId = os.getenv("SPOTIFY_CLIENT_ID")
clientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")
playlistId = os.getenv("SPOTIFY_PLAYLIST_ID")

# Authenticate using your client ID and client secret
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=clientId,
        client_secret=clientSecret,
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-private",
    )
)


playlisName = "Ma Musik"
user_profile = sp.current_user()
user_id = user_profile["id"]

# Get the current user's playlists
playlists = sp.current_user_playlists()

plNames = []
# Iterate over the playlists and print their names and IDs
for playlist in playlists["items"]:
    plNames.append(playlist["name"].lower())
    if playlist["name"].lower() == playlisName.lower():
        playlistID = playlist["id"]


# Retrieve the tracks in the playlist

playlist = sp.playlist(playlistID)
total_tracks = playlist["tracks"]["total"]

# Set the batch size for each request (e.g., 50 tracks per request)
batch_size = 50
limit = 5
seed_tracks = []

genres = []
artistas = {}

playlist_name = "REC List: "


print("\nRecommendations Based on: ")

# Retrieve the tracks in the playlist in reverse order (most recent first)
for offset in range(total_tracks - batch_size, -1, -batch_size):
    results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

    randSongs = random.sample(results["items"], limit)

    for track in randSongs:
        print(track["track"]["name"])
        for artist in track["track"]["artists"]:
            playlist_name += artist["name"] + ", "
            artistas[artist["name"]] = artist["id"]
        # artists.append(track['track']['artists'])
        #
        # genres = get_genres(track["track"])
        seed_tracks.append(track["track"]["id"])

        # Stop the loop when the limit is reached
        if len(seed_tracks) >= limit:
            break

    # Stop the loop when the limit is reached
    if len(seed_tracks) >= limit:
        break


new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlistLen = 30
track_uris = []
with open('recommended_ids.pkl', 'rb') as f:
    recommended_track_ids = pickle.load(f)


print('\n Recommended Songs')
while len(track_uris) < playlistLen:
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=playlistLen +5 )
    for track in recommendations["tracks"]:

        if len(track_uris) >= playlistLen:
            break

        if track["uri"] not in recommended_track_ids:
            recommended_track_ids.add(track["uri"])
            track_uris.append(track["uri"])
            print('\nSong Name: ',track["name"])
            print('Artists: ',track["artists"][0]["name"])



with open('recommended_ids.pkl', 'wb') as f:
    pickle.dump(recommended_track_ids, f)


sp.user_playlist_add_tracks(
    user=user_id, playlist_id=new_playlist["id"], tracks=track_uris
)


### Tries


# artistID = artistas[list(artistas.keys())[0]]
# print(artistID)
# sp.artists(artist_id= str(artistID))

# ranges = ['medium_term', 'long_term']
# for sp_range in ranges:
#     print("range:", sp_range)
#     results = sp.current_user_top_tracks(time_range=sp_range)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], '//', item['artists'][0]['name'])
#     print()




# def get_genres(track_details):
#     genres = {}
#     # Get the artists associated with the track
#     artists = [artist["name"] for artist in track_details["artists"]]

#     # Fetch genre information for each artist
#     for artist_name in artists:
#         # Make a request to the Last.fm API to get artist info (replace 'API_KEY' with your actual Last.fm API key)
#         response = requests.get(
#             f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key=API_KEY&format=json"
#         )
#         data = response.json()
#         if "artist" in data and "tags" in data["artist"]:
#             artist_genres = [tag["name"] for tag in data["artist"]["tags"]["tag"]]
#             genres.extend(artist_genres)

#     return genres