# Super League Greece Statistics 2021 - 2023 Dashboard

This project fetches football data from the Super League Greece (2021 - 2023) API, processes it into a clean CSV format, and visualizes key statistics in an interactive Power BI dashboard.  

---

## Project Workflow
1. **Data Fetching**
   - Uses API key to request Super League Greece data from 2021 - 2023 seasons.
   - Converts JSON response to CSV.

2. **Data Cleaning**
   - CSV is processed in Excel for:
     - Removing null/duplicate rows.
     - Adding calculated columns (Total Goals, Home/Away points, etc.).
     - Formatting for Power BI.

3. **Visualization**
   - Cleaned Excel data is imported into Power BI.
   - Interactive dashboard is created to display:
     - Team performance (Wins, Draws, Losses).
     - Least & most goals in a match.
     - Home/Away goals and other metrics.

---

## Screenshots
![Page-1](Screenshot01_PowerBi-2.png)
![Page-2](Screenshot2_PowerBi-1.png)

---

## Installation & Usage
### Clone the Repository
```bash
git clone https://github.com/timosvar/Greek_Superleague_Stats.git
cd Greek_Superleague_Stats
