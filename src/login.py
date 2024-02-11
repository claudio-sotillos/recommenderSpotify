import os, sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def loginPLT(scope="playlist-modify-private"):

    load_dotenv()
    # Access environment variables
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        # Prompt user to provide Spotify client ID and client secret
        print("\nPlease provide your Spotify client ID and client secret:")
        client_id = input("Client ID: ")
        client_secret = input("Client Secret: ")

        os.environ["SPOTIFY_CLIENT_ID"] = client_id
        os.environ["SPOTIFY_CLIENT_SECRET"] = client_secret
        # Store Spotify client ID and client secret in the .env file
        with open(".env", "w") as env_file:
            env_file.write(f"\nSPOTIFY_CLIENT_ID={client_id}\n")
            env_file.write(f"SPOTIFY_CLIENT_SECRET={client_secret}\n")

    # Authenticate using your client ID and client secret
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://localhost:8888/callback",
            scope=scope,
        )
    )

    return sp
