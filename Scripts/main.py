import os
import spotipy
import pytz
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

DATA_PATH = "./Data/"
scope = ["user-read-recently-played"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

today = datetime.now(pytz.timezone("Brazil/East")).replace(hour=0,minute=0,second=0,microsecond=0)

after_millisec = int(today.timestamp() * 1000)

results = sp.current_user_recently_played(limit=50, after=after_millisec, before=None)

if results:
    json_normalized = pd.json_normalize(results["items"])

    json_data = pd.read_json(json_normalized.to_json(orient="records"))

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    json_data.to_csv(DATA_PATH + f"{after_millisec} data.csv", index=False)