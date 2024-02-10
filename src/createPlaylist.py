import pickle
import os, sys
from login import loginPLT


def recommend_createPL(seed_artists, seed_tracks, playlist_name):

    # Log in & Choose playlist
    sp, _ = loginPLT(playlistName="Ma Musik", scope="playlist-modify-private")

    user_profile = sp.current_user()
    user_id = user_profile["id"]

    print("\nNew Playlist --- ", playlist_name)

    playlistLen = 30

    ## FOR LOCAL
    script_directory = os.path.dirname(sys.argv[0])
    parent_directory = os.path.dirname(script_directory)
    pickle_file_path = os.path.normpath(
        os.path.join(parent_directory, "recommended_ids.pkl")
    )

    ## FOR EXE
    # pickle_directory = os.path.dirname(os.path.dirname(os.path.dirname(sys.executable)))
    # pickle_file_path = os.path.normpath(
    #     os.path.join(pickle_directory, "recommended_ids.pkl")
    # )

    with open(pickle_file_path, "rb") as f:
        recommended_track_ids = pickle.load(f)

    print("\n Recommended Songs")

    track_uris = []
    while len(track_uris) < playlistLen:

        recommendations = sp.recommendations(
            seed_artists=seed_artists, seed_tracks=seed_tracks, limit=playlistLen + 5
        )
        for track in recommendations["tracks"]:

            if len(track_uris) >= playlistLen:
                break

            if track["uri"] not in recommended_track_ids:
                recommended_track_ids.add(track["uri"])
                track_uris.append(track["uri"])
                print("\n  Song Name: ", track["name"])
                print("    Artists: ", track["artists"][0]["name"])

    print()

    with open(pickle_file_path, "wb") as f:
        pickle.dump(recommended_track_ids, f)

    new_playlist = sp.user_playlist_create(
        user=user_id, name=playlist_name, public=False
    )
    sp.user_playlist_add_tracks(
        user=user_id, playlist_id=new_playlist["id"], tracks=track_uris
    )
