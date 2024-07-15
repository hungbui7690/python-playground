"""
Write CSV File

"""

import csv

header = ["name", "area", "country_code2", "country_code3"]
data = ["Afghanistan", 652090, "AF", "AFG"]

# open the file in the write mode
with open(".\\playground\countries.csv", "w", encoding="UTF8") as f:
    # create the csv writer
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)

# If you open the countries.csv, you’ll see one issue that the file contents have an additional blank line between two subsequent rows
