# Inheritance is where by an object inherits properties from a parent class.
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)