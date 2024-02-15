# Spotify Recommendation System Interface

This Python application leverages the Spotify API to provide personalized music recommendations based on various strategies such as track-based, artist-based, and genre-based preferences. It allows users to interactively select strategies and receive recommendations tailored to their listening history and preferences. Each creation strategy creates a playlist with 30 tracks based on some seeding tracks/artists/genres.

---

## Prerequisites

Before using this application, ensure you have the following account:

- **Spotify Developer Account**: To interact with the Spotify API and access personalized music recommendations, you'll need to create a Spotify Developer Account. You can sign up for a free account on the [Spotify for Developers](https://developer.spotify.com/) website. Once registered, you can retrieve your **Client ID** and **Secret ID** by navigating to your profile image, clicking on Dashboard, selecting the project you've created for using this app, and then accessing Settings. These credentials are required only once when you execute the _main.exe_ file for the first time.


---

## Getting Started

To use this application effectively, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/recommenderSpotify.git
   ```
2. **Execute the main.exe**: Navigate to the folder _recommenderSpotify_ and then open the dist/main directory. Inside this directory, you'll find main.exe. Simply double-click on main.exe to run the application, or if you prefer using the command line, execute _main.exe_.

3. **Update Credentials**: If it is the first time that you are executing _main.exe_ you will be eventually asked to input your Developer Account credentials. This will happen once. In case you change your _secret_id_ from the Spotify Developer page you can rewrite your credentials by running option "c" in the main menu. 

5. **Update Listened Songs History**: It's advisable to update the listened songs history before getting recommendations. Use options "a" and "b" in the main menu to generate a history of the songs you have already listened to. This helps prevent recommending songs you've already heard.

6. **Choose Strategy**: Follow the prompts to select a recommendation strategy based on tracks, artists, or genres. Choose the desired time range for personalized recommendations.

7. **Enjoy Your Recommendations**: Once the strategy is selected, the application will provide recommendations based on your preferences and listening history.

## Recommendation Strategies
- **Track-Based Strategy**:
  - **Based on 5 Random Songs**: This option generates recommendations based on five randomly selected songs from your last listened songs in the input Playlist.
  - **Based on your Most Listened Songs**: This option allows you to select recommendations based on your most listened songs within different time ranges: this month, this year, or all-time. It offers recommendations tailored to your current listening habits.

- **Artist-Based Strategy**:
  - **Based on 5 Random Artists**: This option provides recommendations based on five randomly selected artists from your last listened songs in the input Playlist. 
  - **Based on your Most Listened Artists**: This option allows you to select recommendations based on your most listened artists within different time ranges: this month, this year, or all-time. It offers recommendations tailored to your favorite artists.

- **Genre-Based Strategy**:
  - **Based on your Most Listened Genres**: This option generates recommendations based on your most listened genres within different time ranges: this month, this year, or all-time. It offers recommendations tailored to your preferred music genres.


## Additional Notes

- **Resetting Credentials**: If you encounter any authentication errors or strange behavior, you can reset the user credentials by running option "c" in the main menu.

- **Credential Security**: Note that your credentials are stored locally and used only for authentication purposes with the Spotify server. They are not shared or transmitted anywhere else. You can still change the Secret ID at any time, only you may also have to change it using the "c" option. 

## Contributions

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request or open an issue on GitHub.
