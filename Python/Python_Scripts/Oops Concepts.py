#Encapsulation
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")

my_car = Car("Toyota", "Blue")
my_car.display_info()
#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy")
print(my_dog.name)
my_dog.bark()
#polymorphism
class Bird:
    def make_sound(self):
        pass

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp chirp!")

class Crow(Bird):
    def make_sound(self):
        print("Caw caw!")

def make_bird_sound(bird):
    bird.make_sound()

sparrow = Sparrow()
crow = Crow()

make_bird_sound(sparrow)
make_bird_sound(crow)

#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())
