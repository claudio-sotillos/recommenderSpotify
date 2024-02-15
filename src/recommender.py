from login import updateCredentials
from utils import update_recommender_pickle
from trackStrategy import random_tracks_based_strategy, track_based_strategy
from artistStrategy import artist_based_strategy, top_artist_strategy
from genreStrategy import genre_based_strategy


# Function to print separator line
def print_separator():
    print("\n" + "-" * 80)


# Main function to execute the selected strategy
def main():
    time_range_mapping = {"1": "short_term", "2": "medium_term", "3": "long_term"}
    while True:
        print_separator()
        print("\n  Choose Strategy: ")
        print("     1 - Track-Based Strategy")
        print("     2 - Artist-Based Strategy")
        print("     3 - Genre-Based Strategy")

        print("\n  More Options")
        print("     a - Update Listened Songs History with Playlist")
        print("     b - Update Listened Songs History with songs in the 'Liked Songs' Playlist")
        print("     c - Update your Credentials (Client/Secret ID)")
        print("     e - Exit")

        strategy = input("\n  Choose the strategy (1, 2, 3 or e): ").strip().lower()

        if strategy == "1":
            while True:
                print_separator()
                print("\n  Choose Track-Based Strategy: ")
                print("     1 - Based on 5 Random Songs (from your last 50 Playlist songs)")
                print("     2 - Based on your Most Listened Songs (this month/ this year/ all times)")
                print("     b - Back to main menu")

                track_strategy = (
                    input("\n  Choose the track-based strategy (1, 2 or b): ")
                    .strip()
                    .lower()
                )
                if track_strategy == "1":
                    print("\n  Insert Playlist you want Recommendations from")
                    playlistName = input("  Write Name Here: ")
                    random_tracks_based_strategy(playlist_name=playlistName)
                elif track_strategy == "2":
                    print("\n     1 - short_term (This Month)")
                    print("     2 - medium_term (Last Year)")
                    print("     3 - long_term (All Time)")
                    time_range_int = (
                        input("\n  Choose the time range for track-based strategy (1, 2 or 3): ").strip().lower()
                    )
                    track_based_strategy(time_range=time_range_mapping[time_range_int])
                elif track_strategy == "b":
                    break
                else:
                    print("  Invalid choice. Please choose a valid option.")

        elif strategy == "2":
            while True:
                print_separator()
                print("\n  Choose Artist-Based Strategy: ")
                print("     1 - Based on 5 Random Artists (from your last 50 Playlist songs)")
                print("     2 - Based on your Most Listened Artists (this month/ this year/ all times)")
                print("     b - Back to main menu")

                artist_strategy = (
                    input("\n  Choose the artist-based strategy (1, 2 or b): ")
                    .strip()
                    .lower()
                )

                if artist_strategy == "1":
                    print("\n  Insert Playlist you want Recommendations from")
                    playlistName = input("Write Name Here: ")
                    artist_based_strategy(playlist_name=playlistName)
                elif artist_strategy == "2":
                    print("\n     1 - short_term (This Month)")
                    print("     2 - medium_term (Last Year)")
                    print("     3 - long_term (All Time)")
                    time_range_int = (
                        input("\n  Choose the time range for track-based strategy (1, 2 or 3): ").strip().lower()
                    )
                    top_artist_strategy(time_range=time_range_mapping[time_range_int])
                elif artist_strategy == "b":
                    break
                else:
                    print("  Invalid choice. Please choose a valid option.")

        elif strategy == "3":
            while True:
                print_separator()
                print("\n  Choose Genre-Based Strategy: ")
                print("     1 - Based on your Most Listened Genres (this month/ this year/ all times)")
                print("     b - Back to main menu")

                genre_strategy = (
                    input("\n  Choose the genre-based strategy (1 or b): ")
                    .strip()
                    .lower()
                )

                if genre_strategy == "1":
                    print("\n     1 - short_term (This Month)")
                    print("     2 - medium_term (Last Year)")
                    print("     3 - long_term (All Time)")
                    time_range_int = (
                        input("\n  Choose the time range for track-based strategy (1, 2 or 3): ").strip().lower()
                    )
                    genre_based_strategy(time_range=time_range_mapping[time_range_int])

                elif genre_strategy == "b":
                    break
                else:
                    print("  Invalid choice. Please choose a valid option.")

        elif strategy == "a":
            print_separator()
            print("\n  Select Playlist")
            playlistName = input("  Write Name Here: ")
            update_recommender_pickle(playlist_name=playlistName)
        elif strategy == "b":
            print_separator()
            update_recommender_pickle(scope="user-library-read")
        elif strategy == "c":
            print_separator()
            updateCredentials()
        elif strategy == "e":
            print_separator()
            print("\n  Exiting program. Goodbye & Enjoy ;) ")
            break
        else:
            print("  Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
