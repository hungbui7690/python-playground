"""
STATIC METHODS

Introduction to Python static methods

- So far, you have learned about instance methods that are bound to a specific instance. It means that instance methods can access and modify the state of the bound object.

- Also, you learned about class methods that are bound to a class. The class methods can access and modify the class state.

- Unlike instance methods, static methods aren’t bound to an object. In other words, static methods cannot access and modify an object state.

- In addition, Python doesn’t implicitly pass the cls parameter (or the self parameter) to static methods. Therefore, static methods cannot access and modify the class’s state.

- In practice, you use static methods to define utility methods or group functions that have some logical relationships in a class.


"""


# To define a static method, you use the @staticmethod decorator:


class className:
    @staticmethod
    def static_method_name(param_list):
        pass


# To call a static method, you use this syntax:
# className.static_method_name()


"""
Python static methods vs class methods

- Since static methods are quite similar to the class methods, you can use the following to find the differences between them:

    Class Methods	                                            Static Methods
    Python implicitly pass the cls argument to class methods.	Python doesn’t implicitly pass the cls argument to static methods
    Class methods can access and modify the class state.	    Static methods cannot access or modify the class state.
    Use @classmethod decorators to define class methods         Use @staticmethod decorators to define static methods.

"""
