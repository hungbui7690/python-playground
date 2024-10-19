"""
Python Closures

"""

# n Python, you can define a function from the inside of another function. And this function is called a nested function. For example:


def say():
    greeting = "Hello"

    def display():
        print(greeting)

    display()


"""
In this example, we define the display function inside the say function. The display function is called a nested function.

Inside the display function, you access the greeting variable from its nonlocal scope.

Python calls the greeting variable a free variable.

When you look at the display function, you actually look at:

    The display function itself.
    And the free variable greeting with the value 'Hello'.

So the combination of the display function and greeting variable is called a closure: pic-1

** By definition, a closure is a nested function that references one or more variables from its enclosing scope.

"""
