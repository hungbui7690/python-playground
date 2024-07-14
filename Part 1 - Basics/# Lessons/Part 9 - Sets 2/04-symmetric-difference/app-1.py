"""
Symmetric Difference
- The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.

- Suppose that you have the following s1 and s2 sets:

    s1 = {'Python', 'Java', 'C++'}
    s2 = {'C#', 'Java', 'C++'}

- The symmetric difference of the s1 and s2 sets returns in the following set:

    {'C#', 'Python'}

"""


# 1) Using the symmetric_difference() method to find the symmetric difference of sets

# The Set type has the symmetric_difference() method that returns the symmetric difference of two or more sets:
#   new_set = set1.symmetric_difference(set2, set3,...)

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

s = s1.symmetric_difference(s2)
print(s)  # {'C#', 'Python'}


# 2) Using the symmetric difference operator(^) to find the symmetric difference of sets

# Besides using the set symmetric_difference() method, you can use the symmetric difference operator (^) to find the symmetric difference between two or more sets:
#   new_set = set1 ^ set2 ^...

s = s1 ^ s2
print(s)  # {'Python', 'C#'}
