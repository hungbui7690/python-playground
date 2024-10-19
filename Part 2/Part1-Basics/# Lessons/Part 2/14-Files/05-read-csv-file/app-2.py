"""
Read Csv Files


"""

import csv


# The following shows how to read the country.csv file and display each line to the screen:
with open(".\\playground\\country.csv", encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)


print("//////////////////")


# The country.csv has the first line as the header. To separate the header and data, you use the enumerate() function to get the index of each line:
with open(".\\playground\\country.csv", encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print("Header:")
            print(line)  # header
            print("Data:")
        else:
            print(line)  # data

# In this example, we use the enumerate() function and specify the index of the first line as 1.
# Inside the loop, if the line_no is 1, the line is the header. Otherwise, it’s a data line.
