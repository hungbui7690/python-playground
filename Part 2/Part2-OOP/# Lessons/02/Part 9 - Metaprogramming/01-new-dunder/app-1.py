"""
Python __new__
- When you create an instance of a class, Python first calls the __new__ method to create the object and then calls the __init__ method to initialize the object’s attributes.

- The __new__ method is a static method of the object class. It has the following signature:

        object.__new__(class, *args, **kwargs)

- The first argument of the __new__ method is the class of the new object that you want to create.

- The *args and **kwargs parameters must match the parameters of the __init__ method of the class. However, the __new__ method does use them.

- The __new__ method should return a new object of the class. But it doesn’t have to.

- When you define a new class, that class implicitly inherits from the object class. It means that you can override the __new__ static method and do something before and after creating a new instance of the class.

- To create the object of a class, you call the super().__new__() method.

- Technically, you can call the object.__new__() method to create an object manually. However, you need to call the __init__ yourself manually after. Python will not call the __init__ method automatically if you explicitly create a new object using the object.__new__() method.

"""


class Person:
    def __init__(self, name):
        self.name = name


# In Python, a class is callable. When you call the class to create a new object:
person = Person("John")
print(person.name)  # John


# Python will call the __new__() and __init__() methods. It’s equivalent to the following method calls:
personX = object.__new__(Person, "Alex")
print(personX.__dict__)  # {}


personX.__init__("Alex")
print(personX.__dict__)  # {'name': 'Alex'}
print(personX.name)  # Alex

# As you can see clearly from the output, after calling the __new__ method, the person.__dict__ is empty. And after calling the __init__ method, the person.__dict__ contains the name attribute with the value ‘John'.
