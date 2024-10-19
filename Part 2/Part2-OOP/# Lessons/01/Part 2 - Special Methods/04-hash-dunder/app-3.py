"""
Python __hash__


"""


# To make the Person class hashable, you also need to implement the __hash__ method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


members = {Person("John", 22), Person("Jane", 22)}
print(members)  # {<__main__.Person object at 0x000002938BC0F990>}

print(hash(Person("John", 22)))  # 22
