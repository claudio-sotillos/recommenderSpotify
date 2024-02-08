from utils import update_recommender_pickle
from randomStrategy import random_based_strategy
from artistStrategy import artist_based_strategy

# Main function to execute the selected strategy
def main():
    
    # Ask user for the strategy choice

    # print('Insert Playlist you want Recommendations from')
    # playlistName = input("Write Name Here: ")

    print('\n\nChoose Strategy: ')
    print(' 1 - Based on 5 Random Songs (from your last 50 Playlist songs)')
    print(' 2 - Based on 5 Random Artists (from your last 50 Playlist songs)')
    print(' 0 - Update Listened Songs Pickle')
    strategy = input("\nChoose the strategy (1 for Random, 2 for Artist based): ").strip().lower()
    
    # Execute the selected strategy
    if strategy == '1':
        random_based_strategy(playlist_name="Ma Musik")
    elif strategy == '2':
        artist_based_strategy(playlist_name="Ma Musik")
    elif strategy == '0':
        update_recommender_pickle()
    else:
        print("Invalid strategy choice. Please choose either '1' for Random or '2' for Artist based.")


if __name__ == "__main__":

    main()