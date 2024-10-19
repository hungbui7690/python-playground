"""
- Python uses the type class to create other classes. The type class itself is a callable. The following shows one of the constructors of the type class:

    type(name, bases, dict) -> a new type

- The constructor has three parameters for creating a new class:

    + name: is the name of the class e.g., Person
    + bases is a tuple that contains the base classes of the new class. For example, the Person inherits from the object class, so the bases contains one class (object,)
    + dict is the class namespace

- Technically, you can use the type class to create a class dynamically. Before doing it, you need to understand how Python creates the classes.

- When the Python interpreter encounters a class definition in the code, it will:

    First, extract the class body as string.
    Second, create a class dictionary for the class namespace.
    Third, execute the class body to fill up the class dictionary.
    Finally, create a new instance of type using the above type() constructor.

- Let’s emulate the steps above to create a Person class dynamically:

"""

from pprint import pprint

# First, extract the class body:
class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def greeting(self):
    return f'Hi, I am {self.name}. I am {self.age} year old.'
"""


# Second, create a class dictionary:
class_dict = {}


# Third, execute the class body and fill up the class dictionary:
exec(class_body, globals(), class_dict)


# Finally, create a new Person class using the type constructor:
Person = type("Person", (object,), class_dict)


# Note that the Person is a class, which is also an object. The Person class inherits from the object class and has the namespace of the class_dict.


# The following shows the type of the Person class which is the type class:
print(type(Person))  # <class 'type'>


# And it is an instance of the type class:
print(isinstance(Person, type))  # True


# The class_dict has the two functions __init__ and greeting:
pprint(Person.__dict__)

"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__init__': <function __init__ at 0x000001B9F6BD8FE0>,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'greeting': <function greeting at 0x000001B9F6F91940>})
"""


"""
In this example, Python creates the type class dynamically, which is the same as the one that you define statically in the code.

Because the type class creates other classes, we often refer to it as a metaclass. A metaclass is a class used to create other classes.

\\\\\\\\\\\\\\\

Summary

- In Python, a class is an instance of the type class.
- The type class creates other classes, therefore, it is called a metaclass.

"""
