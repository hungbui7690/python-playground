"""
Write CSV File
- Steps for writing a CSV file

- To write data into a CSV file, you follow these steps:

    First, open the CSV file for writing (w mode) by using the open() function.
    Second, create a CSV writer object by calling the writer() function of the csv module.
    Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
    Finally, close the file once you complete writing data to it.

"""

# The following code illustrates the above steps:
import csv

# data
row = ["Alex", "Pandrea", 29]

# open the file in the write mode
f = open(".\\playground\\user.csv", "w")

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(row)

# close the file
f.close()
