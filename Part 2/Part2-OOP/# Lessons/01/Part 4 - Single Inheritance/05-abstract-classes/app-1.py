"""
ABSTRACT CLASSES

Introduction to Python Abstract Classes

- In object-oriented programming, an abstract class is a class that cannot be instantiated. However, you can create classes that inherit from an abstract class.

- Typically, you use an abstract class to create a blueprint for other classes.

- Similarly, an abstract method is an method without an implementation. An abstract class may or may not include abstract methods.

- Python doesn’t directly support abstract classes. But it does offer a module that allows you to define abstract classes.



"""

# To define an abstract class, you use the abc (abstract base class) module.
# The abc module provides you with the infrastructure for defining abstract base classes.
# To define an abstract method, you use the @abstractmethod decorator:
from abc import ABC, abstractmethod


class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass
