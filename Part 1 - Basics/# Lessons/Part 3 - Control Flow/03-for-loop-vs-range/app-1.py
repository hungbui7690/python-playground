"""
for Loop with Range

    for index in range(n):
      statement

  - The range(n) generates a sequence of n integers starting at zero. It increases the value by one until it reaches n.
  - So the range(n) generates a sequence of numbers: 0,1, 2, …n-1. Note that it’s always short of the final number (n).

  - 3 ways to use range:
    range(stop)
    range(start, stop)
    range(start, stop, step)


"""

# The following example shows how to use the for loop with the range() function to display 5 numbers from 0 to 4 to the screen:
for index in range(5):
    print(index)


# range(start, stop)
# The following example uses a for loop to show five numbers, from 1 to 5 to the screen:
for index in range(1, 6):
    print(index)


# The following example shows all the odd numbers from 0 to 10:
for index in range(0, 11, 2):
    print(index)
