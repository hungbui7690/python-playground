"""
id
- to get the identity of an object
- The id() function accepts an object and returns an integer that identifies that object:

    id(object)

- The returned integer is unique and doesn’t change during the lifetime of the object.

"""

# In Python, everything is an object including a number, a string, etc. For example:
x = 10
print(id(x))  # 2304409666064
# In this example, we define a variable x and set it to 10. Internally, Python creates a new integer object and references x to that object in the memory.
# The id(x) returns an integer (2523002569232) that is corresponding to the memory address of the object that x references.
# Note that you’ll see a different integer number every time you run the program.


# To convert the memory address from an integer to hexadecimal, you use the hex() function:
x = 10
print(id(x))  # 2304409666064
print(hex(id(x)))  # 0x24b6eac0210


# The following defines two variables x and y and assigns 10 to both:
x = 10
y = 10
print(id(x) == id(y))  # True


"""
In this case, Python creates only one integer object with the value of 10 and references both the x and y variables to it. Therefore, the identity of the object that x and y reference is the same:

+---------------+
| 10            |
+---------------+
| 0x24b6eac0210 |
+---------------+
    ^   ^
+----+ +---+
| X  | | Y |
+----+ +---+

"""


# Python does the same way for string objects. For example:
a = "Python"
b = "Python"
print(id(a) == id(b))  # True
