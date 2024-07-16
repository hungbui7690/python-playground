"""
Returning an inner function
- Python cells and multi-scoped variables

- The value of the greeting variable is shared between two scopes of:

    The say function.
    The closure

- The label greeting is in two different scopes. However, they always reference the same string object with the value 'Hello'.

- To achieve this, Python creates an intermediary object called a cell: pic-3

"""


def say():
    greeting = "Hello"

    def display():
        print(greeting)

    return display


fn = say()
fn()


# To find the memory address of the cell object, you can use the __closure__ property as follows:
print(fn.__closure__)
# (<cell at 0x000001E8CA5AAB90: str object at 0x000001E8CA5B5170>,)
# The __closure__ returns a tuple of cells.
# In this example, the memory address of the cell is 0x0000017184915C40. It references a string object at 0x0000017186A829B0.
