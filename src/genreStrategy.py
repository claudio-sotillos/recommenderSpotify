from createPlaylist import recommend_createPL
from utils import get_user_top_items

class InvalidPlaylistNameError(Exception):
    """Expected playlist name but got None."""
    pass

def genre_based_strategy( time_range="medium_term"):

    playlist_name = f"Genre List ({time_range}):  "

    print("\nRecommendations Based on: ")

    seed_tracks = []
    seed_artists = []
    seed_genres = []

    # Retrieve top items based on user's preference of time range
    top_items = get_user_top_items(time_range=time_range, limit=5, type="genres")
    for item in top_items:
        playlist_name += item["name"] + ", "
        print(item["name"])  # Print the name of the genre
        seed_genres.append(item["name"])  # Store the name of the genre

    # Create playlist with recommendations
    recommend_createPL(seed_artists, seed_tracks, seed_genres, playlist_name)


