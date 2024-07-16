"""
Open–closed principle
- To make the PersonStorage class conforms with the open-closed principle; you need to design the classes so that when you need to save the Person’s object into a different file format, you don’t need to modify it.

- See the following class diagram:

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
                      ^
        ^       +------------+
        |       | PersonJSON |
        |       +------------+
        |       | + save()   |
        |       +------------+
  +----------+
  | PersonDB |
  +----------+
  | + save() |
  +----------+

"""

from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"


# First, define the PersonStorage abstract class that contains the save() abstract method:
class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


# Second, create two classes PersonDB and PersonJSON that save the Person object into the database and JSON file. These classes inherit from the PersonStorage class:
class PersonDB(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to database")


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to a JSON file")


"""
To save the Person object into an XML file, you can define a new class PersonXML that inherits from the PersonStorage class like this:

      +--------+
      | Person |
      +--------+
      | + name |
      +--------+
          ^
    +------------------+     +-----------+
    | PersonStorage    |     | PersonXML |
    +------------------+  <- +-----------+
    | + save_to_db()   |     | + save()  |
    +------------------+     +-----------+
    | + save_to_json() |
    +------------------+
                      ^
        ^       +------------+
        |       | PersonJSON |
        |       +------------+
        |       | + save()   |
        |       +------------+
  +----------+    
  | PersonDB |
  +----------+
  | + save() |
  +----------+

"""


class PersonXML(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to an XML file")


# And you can save the Person‘s object into an XML file using the PersonXML class:
if __name__ == "__main__":
    person = Person("John Doe")
    storage = PersonXML()
    storage.save(person)
# Save the Person(name=John Doe) to an XML file


# Summary
# The open-closed principle allows you to design the system so that it is open for extension but closed for modification.
