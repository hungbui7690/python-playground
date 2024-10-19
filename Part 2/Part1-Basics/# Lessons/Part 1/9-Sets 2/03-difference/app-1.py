"""
Set Difference
- find the difference between two or more sets.

- The Set type has a difference() method that returns the difference between two or more sets:

        set1.difference(s2, s3, ...)

"""

# For example, you can use the set difference() method to find the difference between s1 and s2 sets:

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}
s = s1.difference(s2)

print(s)  # {'Python'}


# And this example shows how to use the set difference() method to find the difference between s2 and s1 sets.

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}
s = s2.difference(s1)

print(s)  # {'C#'}
