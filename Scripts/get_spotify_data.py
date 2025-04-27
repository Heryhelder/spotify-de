import os
import spotipy
import pytz
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

def get_data_from_spotify():
    CSV_PATH = "./Data/csv/"
    SCOPE = ["user-read-recently-played"]

    if not os.path.exists(CSV_PATH):
        os.makedirs(CSV_PATH)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    today = datetime.now(pytz.timezone("Brazil/East")).replace(hour=0,minute=0,second=0,microsecond=0)

    after_millisec = int(today.timestamp() * 1000)

    if not os.path.exists(CSV_PATH + f"{after_millisec} data.csv"):
        results = sp.current_user_recently_played(limit=50, after=after_millisec, before=None)

        if results:
            json_normalized = pd.json_normalize(results["items"])

            json_data = pd.read_json(json_normalized.to_json(orient="records"))

            json_data.to_csv(CSV_PATH + f"{after_millisec} data.csv", index=False)

if __name__ == "__main__":
    get_data_from_spotify()