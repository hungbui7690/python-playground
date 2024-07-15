"""
Writing to CSV files using the DictWriter class

- If each row of the CSV file is a dictionary, you can use the DictWriter class of the csv module to write the dictionary to the CSV file.

"""

import csv

# First, define variables that hold the field names and data rows of the CSV file.
fieldnames = ["name", "area", "country_code2", "country_code3"]

# csv data
rows = [
    {"name": "Albania", "area": 28748, "country_code2": "AL", "country_code3": "ALB"},
    {"name": "Algeria", "area": 2381741, "country_code2": "DZ", "country_code3": "DZA"},
    {
        "name": "American Samoa",
        "area": 199,
        "country_code2": "AS",
        "country_code3": "ASM",
    },
]

# Next, open the CSV file for writing by calling the open() function.
with open(".\\playground\\countries.csv", "w", encoding="UTF8", newline="") as f:
    # Then, create a new instance of the DictWriter class by passing the file object (f) and fieldnames argument to it.
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # After that, write the header for the CSV file by calling the writeheader() method.
    writer.writeheader()

    # Finally, write data rows to the CSV file using the writerows() method.
    writer.writerows(rows)
