"""
Python __bool__


"""


# For example, suppose that you want the person object to evaluate False if the age of a person is under 18 or above 65:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True


if __name__ == "__main__":
    person = Person("Jane", 16)
    print(bool(person))  # False

# In this example, the __bool__ method returns False if the age is less than 18 or greater than 65. Otherwise, it returns True. The person object has the age value of 16 therefore it returns False in this case.
