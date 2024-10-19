"""
What is a CSV file
- CSV stands for comma-separated values. A CSV file is a delimited text file that uses a comma to separate values.

- A CSV file consists of one or more lines. Each line is a data record. And each data record consists of one or more values separated by commas. In addition, all the lines of a CSV file have the same number of values.

- Typically, you use a CSV file to store tabular data in plain text. The CSV file format is quite popular and supported by many software applications such as Microsoft Excel and Google Spreadsheet.


"""

# Reading a csv file in Python
# To read a CSV file in Python, you follow these steps:
# First, import the csv module:
import csv


# Second, open the CSV file using the built-in open() function in the read mode:
with open(".\\playground\\address.csv", "r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        print(line)
