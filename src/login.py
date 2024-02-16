from colorama import Fore, Back, Style, init
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize colorama on Windows
init()

def updateCredentials():
    while True:
        # Prompt user to provide Spotify client ID and client secret
        print(f"{Fore.YELLOW}\n  Please provide your Spotify client ID and client secret:{Style.RESET_ALL}")
        client_id = input("  Client ID: ")
        client_secret = input("  Client Secret: ")

        # Attempt to create a Spotify client
        try:
            sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                    client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri="http://localhost:8888/callback",
                    scope="user-read-private",
                )
            )

            # Make a trial request to check if credentials are correct
            sp.current_user()

            os.environ["SPOTIFY_CLIENT_ID"] = client_id
            os.environ["SPOTIFY_CLIENT_SECRET"] = client_secret

            with open(".env", "w") as env_file:
                env_file.write(f"\nSPOTIFY_CLIENT_ID={client_id}\n")
                env_file.write(f"SPOTIFY_CLIENT_SECRET={client_secret}\n")

            print(f"{Fore.GREEN}  User Credentials updated successfully.{Style.RESET_ALL}")
            return client_id, client_secret

        except spotipy.oauth2.SpotifyOauthError as e:
            print(f"{Fore.RED}  Error:{Style.RESET_ALL}", e)
            print(f"{Fore.RED}  Invalid credentials. Please try again.{Style.RESET_ALL}")


def loginPLT(scope="playlist-modify-private"):
    load_dotenv()
    # Access environment variables
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        client_id, client_secret = updateCredentials()

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
