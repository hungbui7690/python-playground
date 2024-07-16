"""
Multiple Inheritance
- When a class inherits from a single class, you have single inheritance. Python allows a class to inherit from multiple classes. If a class inherits from two or more classes, you’ll have multiple inheritance.

- To extend multiple classes, you specify the parent classes inside the parentheses () after the class name of the child class like this:

      class ChildClass(ParentClass1, ParentClass2, ParentClass3):
          pass

- The syntax for multiple inheritance is similar to a parameter list in the class definition. Instead of including one parent class inside the parentheses, you include two or more classes, separated by a comma.

"""


# First, define a class Car that has the go() method:
class Car:
    def go(self):
        print("Going")


# Second, define a class Flyable that has the fly() method:
class Flyable:
    def fly(self):
        print("Flying")


# Third, define the FlyingCar that inherits from both Car and Flyable classes:
class FlyingCar(Flyable, Car):
    pass


# Since the FlyingCar inherits from Car and Flyable classes, it reuses the methods from those classes. It means you can call the go() and fly() methods on an instance of the FlyingCar class like this:
if __name__ == "__main__":
    fc = FlyingCar()
    fc.go()  # Going
    fc.fly()  # Flying
