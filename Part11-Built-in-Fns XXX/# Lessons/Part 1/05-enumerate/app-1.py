"""
enumerate
- use it to enumerate a sequence, iterator, or any other object that supports iteration.
- The enumerate() is a built-in function with the following syntax:

    enumerate(iterable, start=0)

- The enumerate() function accepts two arguments:

    iterable is a sequence, an iterator, or any object that supports the iterable protocol.
    start is the starting number from which the function starts counting. It defaults to zero.

- The enumerate() function returns an enumerate object. The __next__() method of the returned enumerate object returns a tuple that contains a count and the value obtained from iterating over the iterable.

"""

# The following example defines a list of fruits and uses the for-in loop to iterate over the list elements and print them out:
fruits = ["Apple", "Orange", "Strawberry"]

for fruit in fruits:
    print(fruit)


# It works fine as expected.
# Sometimes, you want to add indices to the output. To do that, you may come up with a loop counter like this:
fruits = ["Apple", "Orange", "Strawberry"]
index = 1

for fruit in fruits:
    print(f"{index}.{fruit}")
    index += 1


# In this example, the index keeps track of the indices. This example also works as expected. But Python has a better solution with the enumerate() function:
fruits = ["Apple", "Orange", "Strawberry"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index} - {fruit}")

# With the enumerate() function, you can achieve the same result with less code. Also, you don’t need to keep track of the index by increasing it in each iteration.
