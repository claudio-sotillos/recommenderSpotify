import pickle 

with open('recommended_ids.pkl', 'rb') as f:
        recommended_track_ids = pickle.load(f)

print(len(recommended_track_ids))





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