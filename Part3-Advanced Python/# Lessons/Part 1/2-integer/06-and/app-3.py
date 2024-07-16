"""
Python and operator

  sum(iterable, start)

- start: Optional - A value that is added to the return value

"""

# The following defines the avg() function that calculates the average of numbers:


def avg(*numbers):
    total = sum(numbers)
    n = len(numbers)

    # Method 1
    # if n > 0:
    #     return total / n

    # Method 2
    return n and total / n

    return 0


if __name__ == "__main__":
    print(avg(1, 2, 3))

# 2.0
