"""
zip
- to perform parallel iterations on multiple iterables.
- The following shows the syntax of the zip() function:

    zip(*iterables, strict=False)

- The zip() function iterates multiple iterables in parallel and returns the tuples that contain elements from each iterable.

- In other words, the zip() function returns an iterator of tuples where i-th tuple contains the i-th element from each input iterable.

"""

# Suppose you have two tuples: names and ages.
"""
    The names tuple stores a list of names.
    The ages tuple stores a list of ages.
"""
# To map names and ages from these tuples one-by-one in sequence, you may use the enumerate() function. For example:
names = ("John", "Jane", "Alice")
ages = (20, 22, 25)

for index, name in enumerate(names):
    print((name, ages[index]))

# So John is 20, Jane is 22, and Alice is 25
# However, It’s getting more complicated if the sizes of the names and ages tuples are different. That’s why the zip() function comes to play.


for employee in zip(names, ages):
    print(employee)

# In this example, the zip() returns a tuple in each iteration and assigns it to the employee variable. The tuple contains the i-th elements the names and ages tuples.
