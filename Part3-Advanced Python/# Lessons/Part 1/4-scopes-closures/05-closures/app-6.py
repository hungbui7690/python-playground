"""
When Python creates the closure

- Python creates a new scope when a function executes. If that function creates a closure, Python also creates a new closure as well.

"""


# First, define a function called multiplier that returns a closure:
def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


# The multiplier function returns the multiplication of two arguments. However, it uses a closure instead.
# Second, call the multiplier function three times:
m1 = multiplier(1)
m2 = multiplier(2)
m3 = multiplier(3)


# These function calls create three closures. Each function multiplies a number with 1, 2, and 3.
# Third, execute functions of the closures:
print(m1(10))  # 10
print(m2(10))  # 20
print(m3(10))  # 30

# The m1, m2, and m3 have different instances of closure.
