"""
Generator expressions vs list comprehensions


"""

# The following shows how to use the list comprehension to generate square numbers from 0 to 4:
square_list = [n**2 for n in range(5)]


# And this defines a square number generator:
square_generator = (n**2 for n in range(5))


"""
1) Syntax
- In terms of syntax, a generator expression uses parentheses () while a list comprehension uses the square brackets [].

2) Memory utilization
- A list comprehension returns a list while a generator expression returns a generator object.
- It means that a list comprehension returns a complete list of elements upfront. However, a generator expression returns a list of elements, one at a time, based on request.
- A list comprehension is eager while a generator expression is lazy.
- In other words, a list comprehension creates all elements right away and loads all of them into the memory.
- Conversely, a generator expression creates a single element based on request. It loads only one single element to the memory.

3) Iterable vs iterator
- A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again.
- However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausting when you complete iterating over it.

\\\\\\\\\\\\\\\\\\\

Summary
- Use a Python generator expression to return a generator.

"""
