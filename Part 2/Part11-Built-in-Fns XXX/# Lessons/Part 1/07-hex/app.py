"""
hex
- convert an integer number to a lowercase hexadecimal string prefixed with 0x.
- The hex() function accepts an integer and converts it to a lowercase hexadecimal string prefixed with 0x.

- Here’s the syntax of the hex() function:

    hex(x)

"""


# The following example uses the hex() function to convert x from an integer (10) to a lowercase hexadecimal string prefixed with 0x:

x = 10
result = hex(10)
print(result)  # 👉 0xa
print(type(result))  # 👉 <class 'str'>


# If x is not an integer, it needs to have an __index__() that returns an integer. For example:
# First, define the MyClass class with a value attribute.
class MyClass:
    # Second, initialize the value in the __init__() method.
    def __init__(self, value):
        self.value = value

    # Third, implement the __index__() method that returns the value.
    def __index__(self):
        return self.value


# Finally, create a new instance of MyClass and pass it to the hex() function.
result = hex(MyClass(10))
print(result)  # 👉 0xa


# Another way to convert an integer to an uppercase or lower hexadecimal string is to use f-strings with a format. For example:
a = 10
h1 = f"{a:#x}"
print(h1)  # 👉 0xa

h2 = f"{a:x}"
print(h2)  # 👉 a

h3 = f"{a:#X}"
print(h3)  # 👉 0XA

h3 = f"{a:X}"
print(h3)  # 👉 A
