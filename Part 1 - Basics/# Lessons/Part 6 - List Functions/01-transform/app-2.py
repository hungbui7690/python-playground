"""
Transform List Elements with Python map() Function


"""

# 1) Using the Python map() function for a list of strings
# The following example uses the map() function to return a new list where each element is transformed into the proper case:

names = ["david", "peter", "jenifer"]
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))  # ['David', 'Peter', 'Jenifer']


# 2) Using the Python map() function to a list of tuples
# Suppose that you have the following shopping cart represented as a list of tuples:

carts = [["SmartPhone", 400], ["Tablet", 450], ["Laptop", 700]]

# And you need to calculate the tax amount for each product with a 10% tax 10%. In addition, you need to add the tax amount to the third element of each item in the list.
# In order to do so, you can use the map() function to create a new element of the list and add the new tax amount to each like this:
TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)
print(
    list(carts)
)  # [['SmartPhone', 400, 40.0], ['Tablet', 450, 45.0], ['Laptop', 700, 70.0]]
