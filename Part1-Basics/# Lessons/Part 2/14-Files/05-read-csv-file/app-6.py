"""
Reading a CSV file using the DictReader class

- When you use the csv.reader() function, you can access values of the CSV file using the bracket notation such as line[0], line[1], and so on. However, using the csv.reader() function has two main limitations:

    + First, the way to access the values from the CSV file is not so obvious. For example, the line[0] implicitly means the country name. It would be more expressive if you can access the country name like line['country_name'].
    + Second, when the order of columns from the CSV file is changed or new columns are added, you need to modify the code to get the right data.

- This is where the DictReader class comes into play. The DictReader class also comes from the csv module.

- The DictReader class allows you to create an object like a regular CSV reader. But it maps the information of each line to a dictionary (dict) whose keys are specified by the values of the first line.

- By using the DictReader class, you can access values in the country.csv file like line['name'], line['area'], line['country_code2'], and line['country_code3'].


"""

# If you want to have different field names other than the ones specified in the first line, you can explicitly specify them by passing a list of field names to the DictReader() constructor like this:
import csv

fieldnames = ["country_name", "area", "code2", "code3"]

with open(".\\playground\\country.csv", encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")


# In this example, instead of using values from the first line as the field names, we explicitly pass a list of field names to the DictReader constructor.
