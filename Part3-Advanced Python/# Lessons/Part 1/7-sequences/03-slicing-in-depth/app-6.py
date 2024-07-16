"""
The indices method

- A slice object essentially defines a sequence of indices for selecting elements of a sequence.

- To make it more convenient, the slice type has the indices method that returns the equivalent range (start, stop, step) for any slice of a sequence with a specified length:

      slice(start, stop, step).indices(length)

- It returns a new tuple:

      (i, j, k)

"""


# And you can use the values of this tuple to generate a list of indices using the range function. For example:

colors = ["red", "green", "blue", "orange"]

s = slice(0, 4, 2)
t = s.indices(len(colors))

print(t)  # (0, 4, 2) > return tuple

for index in range(*t):
    print(colors[index])
