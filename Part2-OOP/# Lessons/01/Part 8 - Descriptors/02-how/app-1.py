"""
WHAT IS A DESCRIPTOR

A descriptor is an object of a class that implements one of the methods specified in the descriptor protocol.

Descriptors have two types: data descriptor and non-data descriptor.

    A data descriptor is an object of a class that implements the __set__ and/or __delete__ method.
    A non-data descriptor is an object that implements the __get__ method only.

The descriptor type specifies the property lookup resolution that we’ll cover in the next tutorial.



HOW DESCRIPTORS WORK


"""


# The following modifies the RequiredString class to include the print statements that print out the arguments.
class RequiredString:
    def __set_name__(self, owner, name):
        print(f"__set_name__ was called with owner={owner} and name={name}")
        self.property_name = name

    def __get__(self, instance, owner):
        print(f"__get__ was called with instance={instance} and owner={owner}")
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        print(f"__set__ was called with instance={instance} and value={value}")

        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must a string")

        if len(value) == 0:
            raise ValueError(f"The {self.property_name} cannot be empty")

        instance.__dict__[self.property_name] = value


class Person:
    first_name = RequiredString()
    last_name = RequiredString()


"""
The __set_name__ method

- When you compile the code, you’ll see that Python creates the descriptor objects for first_name and last_name and automatically call the __set_name__ method of these objects. Here’s the output:

    __set_name__ was called with owner=<class '__main__.Person'> and name=first_name
    __set_name__ was called with owner=<class '__main__.Person'> and name=last_name


- In this example, the owner argument of __set_name__ is set to the Person class in the __main__ module, and the name argument is set to the first_name and last_name attribute accordingly.

- It means that Python automatically calls the __set_name__ when the owning class Person is created. The following statements are equivalent:

    first_name = RequiredString()

and

    first_name.__set_name__(Person, 'first_name')

- Inside, the __set_name__ method, we assign the name argument to the property_name instance attribute of the descriptor object so that we can access it later in the __get__ and __set__ method:

    self.property_name = name
"""

# The first_name and last_name are the class variables of the Person class. If you look at the Person.__dict__ class attribute, you’ll see two descriptor objects first_name and last_name:
pprint(Person.__dict__)
"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'first_name': <__main__.RequiredString object at 0x0000022A19F6FE90>,
            'last_name': <__main__.RequiredString object at 0x0000022A19F6FF10>})
"""
