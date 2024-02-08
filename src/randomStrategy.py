from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random
import pickle

from createPlaylist import recommend_createPL
from login import loginPLT

class InvalidPlaylistNameError(Exception):
    """Expected playlist name but got None."""
    pass

def random_based_strategy(playlist_name = None):

    if playlist_name is None:
        raise InvalidPlaylistNameError("The playlist name cannot be None.")
    # Log in & Choose playlist
    sp, playlistID =  loginPLT(playlistName='Ma Musik', scope = "playlist-modify-private")


    #  Retrieve the tracks in the playlist
    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

    # Set the batch size for each request (e.g., 50 tracks per request)
    batch_size = 50
    limit = 5


    genres = []
    artistas = {}

    playlist_name = "Random List:  "


    print("\nRecommendations Based on: ")

    seed_tracks = []
    seed_artists = []
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

    recommend_createPL(seed_artists,seed_tracks, playlist_name)