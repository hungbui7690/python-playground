"""
Set Difference
- Besides the difference() method, Python provides you with the set difference operator (-) that allows you to find the difference between sets.

        s = s1 - s2

"""

# The following example uses the difference operator (-) to find the difference between the s1 and s2 sets:

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

s = s1 - s2
print(s)  # {'Python'}


# And this example use the set difference operator to return the difference between s2 and s1:

s = s2 - s1
print(s)  # {'C#'}
