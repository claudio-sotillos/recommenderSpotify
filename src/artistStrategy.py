from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random
import pickle

from login import loginPLT
from createPlaylist import recommend_createPL

class InvalidPlaylistNameError(Exception):
    """Expected playlist name but got None."""
    pass

def artist_based_strategy(playlist_name = None):

    if playlist_name is None:
        raise InvalidPlaylistNameError("The playlist name cannot be None.")
    
    # Log in & Choose playlist
    sp, playlistID = loginPLT(playlistName=playlist_name, scope="playlist-modify-private")


    #  Retrieve the tracks in the playlist
    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

    # Set the batch size for each request (e.g., 50 tracks per request)
    batch_size = 50
    limit = 100
    seed_tracks = []
    artistas = {}

    playlist_name = "Based on: "

    print("\nRecommendations Based on: ")
    print("Gathering data ...")
    artistas = {}
    artist_counts = {}

    for offset in range(total_tracks - batch_size, -1, -batch_size):
        results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        # if len(artist_counts) <= limit:

        for track in reversed(results["items"]):
            # print(track["track"]["name"])
            for artist in track["track"]["artists"]:

                artist_name = artist["name"]
                artist_id = artist["id"]
            

                # Update the count for the current artist
                if artist_name in artist_counts.keys():
                    artist_counts[artist_name] += 1
                else:
                    artist_counts[artist_name] = 1

                artistas[artist_name] = artist_id
        # else:
        #     break

    print("Top ", limit, " artists Selected")
    # Sort the artists by their counts in descending order
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)[:100]


    randArtists = random.sample(sorted_artists, 5)

    seed_artists = []
    seed_tracks = []
    for artist in randArtists:
        print(artist[0], '(Counts: ',artist[1],')')
        playlist_name += artist[0] + ", "
        seed_artists.append(artistas[artist[0]])


    recommend_createPL(seed_artists,seed_tracks, playlist_name)

