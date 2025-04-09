 # Constructors (__init__ methods) allow each object to start with specific values. It’s like building a pizza 🍕 with the toppings you want! 

class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
Car1 = Car("blue", "BMW")
car2 = Car("red", "SUV")
print(Car1.color)
print(car2.color)