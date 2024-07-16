"""
Interface Segregation Principle
- An interface is a description of behaviors that an object can do. For example, when you press the power button on the TV remote control, it turns the TV on, and you don’t need to care how.

- In object-oriented programming, an interface is a set of methods an object must-have. The purpose of interfaces is to allow clients to request the correct methods of an object via its interface.

- Python uses abstract classes as interfaces because it follows the so-called duck typing principle. The duck typing principle states that “if it walks like a duck and quacks like a duck, it must be a duck.” In other words, the methods of a class determine what its objects will be, not the type of the class.

- The interface segregation principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing.

- It doesn’t mean that the interface should have one method. An interface can have multiple cohesive methods.

- For example, the Database interface can have the connect() and disconnect() methods because they must go together. If the Database interface doesn’t use both methods, it’ll be incomplete.

- Uncle Bob, who is the originator of the SOLID term, explains the interface segregation principle by advising that “Make fine-grained interfaces that are client-specific. Clients should not be forced to implement interfaces they do not use.”


- Consider the following example:

      +---------+
      | Movable |
      +---------+
      | + go()  |
      +---------+
        ^       ^
+----------+    +---------+
| Flyable  |    | Car     |
+----------+    +---------+
| + fly()  |    | + go()  |
+----------+    +---------+
      ^
+----------+
| Aircraft |
+----------+
| + go()   |
+----------+
| + fly()  |
+----------+

"""

from abc import ABC, abstractmethod


# First, split the Vehicle interface into two smaller interfaces: Movable and Flyable, and inherits the Movable class from the Flyable class:
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


# Second, inherits from the Flyable class from the Aircraft class:
class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


# Third, inherit the Movable class from the Car class:
class Car(Movable):
    def go(self):
        print("Going")


# In this design, the Car only need to implement the go() method that it needs. It doesn’t need to implement the fly() method that it doesn’t use.


# Summary
# The interface segregation principle advises that the interfaces should be small in terms of cohesions.
# Make fine grained interfaces that are client-specific. Clients should not be forced to implement interfaces they do not use.
