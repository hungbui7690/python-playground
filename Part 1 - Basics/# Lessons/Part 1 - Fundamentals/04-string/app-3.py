'''
String
- A string is a series of characters. 

'''

# Using variables in Python strings with the f-strings
# Sometimes, you want to use the values of variables in a string.

# For example, you may want to use the value of the name variable inside the message string variable:
name = 'John'

# To do it, you place the letter f before the opening quotation mark and put the brace around the variable name:
message = f'Hi {name}'
print(message)
# Python will replace the {name} by the value of the name variable.