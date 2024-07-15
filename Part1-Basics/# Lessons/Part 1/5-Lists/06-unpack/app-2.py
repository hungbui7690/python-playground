"""
Unpacking and packing

- If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

      First, unpack the needed elements to variables.
      Second, pack the leftover elements into a new list and assign it to another variable.

"""


# By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable. For example:

colors = ["red", "blue", "green"]
red, blue, *other = colors

print(red)
print(blue)
print(other)  # ['green']


# Here’s another example:

colors = ["cyan", "magenta", "yellow", "black"]
cyan, magenta, *other = colors

print(cyan)
print(magenta)
print(other)  # ['yellow', 'black']
# This example assigns the first and second elements to variables. It packs the last two elements in a new list and assigns the new list to the other variable.


"""
      Summary

            Unpacking assigns elements of the list to multiple variables.
            Use the asterisk (*) in front of a variable like this *variable_name to pack the leftover elements of a list into another list.
      """
