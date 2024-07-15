"""
Writing multiple rows to CSV files

- To write multiple rows to a CSV file at once, you use the writerows() method of the CSV writer object.

"""

# The following uses the writerows() method to write multiple rows into the countries.csv file:
import csv

header = ["name", "area", "country_code2", "country_code3"]
data = [
    ["Albania", 28748, "AL", "ALB"],
    ["Algeria", 2381741, "DZ", "DZA"],
    ["American Samoa", 199, "AS", "ASM"],
    ["Andorra", 468, "AD", "AND"],
    ["Angola", 1246700, "AO", "AGO"],
]

with open(".\\playground\\countries.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
