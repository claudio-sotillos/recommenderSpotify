
import pickle

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random
import pickle


def update_recommender_pickle(spClient,playlistID):
    batch_size = 50

    playlist = spClient.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

    with open('recommended_ids.pkl', 'rb') as f:
        recommended_track_ids = pickle.load(f)

    print(len(recommended_track_ids))
    for offset in range(total_tracks - batch_size, -1, -batch_size):
        results = spClient.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        # randSongs = random.sample(results["items"], limit)

        for track in reversed(results['items']):
            recommended_track_ids.add(track["track"]["id"])


    print(len(recommended_track_ids))

    with open('recommended_ids.pkl', 'wb') as f:
        pickle.dump(recommended_track_ids, f)




