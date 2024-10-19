"""
Read Csv Files


"""

import csv


# The following reads the country.csv file and calculate the total areas of all countries:
total_area = 0

# calculate the total area of all countries
with open(".\\playground\\country.csv", encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the header
    next(csv_reader)

    # calculate total
    for line in csv_reader:
        total_area += float(line[1])

print(total_area)  # 28065956.0
