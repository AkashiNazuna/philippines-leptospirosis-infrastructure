import csv
import requests

url = "https://api.worldbank.org/v2/country/PHL/indicator/SH.STA.SMSS.ZS"
params = {
    "format": "json",
    "date": "2020:2024",
    "per_page": 100,
}

response = requests.get(url, params=params)
response.raise_for_status()

rows = response.json()[1]

with open("sanitation_philippines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["year", "sanitation_percent"])

    for row in sorted(rows, key=lambda row: row["date"]):
        if row["value"] is not None:
            writer.writerow([row["date"], row["value"]])

print("Saved sanitation_philippines.csv")