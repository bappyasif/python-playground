# abstraction

# when a program starts to get bigm classes might start to share functionality or we may lose sight of purpose of a class inheritance structure
# in order to alleviate issues like this, we can use concept of abstraction

# abstraction helps with design of code by defining necessary behaviors to be implemented within a class structure.
# by doing so, abstraction also helps avoid leaving out or overlapping class functionality as class heirarchies get larger.

# abstraction is a way to hide implementation details from users

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_noise(self):
        pass

class Cat(Animal):
    def make_noise(self):
        print("{} says meow".format(self.name))

class Dog(Animal):
    def make_noise(self):
        print("{} says woof".format(self.name))

kitty = Cat("Fido")
kitty.make_noise() # Fido says meow

doggy = Dog("Rover")
doggy.make_noise() # Rover says woof

# observations:
# in above example we have abstract class Animal and two subclasses Cat and Dog
# abstract class has one attribute name and one abstract method make_noise
# in above Cat and Dog classes inherits from Animal class. and Animal class inherits from ABC class which stands for Abstract Base Class
# and abstract classes are not meant to be instantiated whe doing so would cause an error, they are meant to be inherited from
# using imported decorator @abstractmethod, we can define abstract methods in abstract classes
# abstract method is a method that has no implementation, it is meant to be implemented in subclasses
# when we call make_noise method on instances of Cat and Dog classes, we see different outputs

# abstraction process involves:
# defining abstract classes
# defining abstract methods
# inheriting from abstract classes

# abstraction process above defines what an Animal is but does not allow us to create an instance of Animal, __init__ method still requires name parameter, so we can create instances of Cat and Dog, make_noise() method is still abstract and needs to be implemented in subclasses otherwise it will cause an error

# exercise: 
class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My id is {self.id}")

class Admin(AbstractEmployee):
    def say_id(self):
        print(f"I am an admin. My id is {self.id}")

e1 = Employee()
e2 = Admin()

e1.say_id()
e2.say_id()
