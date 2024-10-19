"""
Method resolution order (MRO)

- When the parent classes have methods with the same name and the child class calls the method, Python uses the method resolution order (MRO) to search for the right method to call. Consider the following example:


+------------+    +----------+
| Flyable    |    | Car      |
+------------+    +----------+
| + start()  |    | + start()|
+------------+    +----------+
| + fly()    |    | + go()   |
+------------+    +----------+
          ^           ^
          +-----------+
          | FlyingCar |
          +-----------+
          | + start() |
          +-----------+



"""


# First, add the start() method to the Car, Flyable, and FlyingCar classes. In the start() method of the FlyingCar class, call the start() method of the super():
class Car:
    def start(self):
        print("Start the Car")

    def go(self):
        print("Going")


class Flyable:
    def start(self):
        print("Start the Flyable object")

    def fly(self):
        print("Flying")


class FlyingCar(Flyable, Car):
    def start(self):
        super().start()


# Second, create an instance of the FlyingCar class and call the start() method:
if __name__ == "__main__":
    car = FlyingCar()
    car.start()  # Start the Flyable object


# As you can see clearly from the output, the super().start() calls the start() method of the Flyable class.
# The following shows the __mro__ of the FlyingCar class:
print(FlyingCar.__mro__)
# (<class '__main__.FlyingCar'>, <class '__main__.Flyable'>, <class '__main__.Car'>, <class 'object'>)


# From left to right, you’ll see the FlyingCar, Flyable, Car, and object.
# Note that the Car and Flyable objects inherit from the object class implicitly. When you call the start() method from the FlyingCar‘s object, Python uses the __mro__ class search path.
# Since the Flyable class is next to the FlyingCar class, the super().start() calls the start() method of the FlyingCar class.
