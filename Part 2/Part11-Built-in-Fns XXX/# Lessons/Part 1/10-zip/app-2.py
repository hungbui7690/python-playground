"""
zip

"""

# The zip() function returns a zip object which is an iterator:
names = ("John", "Jane", "Alice")
ages = (20, 22, 25)
employees = zip(names, ages)

print(employees)  # <zip object at 0x000001D356E9ECC0>
print(type(employees))  # 👉 <class 'zip'>


"""
The zip() is lazy. It means that Python won’t process the elements until you iterate the iterable. To iterate the iterable, you can use:

    Using a for loop
    Calling the next() function
    Wrapping in a list()
"""
employee_list = list(employees)
print(employee_list)  # 👉 [('John', 20), ('Jane', 22), ('Alice', 25)]
