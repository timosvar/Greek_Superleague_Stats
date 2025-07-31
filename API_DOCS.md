# API Documentation – Greek_Superleague_Stats

This file describes the main API calls used in the **Greek_Superleague_Stats** project and how to securely manage your API key using a `.env` file.

---

## Authentication
To access the data, an **API key** is required.  
The API key is stored in a `.env` file for security reasons and is never hardcoded in the source code.

### Create the `.env` file
```env
API_KEY=abcdef12345
```

#### Load the API key in Python

```python
import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Loads environment variables from the .env file

API_KEY = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

url = "https://api.superleague.example.com/matches"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"API Error: {response.status_code}")
```

- This way, the API key is not exposed in the GitHub repository.

## Endpoints

### Fetch Matches

`GET /matches`
Parameters:
- season (e.g.2021-2022)
- team (optional)
- limit (optional)


**Example:**
```python
params = {"season": "2025-26"}
response = requests.get(f"{BASE_URL}/matches", headers=headers, params=params)
print(response.json())
```

### Fetch Team Statistics

`GET /teams/stats`
Parameters:
- season (e.g.2022-2023)
- team_id (optional)


**Example:**
```python
params = {"season": "2023-24", "team_id": 12}
response = requests.get(f"{BASE_URL}/teams/stats", headers=headers, params=params)
print(response.json())
```

# Notes:

- All responses are returned in JSON format.

- It is recommended to store fetched data locally (e.g. CSV) for further analysis.

- The API can be used to feed Power BI dashboards or Python scripts for analytics.