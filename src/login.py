from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def loginPLT(playlistName='Ma Musik', scope = "playlist-modify-private"):

    load_dotenv()
    # Access environment variables
    clientId = os.getenv("SPOTIFY_CLIENT_ID")
    clientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")

    # Authenticate using your client ID and client secret
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=clientId,
            client_secret=clientSecret,
            redirect_uri="http://localhost:8888/callback",
            scope=scope,
        )
    )

    # Get the current user's playlists
    playlists = sp.current_user_playlists()

    plNames = []
    # Iterate over the playlists and print their names and IDs
    for playlist in playlists["items"]:
        plNames.append(playlist["name"].lower())
        if playlist["name"].lower() == playlistName.lower():
            playlistID = playlist["id"]

    return sp, playlistID
