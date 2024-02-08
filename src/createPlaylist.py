import pickle
from login import loginPLT

def recommend_createPL(seed_artists,seed_tracks, playlist_name):

    # Log in & Choose playlist
    sp, _ = loginPLT(playlistName="Ma Musik", scope="playlist-modify-private")

    user_profile = sp.current_user()
    user_id = user_profile["id"]
    

    print('\nNew Playlist --- ',playlist_name)
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlistLen = 30
    track_uris = []
    with open('recommended_ids.pkl', 'rb') as f:
        recommended_track_ids = pickle.load(f)


    print('\n Recommended Songs')
    
    while len(track_uris) < playlistLen:
        
        recommendations = sp.recommendations(seed_artists = seed_artists,seed_tracks=seed_tracks, limit=playlistLen +5 )
        for track in recommendations["tracks"]:

            if len(track_uris) >= playlistLen:
                break

            if track["uri"] not in recommended_track_ids:
                recommended_track_ids.add(track["uri"])
                track_uris.append(track["uri"])
                print('\n  Song Name: ',track["name"])
                print('    Artists: ',track["artists"][0]["name"])

    print()

    with open('recommended_ids.pkl', 'wb') as f:
        pickle.dump(recommended_track_ids, f)


    sp.user_playlist_add_tracks(
        user=user_id, playlist_id=new_playlist["id"], tracks=track_uris
    )

