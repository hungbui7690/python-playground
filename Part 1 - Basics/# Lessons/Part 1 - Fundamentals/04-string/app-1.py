'''
String
- A string is a series of characters. 
- In Python, anything inside quotes is a string. And you can use either single or double quotes

'''

# If a string contains a single quote, you should place it in double-quotes like this:
message = "It's a string"
print(message)

# And when a string contains double quotes, you can use the single quotes:
message = '"Beautiful is better than ugly.". Said Tim Peters'
print(message)

# To escape the quotes, you use the backslash (\). For example:
message = 'It\'s also a valid string'
print(message)

# The Python interpreter will treat the backslash character (\) special. If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote. For example:
message = r'C:\python\bin'
print(message)