"""
S – Single responsibility Principle


"""


# To make it more convenient, you can use the facade pattern so that the Person class will be the facade for the PersonDB class like this:
class PersonDB:
    def save(self, person):
        print(f"Save the {person} to the database")


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f"Person(name={self.name})"

    def save(self):
        self.db.save(person=self)


if __name__ == "__main__":
    p = Person("John Doe")
    p.save()


# Summary
# The single responsibility principle (SRP) states that every class, method, or function should have only one job or one reason to change.
# Use the single responsibility principle to separate classes, methods, and functions with the same reason for changes.
