import csv
import matplotlib.pyplot as plt

years = []
sanitation = []

with open("sanitation_philippines.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        years.append(int(row["year"]))
        sanitation.append(float(row["sanitation_percent"]))

plt.plot(years, sanitation, marker="o")
plt.title("Safely Managed Sanitation Services in the Philippines")
plt.xlabel("Year")
plt.ylabel("Population (%)")
plt.grid(True)

plt.savefig("sanitation_philippines.png", dpi=150)
print("Saved sanitation_philippines.png")