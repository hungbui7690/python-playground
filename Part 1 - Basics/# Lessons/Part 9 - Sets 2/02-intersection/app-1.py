"""
Set Intersection
- In Python, you can use the set intersection() method or set intersection operator (&) to intersect two or more sets:

    new_set = set1.intersection(set2, set3)
    new_set = set1 & set2 & set3

- The intersection() method and & operator have the same performance.
- When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.

- The set intersection has many useful applications. For example, you can use set intersections to find the common favorites of two friends on a social networking application or to search for common skills of two or more employees on an HR application.

"""

# 1) Using Python set intersection() method to intersect two or more sets

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

s = s1.intersection(s2)
print(s)  # {'C++', 'Java'}


# 2) Using Python set intersection (&) operator to intersect two or more sets

s = s1 & s2
print(s)  # {'Java', 'C++'}
