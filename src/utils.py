from colorama import Fore, Back, Style, init
import pickle
import os
import sys
from login import loginPLT

# Initialize colorama for colored output
init()

def get_playlist_id(sp, playlistName="Ma Musik"):
    sp = loginPLT(scope="playlist-read-private")
    # Get the current user's playlists
    playlists = sp.current_user_playlists()

    plNames = []
    # Iterate over the playlists and print their names and IDs
    for playlist in playlists["items"]:
        plNames.append(playlist["name"].lower())
        if playlist["name"].lower() == playlistName.lower():
            playlistID = playlist["id"]

    return playlistID

# Define function to get user's top items
def get_user_top_items(time_range="medium_term", limit=10, type="tracks"):
    """
    Get the user's top items (tracks, artists, or genres) from Spotify.

    :param time_range: The time range of the top items. Possible values: short_term, medium_term, long_term.
    :param limit: The number of items to return. Maximum is 50.
    :param type: The type of top items to return. Possible values: tracks, artists, genres.
    :return: A list of top items with their IDs.
    """
    # Log in & Choose playlist
    sp = loginPLT(scope="user-top-read")
    top_items = []
    if type == "tracks":
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        for idx, item in enumerate(results["items"]):
            top_items.append(
                {
                    "name": item["name"],
                    "id": item["id"],
                    "artists": [artist["name"] for artist in item["artists"]],
                }
            )
    elif type == "artists":
        results = sp.current_user_top_artists(time_range=time_range, limit=limit)
        for idx, item in enumerate(results["items"]):
            top_items.append({"name": item["name"], "id": item["id"]})
    elif type == "genres":
        results = sp.current_user_top_artists(time_range=time_range, limit=limit)
        genres = []
        for artist in results["items"]:
            genres.extend(artist["genres"])
        top_genres = {genre: genres.count(genre) for genre in set(genres)}
        sorted_genres = sorted(top_genres.items(), key=lambda x: x[1], reverse=True)[
            :limit
        ]
        for idx, (genre, count) in enumerate(sorted_genres):
            top_items.append({"name": genre, "count": count})
    return top_items

def update_recommender_pickle(playlist_name=None, scope="playlist-modify-private"):
    # Log in & Choose playlist
    sp = loginPLT(scope=scope)

    batch_size = 50

    ## FOR LOCAL
    # script_directory = os.path.dirname(sys.argv[0])
    # parent_directory = os.path.dirname(script_directory)
    # pickle_file_path = os.path.normpath(
    #     os.path.join(parent_directory, "recommended_ids.pkl")
    # )

    ## FOR EXE
    pickle_file_path = os.path.join(
        os.path.dirname(sys.executable), "_internal", "recommended_ids.pkl"
    )
    with open(pickle_file_path, "rb") as f:
        recommended_track_ids = pickle.load(f)

    init_len = len(recommended_track_ids)
    print(f"\n{Fore.GREEN}    Actual History of Songs -- Amount: {init_len}{Style.RESET_ALL}")
    if scope == "user-library-read":
        print("    Adding songs already listened from the 'Liked Songs' List ...")
        results = sp.current_user_saved_tracks(limit=1)
        total_tracks = results["total"]
        last_batch_start = total_tracks % batch_size

    else:
        playlistID = get_playlist_id(sp, playlistName=playlist_name)
        playlist = sp.playlist(playlistID)
        total_tracks = playlist["tracks"]["total"]
        last_batch_start = total_tracks % batch_size
        print(
            f"    Adding songs already listened from the Playlist '{playlist_name}' ..."
        )

    if last_batch_start == 0:
        last_batch_start = total_tracks - batch_size

    for offset in range(total_tracks - batch_size, last_batch_start - 1, -batch_size):
        if scope == "user-library-read":
            results = sp.current_user_saved_tracks(limit=batch_size, offset=offset)
        else:
            results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        for track in results["items"]:
            recommended_track_ids.add(track["track"]["id"])

    if last_batch_start > 0:
        if scope == "user-library-read":
            results = sp.current_user_saved_tracks(limit=batch_size, offset=0)
        else:
            results = sp.playlist_tracks(playlistID, limit=batch_size, offset=0)
        for track in results["items"]:
            recommended_track_ids.add(track["track"]["id"])

    with open(pickle_file_path, "wb") as f:
        pickle.dump(recommended_track_ids, f)

    end_len = len(recommended_track_ids)
    print(f"\n{Fore.GREEN}    Updated History of Songs -- Amount: {end_len}{Style.RESET_ALL}")

    if end_len > init_len:
        print(f"    {end_len - init_len} Songs where added to your History ")

    else:
        print("    There aren´t new Songs to add to your History.")
