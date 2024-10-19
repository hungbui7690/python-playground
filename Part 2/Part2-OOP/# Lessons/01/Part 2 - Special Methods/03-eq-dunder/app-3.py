"""
Python __eq__

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # To fix the issue of comparing with number, you can modify the __eq__ method to check if the object is an instance of the Person class before accessing the age attribute.
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False


john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)
mary = Person("Mary", "Doe", 27)


# And you can now compare an instance of the Person class with an integer or any object of a different type:
john = Person("John", "Doe", 25)
print(john == 20)  # False
