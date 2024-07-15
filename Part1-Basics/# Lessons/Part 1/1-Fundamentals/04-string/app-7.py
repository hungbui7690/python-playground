'''
String

'''

# Python strings are immutable
# Python strings are immutable. It means that you cannot change the string. For example, you’ll get an error if you update one or more characters in a string:
str = "Python String" 
# str[0] = 'J' # error: 'str' object does not support item assignment

# When want to modify a string, you need to create a new one from the existing string. For example:
new_str = 'J' + str[1:]
print(new_str)

'''
  Summary

      In Python, a string is a series of characters. Also, Python strings are immutable.
      Use quotes, either single quotes or double quotes to create string literals.
      Use the backslash character \ to escape quotes in strings
      Use raw strings r'...' to escape the backslash character.
      Use f-strings to insert substitute variables in literal strings.
      Place literal strings next to each other to concatenate them. And use the + operator to concatenate string variables.
      Use the len() function to get the size of a string.
      Use the str[n] to access the character at the position n of the string str.
      Use slicing to extract a substring from a string.
'''