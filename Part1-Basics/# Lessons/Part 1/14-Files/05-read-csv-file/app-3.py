"""
Read Csv Files


"""

import csv


# Another way to skip the header is to use the next() function. The next() function forwards to the reader to the next line. For example:
with open(".\\playground\\country.csv", encoding="utf8") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # skip the first row
    # show the data
    for line in csv_reader:
        print(line)
