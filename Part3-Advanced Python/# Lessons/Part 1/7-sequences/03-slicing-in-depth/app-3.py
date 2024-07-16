"""
Python Slicing: start and stop bounds

- The slice seq[start:stop] selects elements starting at the index start and stopping at the index stop (excluding the element at the index stop).

- In other words, it returns all elements of the sequence at the index n where n satisfies the following expression:

      start <= n < stop

- When start or stop is greater than the length of the sequence:

      len(seq)

… Python uses len(seq) for the start or stop.

- Both start and stop are optional. The start defaults to 0 and stop defaults to len(seq) when you don’t specify it.

"""

# The following example returns the entire list:

colors = ["red", "green", "blue", "orange"]
print(colors[0:100])  # ['red', 'green', 'blue', 'orange']
# Since the stop bound is 100, Python uses the len(colors) for the stop bound.


# The following example returns an empty list:

colors = ["red", "green", "blue", "orange"]
print(colors[10:])  # []
# Because the start is 10, Python assigns the len(colors) to it.
