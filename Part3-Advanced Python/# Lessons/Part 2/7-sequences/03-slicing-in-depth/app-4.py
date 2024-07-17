"""
Negative start and stop bounds

"""


# The slice object also accepts negative start and stop bounds. The following example uses the negative start and stop bounds to slice a list:

colors = ["red", "green", "blue", "orange"]

print(colors[-4:-2])  # ['red', 'green']


# To get the 'blue' and 'orange' elements from the colors list, you can combine the negative and positive bounds:

colors = ["red", "green", "blue", "orange"]
print(colors[-2:4])  # ['blue', 'orange']
