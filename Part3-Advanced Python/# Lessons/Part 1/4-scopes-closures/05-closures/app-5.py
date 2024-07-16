"""
Returning an inner function


"""


# To find the free variables that a closure contains, you can use the __code__.co_freevars, for example:


def say():
    greeting = "Hello"

    def display():
        print(greeting)

    return display


fn = say()
print(fn.__code__.co_freevars)  # ('greeting',)

# In this example, the fn.__code__.co_freevars returns the greeting free variable of the fn closure.
