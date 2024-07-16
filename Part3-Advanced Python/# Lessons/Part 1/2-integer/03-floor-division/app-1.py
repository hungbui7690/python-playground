"""
Introduction to Python floor division

- Suppose you have a division of two integers:

    101 / 4

- In this division, 101 is called a numerator (N) and 4 is called a denominator (D).

- The integer division 101 / 4 returns 25 with the remainder 1. In other words:

    101 / 4 = 25 with remainder 1

- Or put it in another way:

    101 = 4 * 25 + 1


"""

# Python uses two operators // and % that returns the result of the division:
# The // is called the floor division operator or div. And the % is called the modulo operator or mod.
print(101 // 4)  # 25
print(101 % 4)  # 1

# Both floor division and modulo operators satisfy the following equation:
print(4 * (101 // 4) + (101 % 4))  # 101
print(4 * 25 + 1)  # 101

# Generally, if N is the numerator and D is the denominator, then the floor division and modulo operators always satisfy the following equation:
# N = D * ( N // D) + (N % D)
