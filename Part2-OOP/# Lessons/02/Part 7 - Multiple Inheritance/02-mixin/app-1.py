"""
What is a mixin in Python

- A mixin is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an is-a relationship.

- A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.

- A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, implementing closely related methods.

- Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.

- Since Python doesn’t define a formal way to define mixin classes, it’s a good practice to name mixin classes with the suffix Mixin.

- A mixin class is like an interface in Java and C# with implementation. And it’s like a trait in PHP.


"""


# First, define a Person class:
class Person:
    def __init__(self, name):
        self.name = name


# Second, define an Employee class that inherits from the Person class:
class Employee(Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


# Third, create a new instance of the Employee class:
if __name__ == "__main__":
    e = Employee(
        name="John",
        skills=["Python Programming" "Project Management"],
        dependents={"wife": "Jane", "children": ["Alice", "Bob"]},
    )


# Suppose you want to convert the Employee object to a dictionary. To do that, you can add a new method to the Employee class, which converts the object to a dictionary.
