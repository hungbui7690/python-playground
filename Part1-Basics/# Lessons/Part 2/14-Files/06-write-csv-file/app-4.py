"""
Write CSV File

"""

# To remove the blank line, you pass the keyword argument newline='' to the open() function as follows:
import csv

header = ["name", "area", "country_code2", "country_code3"]
data = ["Afghanistan", 652090, "AF", "AFG"]


with open(".\\playground\\countries.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
