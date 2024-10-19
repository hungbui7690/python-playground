"""
Looping through set elements


"""

# Since a set is an iterable, you can use a for loop to iterate over its elements. For example:

skills = {"Problem solving", "Software design", "Python programming"}

for skill in skills:
    print(skill)


# To access the index of the current element inside the loop, you can use the built-in enumerate() function:

for index, skill in enumerate(skills):
    print(f"{index}. {skill}")


# By default, the index starts at zero. To change this, you pass the starting value to the second argument of the enumerate() function. For example:

for index, skill in enumerate(skills, 1):
    print(f"{index} - {skill}")

# Notice that every time you run the code, you’ll get the set elements in a different order.


""" 
    Summary

        A set is an unordered collection of immutable elements.

"""
