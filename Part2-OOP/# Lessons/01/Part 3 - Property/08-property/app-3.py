"""
The Python property class

- The property class returns a property object. The property() class has the following syntax:

    @@ property(fget=None, fset=None, fdel=None, doc=None)

- The property() has the following parameters:

    fget is a function to get the value of the attribute, or the getter method.
    fset is a function to set the value of the attribute, or the setter method.
    fdel is a function to delete the attribute.
    doc is a docstring i.e., a comment.

"""

from pprint import pprint


# The following uses the property() function to define the age property for the Person class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # (1)
    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    # (2)
    def get_age(self):
        return self._age

    # (3) define the age property for the Person class.
    age = property(fget=get_age, fset=set_age)


# In the Person class, we create a new property object by calling the property() and assign the property object to the age attribute. Note that the age is a class attribute, not an instance attribute.
# The following shows that the Person.age is a property object:
print(Person.age)  # <property object at 0x000001AA0BC47A60>


# The following creates a new instance of the Person class and access the age attribute:
john = Person("John", 18)
print(john.age)  # 18


john.age = 22
print(john.age)  # 22


# The john.__dict__ stores the instance attributes of the john object. The following shows the contents of the john.__dict__ :
print(john.__dict__)  # {'name': 'John', '_age': 18}


# As you can see clearly from the output, the john.__dict__ doesn’t have the age attribute.
# The following assigns a value to the age attribute of the john object:
john.age = 19


# In this case, Python looks up the age attribute in the john.__dict__ first. Because Python doesn’t find the age attribute in the john.__dict__, it’ll then find the age attribute in the Person.__dict__.
# The Person.__dict__ stores the class attributes of the Person class. The following shows the contents of the Person.__dict__:
pprint(Person.__dict__)
"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__init__': <function Person.__init__ at 0x000001D1E4568FE0>,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'age': <property object at 0x000001D1E4567AB0>,
            'get_age': <function Person.get_age at 0x000001D1E49259E0>,
            'set_age': <function Person.set_age at 0x000001D1E4925940>})



- Because Python finds the age attribute in the Person.__dict__, it’ll call the age property object.

- When you assign a value to the age object:

    john.age = 19

- Python will call the function assigned to the fset argument, which is the set_age().
- Similarly, when you read from the age property object, Python will execute the function assigned to the fget argument, which is the get_age() method.

- By using the property() class, we can add a property to a class while maintaining backward compatibility. In practice, you will define the attributes first. Later, you can add the property to the class if needed.




Summary
- Use the Python property() class to define a property for a class.

"""
