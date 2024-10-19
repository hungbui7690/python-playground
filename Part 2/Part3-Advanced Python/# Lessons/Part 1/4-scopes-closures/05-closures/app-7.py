"""
Python closures and for loop

"""


# Suppose that you want to create all three closures above at once and you might come up with the following:

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y: x * y)

m1, m2, m3 = multipliers

print(m1(10))  # 30
print(m2(10))  # 30
print(m3(10))  # 30

"""
How it works.
  First, declare a list that will store the closures.
  Second, use a lambda expression to create a closure and append the closure to the list in each iteration.
  Third, unpack the closures from the list to the m1, m2, and m3 variables.
  Finally, pass the values 10, 20, and 30 to each closure and execute it.


This doesn’t work as you expected. But why?
- The x starts from 1 to 3 in the loop. After the loop, its value is 3.
- Each element of the list is the following closure:

    lambda y: x*y

- Python evaluates x when you call the m1(10), m2(10), and m3(10). At the moment the closures execute, x is 3.
- That’s why you see the same result when you call m1(10), m2(10), and m3(10). 
"""


# To fix this, you need to instruct Python to evaluate x in the loop:


def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


multipliers = []
for x in range(1, 4):
    multipliers.append(multiplier(x))

m1, m2, m3 = multipliers

print(m1(10))  # 10
print(m2(10))  # 20
print(m3(10))  # 30
