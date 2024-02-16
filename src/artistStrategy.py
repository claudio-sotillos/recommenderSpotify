from colorama import Fore, Back, Style, init
from login import loginPLT
from createPlaylist import recommend_createPL
from utils import get_playlist_id, get_user_top_items
import random

class InvalidPlaylistNameError(Exception):
    """Expected playlist name but got None."""
    pass

# Initialize colorama on Windows
init()

def top_artist_strategy(time_range="medium_term"):
    playlist_name = f"Artist List ({time_range}):  "

    print(f"{Fore.YELLOW}\n    Recommendations Based on:{Style.RESET_ALL}")

    seed_tracks = []
    seed_artists = []
    seed_genres = []

    # Retrieve top items based on user's preference of time range
    top_items = get_user_top_items(time_range=time_range, limit=5, type="artists")
    for item in top_items:
        playlist_name += item["name"] + ", "
        seed_artists.append(item["id"])  # Store the ID of the artist

    # Create playlist with recommendations
    recommend_createPL(seed_artists, seed_tracks, seed_genres, playlist_name)


def artist_based_strategy(playlist_name=None):
    if playlist_name is None:
        raise InvalidPlaylistNameError(f"{Fore.RED}The playlist name cannot be None.{Style.RESET_ALL}")

    # Log in & Choose playlist
    sp = loginPLT(scope="playlist-modify-private")
    playlistID = get_playlist_id(sp, playlistName=playlist_name)

    # Retrieve the tracks in the playlist
    playlist = sp.playlist(playlistID)
    total_tracks = playlist["tracks"]["total"]

    # Set the batch size for each request (e.g., 50 tracks per request)
    batch_size = 50
    limit = 100
    seed_tracks = []
    artistas = {}

    playlist_name = "Based on: "

    print(f"{Fore.YELLOW}\n  Recommendations Based on:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}  Gathering data ...{Style.RESET_ALL}")
    artistas = {}
    artist_counts = {}

    for offset in range(total_tracks - batch_size, -1, -batch_size):
        results = sp.playlist_tracks(playlistID, limit=batch_size, offset=offset)

        for track in reversed(results["items"]):
            for artist in track["track"]["artists"]:
                artist_name = artist["name"]
                artist_id = artist["id"]

                # Update the count for the current artist
                if artist_name in artist_counts.keys():
                    artist_counts[artist_name] += 1
                else:
                    artist_counts[artist_name] = 1

                artistas[artist_name] = artist_id

    print(f"{Fore.YELLOW}  Top {limit} artists Selected{Style.RESET_ALL}")

    # Sort the artists by their counts in descending order
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)[:100]
    randArtists = random.sample(sorted_artists, 5)

    seed_artists = []
    seed_tracks = []
    seed_genres = []
    for artist in randArtists:
        print("  ",artist[0], f"(Counts: {artist[1]})")
        playlist_name += artist[0] + ", "
        seed_artists.append(artistas[artist[0]])

    recommend_createPL(seed_artists, seed_tracks, seed_genres, playlist_name)
