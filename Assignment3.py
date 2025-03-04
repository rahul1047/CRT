# 1. Lambda function to merge two lists into a dictionary
merge_lists = lambda keys, values: dict(zip(keys, values))

# Example usage
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(merge_lists(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}


# 2. Product class with discount calculation
class Product:
    discount_rate = 0.10  # 10% discount

    def _init_(self, name, price):
        self.name = name
        self.price = price

    def discounted_price(self):
        return self.price * (1 - self.discount_rate)


# Example usage
product = Product("Laptop", 50000)
print(product.discounted_price())  # Output: 45000.0


# 3. Shape Inheritance
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  # Output: 78.53981633974483
print(rectangle.area())  # Output: 24


# 4. Multiple Inheritance
class Person:
    def _init_(self, name):
        self.name = name

class Employee:
    def _init_(self, salary):
        self.salary = salary

class Manager(Person, Employee):
    def _init_(self, name, salary, department):
        Person._init_(self, name)
        Employee._init_(self, salary)
        self.department = department


# Example usage
manager = Manager("Alice", 80000, "IT")
print(manager.name, manager.salary, manager.department)  # Output: Alice 80000 IT


# 5. Polymorphism with Animal Sounds
class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())


# Example usage
dog = Dog()
cat = Cat()
cow = Cow()
play_sound(dog)  # Output: Bark
play_sound(cat)  # Output: Meow
play_sound(cow)  # Output: Moo


# 6. Car Rental System
class Vehicle:
    def _init_(self, brand, model, price_per_day):
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day

    def vehicle_info(self):
        return f"{self.brand} {self.model} - {self.price_per_day} per day"

class Car(Vehicle):
    def _init_(self, brand, model, price_per_day, seats):
        super()._init_(brand, model, price_per_day)
        self.seats = seats

class Bike(Vehicle):
    def _init_(self, brand, model, price_per_day, engine_capacity):
        super()._init_(brand, model, price_per_day)
        self.engine_capacity = engine_capacity


# Example usage
car = Car("Toyota", "Camry", 3000, 5)
bike = Bike("Yamaha", "R15", 1500, "150cc")
print(car.vehicle_info())  # Output: Toyota Camry - 3000 per day
print(bike.vehicle_info())  # Output: Yamaha R15 - 1500 per day
