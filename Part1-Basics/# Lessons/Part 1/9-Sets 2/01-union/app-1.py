"""
Set Union
- pic

- union two or more sets by using the Python set union() or set union operator (|).
- returns a new set that consists of distinct elements from both set1 and set2.

- In Python, to union two or more sets, you use the union() method:

        new_set = set.union(another_set, ...)

- Python provides you with the set union operator | that allows you to union two sets:

        new_set = set1 | set2



"""

# The following example shows how to union the s1 and s2 sets:

s1 = {"Python", "Java"}
s2 = {"C#", "Java"}

s = s1.union(s2)

print(s)  # {'C#', 'Java', 'Python'}


# The following example shows how to use the union operator (|) to union the s1 and s2 sets:

s1 = {"Python", "Java", "Go"}
s2 = {"C#", "Java", "Go"}

s = s1 | s2

print(s)  # {'Java', 'C#', 'Python', 'Go'}
