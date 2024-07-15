'''
String

'''

# Accessing string elements
# Since a string is a sequence of characters, you can access its elements using an index. The first character in the string has an index of zero.
# The following example shows how to access elements using an index:

str = "Python String"
print(str[0]) # P
print(str[1]) # y
'''
How it works:

    First, create a variable that holds a string "Python String".
    Then, access the first and second characters of the string by using the square brackets [] and indexes.
'''


# If you use a negative index, Python returns the character starting from the end of the string. For example:
str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

'''
The following illustrates the indexes of the string "Python String":

+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 

'''