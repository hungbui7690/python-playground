"""
Python Class Decorators
- A class instance can be a callable when it implements the __call__ method. Therefore, you can make the __call__ method as a decorator.

"""


# The following example rewrites the star decorator factory using a class instead:
class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n * "*")
            result = fn(*args, **kwargs)
            print(result)
            print(self.n * "*")
            return result

        return wrapper


# And you can use the Star class as a decorator like this:
@Star(5)
def add(a, b):
    return a + b


# The @Star(5) returns an instance of the Star class. That instance is a callable, so you can do something like:
# add = Star(5)(add)
# So you can use callable classes to decorate functions.


add(10, 20)


# Summary
# Use callable classes as decorators by implementing the __call__ method.
# Pass the decorator arguments to the __init__ method.
