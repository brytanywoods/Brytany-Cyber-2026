# Create csv_parser.py

import csv
ips = []
#Read the CVS data

with open("logs.csv", "r") as F:
    reader = csv.reader(F)

    for row in reader:
        ips.append(row[0])

print(f"IPs: {ips}")