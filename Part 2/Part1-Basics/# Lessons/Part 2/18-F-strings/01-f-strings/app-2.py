"""
F-STRINGS

"""

# The following example calls the upper() method to convert the name to uppercase inside the curly braces of an f-string:
name = "John"
s = f"Hello, {name.upper()}!"
print(s)  # Hello, JOHN!


# The following example uses multiple curly braces inside an f-string:
first_name = "John"
last_name = "Doe"
s = f"Hello, {first_name} {last_name}!"
print(s)  # Hello, John Doe!


# This example is equivalent to the above example but uses the join() method:
first_name = "John"
last_name = "Doe"
s = f'Hello, {" ".join((first_name, last_name))}!'

print(s)  # Hello, John Doe!
