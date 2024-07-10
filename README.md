# Spotify Billboard Playlist

Spotify Billboard Playlist is an Azure Function app that automatically creates and updates a Spotify playlist with the current Billboard Hot 100 songs every week. The function scrapes the Billboard Hot 100 chart and uses the Spotify API to manage the playlist.

## Features

- Automatically updates the playlist every Sunday.
- Removes old weekly playlists starting with "Week of".
- Creates a new playlist with the current week's Billboard Hot 100 songs.

## Requirements

- Python 3.8+
- Spotify Developer Account
- Azure Account

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/spotify-billboard-playlist.git
    cd spotify-billboard-playlist
    ```

2. Create a virtual environment and install dependencies:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configure environment variables in a `.env` file:

    ```env
    SPOTIFY_ID=your_spotify_client_id
    SPOTIFY_SECRET=your_spotify_client_secret
    SPOTIFY_REDIRECT_URI=your_spotify_redirect_uri
    ```

4. Deploy to Azure:

    - Follow [Azure Functions Python Deployment Guide](https://docs.microsoft.com/azure/azure-functions/functions-create-first-function-python) to deploy the function.
    - Ensure the function app is set to run on a schedule with the cron expression `0 0 0 * * 0`.

## Usage

The function will run automatically every Sunday and update the Spotify playlist with the latest Billboard Hot 100 songs.
