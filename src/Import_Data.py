import requests
import time
import csv
import os
from dotenv import load_dotenv

load_dotenv() # Loads env
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-apisports-key": API_KEY
}

LEAGUE_ID = 197  # Greek Super League
SEASONS = [2021, 2022, 2023]

def get_matches(season):
    url = f"{BASE_URL}/fixtures"
    params = {
        "league": LEAGUE_ID,
        "season": season 
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    if data.get("results", 0) == 0:
        print(f"No data found for season {season}")
        return []
    matches = data.get("response", [])
    print(f"Found {len(matches)} matches for season {season}")
    return matches

def main():
    all_matches = []
    for season in SEASONS:
        matches = get_matches(season)
        all_matches.extend(matches)
        time.sleep(2)

    # Save to CSV
    keys = ["fixture_id", "date", "home_team", "away_team", "home_score", "away_score", "status"]
    with open("Greek_SuperLeague_Matches.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        for match in all_matches:
            fixture = match.get("fixture", {})
            teams = match.get("teams", {})
            goals = match.get("goals", {})
            writer.writerow([
                fixture.get("id"),
                fixture.get("date"),
                teams.get("home", {}).get("name"),
                teams.get("away", {}).get("name"),
                goals.get("home"),
                goals.get("away"),
                fixture.get("status", {}).get("long")
            ])
    print(f"✅ Saved all matches to Greek_SuperLeague_Matches.csv")

if __name__ == "__main__":
    main()
