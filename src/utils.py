import pickle
from login import loginPLT


def update_recommender_pickle():
    sp, playlistID = loginPLT(playlistName="Ma Musik", scope="playlist-modify-private")
    batch_size = 50

    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]
    print(total_tracks)

    with open('recommended_ids.pkl', 'rb') as f:
        recommended_track_ids = pickle.load(f)

    print('\nHistory of Songs -- Amount: ',len(recommended_track_ids))
    last_batch_start = total_tracks % batch_size
    if last_batch_start == 0:
        last_batch_start = total_tracks - batch_size

    for offset in range(total_tracks - batch_size, last_batch_start - 1, -batch_size):
        results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        for track in results['items']:
            recommended_track_ids.add(track["track"]["id"])

    if last_batch_start > 0:
        results = sp.playlist_tracks(playlistID, limit=last_batch_start, offset=0)
        for track in results['items']:
            recommended_track_ids.add(track["track"]["id"])

    
    with open('recommended_ids.pkl', 'wb') as f:
        pickle.dump(recommended_track_ids, f)

    print('Updated History of Songs -- Amount: ', len(recommended_track_ids))



