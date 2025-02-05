"""
Define class method

- Like a class attribute, a class method is shared by all instances of the class. The first argument of a class method is the class itself.

- By convention, its name is "cls".

- Python automatically passes this argument to the class method. Also, you use the @classmethod decorator to decorate a class method.



@@ @classmethod
@@    def create_anonymous(cls):

@@ cls === Person

"""


# The following example defines a class method that returns an anonymous Person object:
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous", 22)  # Method 1
        # return Person("Anonymous", 22) # Method 2


# The following shows how to call the create_anonymous() class method:
anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous
