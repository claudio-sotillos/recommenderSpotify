import pickle
import os , sys
from login import loginPLT


def update_recommender_pickle(playlist_name, scope = "playlist-modify-private"):
    sp, playlistID = loginPLT(playlistName=playlist_name, scope=scope)
    batch_size = 50

    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

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


    with open(pickle_file_path, 'rb') as f:
        recommended_track_ids = pickle.load(f)

    init_len = len(recommended_track_ids)
    print('\nActual History of Songs -- Amount: ',init_len)
    if scope == "user-library-read":
        print("Adding songs already listened from the 'Liked Songs' List ...")
    else:
        print("Adding songs already listened from the Playlist '",playlist_name,"' ...")
        
    last_batch_start = total_tracks % batch_size
    if last_batch_start == 0:
        last_batch_start = total_tracks - batch_size

    for offset in range(total_tracks - batch_size, last_batch_start - 1, -batch_size):
        if scope == "user-library-read":
            results = sp.current_user_saved_tracks(limit=batch_size, offset=offset)
        else:
            results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        for track in results['items']:
            recommended_track_ids.add(track["track"]["id"])

    if last_batch_start > 0:
        if scope == "user-library-read":
            results = sp.current_user_saved_tracks(limit=batch_size, offset=0)
        else:
            results = sp.playlist_tracks(playlistID, limit=batch_size, offset=0)
        for track in results['items']:
            recommended_track_ids.add(track["track"]["id"])

    
    with open(pickle_file_path, 'wb') as f:
        pickle.dump(recommended_track_ids, f)

    end_len = len(recommended_track_ids)
    print('\nUpdated History of Songs -- Amount: ', end_len)

    if end_len > init_len:
        print(end_len-init_len, " Songs where added to your History ")

    else:
        print('There aren´t new Songs to add to your History.')




