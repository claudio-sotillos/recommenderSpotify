import random

from createPlaylist import recommend_createPL
from login import loginPLT
from utils import get_playlist_id
from utils import get_user_top_items


class InvalidPlaylistNameError(Exception):
    """Expected playlist name but got None."""
    pass

def track_based_strategy(time_range="medium_term"):

    playlist_name = f"Track List ({time_range}):  "

    print("  \n  Recommendations Based on: ")

    seed_tracks = []
    seed_artists = []
    seed_genres = []

    # Retrieve top items based on user's preference of time range
    top_items = get_user_top_items(time_range=time_range, limit=5, type="tracks")
    for item in top_items:
        playlist_name += item["name"] + ", "
        print(item["name"])  # Print the name of the track
        seed_tracks.append(item["id"])  # Store the ID of the track in seed_tracks list

    # Create playlist with recommendations
    recommend_createPL(seed_artists, seed_tracks, seed_genres, playlist_name)

def random_tracks_based_strategy(playlist_name = None):

    if playlist_name is None:
        raise InvalidPlaylistNameError("The playlist name cannot be None.")
    
    # Log in & Choose playlist
    sp = loginPLT(scope="playlist-modify-private")
    playlistID = get_playlist_id(sp, playlistName=playlist_name)

    #  Retrieve the tracks in the playlist
    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

    # Set the batch size for each request (e.g., 50 tracks per request)
    batch_size = 50
    limit = 5


    genres = []
    artistas = {}

    playlist_name = "Random Tracks List:  "


    print("  \n  Recommendations Based on: ")

    seed_tracks = []
    seed_artists = []
    seed_genres = []
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

    recommend_createPL(seed_artists,seed_tracks,seed_genres, playlist_name)