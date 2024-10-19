"""
Method resolution order (MRO)


"""


# If you flip the order of Flyable and Car classes in the list, the __mro__ will change accordingly. For example:
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


class FlyingCar(Car, Flyable):
    def start(self):
        super().start()


if __name__ == "__main__":
    car = FlyingCar()
    car.start()  # Start the Flyable object


# (<class '__main__.FlyingCar'>, <class '__main__.Flyable'>, <class '__main__.Car'>, <class 'object'>)
print(FlyingCar.__mro__)
# (<class '__main__.FlyingCar'>, <class '__main__.Car'>, <class '__main__.Flyable'>, <class 'object'>)


# In this example, the super().start() calls the start() method of the Car class instead, based on their orders in the method order resolution.
