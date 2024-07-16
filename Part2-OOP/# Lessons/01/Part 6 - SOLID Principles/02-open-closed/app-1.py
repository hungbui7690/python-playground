"""
Open–closed principle
- The open-closed principle states that a class, method, and function should be open for extension but closed for modification.

- The open-closed principle sounds contradictory.

- The purpose of the open-closed principle is to make it easy to add new features (or use cases) to the system without directly modifying the existing code.

- Consider the following example:

      +--------+
      | Person |
      +--------+
      | + name |
      +--------+
          ^
    +------------------+
    | PersonStorage    |
    +------------------+
    | + save_to_db()   |
    +------------------+
    | + save_to_json() |
    +------------------+

"""


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"


class PersonStorage:
    def save_to_database(self, person):
        print(f"Save the {person} to database")

    def save_to_json(self, person):
        print(f"Save the {person} to a JSON file")


if __name__ == "__main__":
    person = Person("John Doe")
    storage = PersonStorage()
    storage.save_to_database(person)


"""
In this example, the PersonStorage class has two methods:

    The save_to_database() method saves a person to the database.
    The save_to_json() method saves a person to a JSON file.

Later, if you want to save the Person’s object into an XML file, you must modify the PersonStorage class. It means that the PersonStorage class is not open for extension but modification. Hence, it violates the open-closed principle.
"""
