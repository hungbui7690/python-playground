"""
Mutable and Immutable
- In Python, everything is an object. An object has its own internal state. Some objects allow you to change their internal state and others don’t.

- An object whose internal state can be changed is called a mutable object, while an object whose internal state cannot be changed is called an immutable object.

- The following are examples of immutable objects:

    Numbers (int, float, bool,…)
    Strings
    Tuples
    Frozen sets

- And the following are examples of mutable objects:

    Lists
    Sets
    Dictionaries

- User-defined classes can be mutable or immutable, depending on whether their internal state can be changed or not.

"""

# When you declare a variable and assign its an integer, Python creates a new integer object and sets the variable to reference that object:
counter = 100


# To get the memory address referenced by a variable, you use the id() function. The id() function returns a based-10 number:
print(id(counter))  # 140717671523072


# And to convert the base-10 number to hexadecimal, you can use the hex() function:
print(hex(id(100)))  # 0x7ffb62d32300

# In the memory, you have a variable called counter that references an integer object located at the 0x7ffb62d32300 address: pic-1


# The following changes the counter to 200 and displays its value to the screen:
counter = 200
print(counter)

# It seems that the value of the object referenced by the counter variable changes, but it doesn’t.
# In fact, Python creates a new integer object with the value 200 and reassigns the counter variable so that it references the new object like this: pic-2


# The reassignment doesn’t change the value of the first integer object. It just reassigns the reference.
# The following shows the memory address of the new object referenced by the counter variable:
print(id(counter))
print(hex(id(counter)))
