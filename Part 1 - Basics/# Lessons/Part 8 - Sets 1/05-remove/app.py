"""
Removing an element from a set
- To remove an element from a set, you use the remove() method:

        set.remove(element)
        set.discard(element)

"""

skills = {"Problem solving", "Software design", "Python programming"}
skills.remove("Software design")

print(skills)  # {'Problem solving', 'Python programming'}


# If you remove an element that doesn’t exist in a set, you’ll get an error (KeyError). For example:

skills = {"Problem solving", "Software design", "Python programming"}
# skills.remove("Java") # KeyError: 'Java'


# To avoid the error, you should use the in operator to check if an element is in the set before removing it:

if "Java" in skills:
    skills.remove("Java")


# To make it more convenient, the set has the discard() method that allows you to remove an element. And it doesn’t raise an error if the element is not in the list:

skills = {"Problem solving", "Software design", "Python programming"}
skills.discard("Java")
