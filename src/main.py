from utils import update_recommender_pickle
from randomStrategy import random_based_strategy
from artistStrategy import artist_based_strategy

# Main function to execute the selected strategy
def main():
    while True:
        # Ask user for the strategy choice
        # print('\nInsert Playlist you want Recommendations from')
        # playlistName = input("Write Name Here: ")
        playlistName = "Ma Musik"

        print('\n\nChoose Strategy: ')
        print(' 1 - Based on 5 Random Songs (from your last 50 Playlist songs)')
        print(' 2 - Based on 5 Random Artists (from your last 50 Playlist songs)')

        print("\nMore Options")
        print(' a - Update Listened Songs History with Playlist')
        print(" b - Update Listened Songs History with songs in the 'Liked Songs' Playlist")        
        print(' e - Exit')
        strategy = input("\nChoose the strategy (0, 1 , 2 or e): ").strip().lower()
        
        # Execute the selected strategy
        if strategy == '1':
            random_based_strategy(playlist_name=playlistName)
        elif strategy == '2':
            artist_based_strategy(playlist_name=playlistName)
        elif strategy == 'a':
            update_recommender_pickle(playlist_name=playlistName)
        elif strategy == 'b':
            update_recommender_pickle(playlist_name=playlistName, scope="user-library-read")
        elif strategy == 'e':
            print("\nExiting program. Goodbye & Enjoy ;) ")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
