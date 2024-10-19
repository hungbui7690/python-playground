"""
Returning an inner function

"""

# In Python, a function can return a value which is another function. For example:
# Instead of exec display function inside say(), we can return it


def say():
    greeting = "Hello"

    def display():
        print(greeting)

    return display


"""
In this example, the say function returns the display function instead of executing it.

Also, when the say function returns the display function, it actually returns a closure: pic-2
"""

# The following assigns the return value of the say function to a variable fn. Since fn is a function, you can execute it:
fn = say()  # return display() > now, fn = display
fn()  # Hello


"""
The say function executes and returns a function. When the fn function executes, the say function already completes.

In other words, the scope of the say function was gone at the time the fn function executes.

Since the greeting variable belongs to the scope of the say function, it should also be destroyed with the scope of the function.

However, you still see that fn displays the value of the message variable.
"""
