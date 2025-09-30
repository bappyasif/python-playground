# polymorphism

# polymorphism is a cocncept of classes sharing methods with same name.
# this becomes useful when there are object inherited from different classes that may share similar methods

# polymorphism with classes
# in python classes are allowed to contain methods that share same name as another method from an another class.

# examples
class Cheking():
    def type(self):
        print("checking account")
    
    def balance(self):
       print('$200 left in your checking.')

class Savings():
    def type(self):
        print("savings account")

    def balance(self):
       print('$2000 left in your savings.')

user = Cheking()
user.type()

user = Savings()
user.type()

print("\n\n")

acc_a = Cheking()
acc_b = Savings()

for account in (acc_a, acc_b):
    account.type()
    account.balance()

#)

class Animal():
    def canspeak(self):
        print("animal speaks")

class Dog():
    def canspeak(self):
        print("dog barks")

class Cat():
    def canspeak(self):
        print("cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

for pet in (animal, dog, cat):
    pet.canspeak()

print("\n\n")

class Human():
    def __init__(self, organic = True):
        self.organic = organic
    
    def can_live(self):
        print(f"Human can live: {self.organic}")

class Robot(Human):
    def __init__(self, organic = False):
        self.organic = organic
        Human.__init__(self, organic)
    
    def can_live(self):
        print(f"Robot can live: {self.organic}")

human = Human()
human.can_live()

robot = Robot()
robot.can_live()

print("\n\n")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal speaks")

    def greet(self):
        print(f"halo {self.name}")

    def special(self):
        print("special method from animal")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
    
    def greet(self):
        print(f"woof {self.name}")

    def special(self):
        print("special method from DOG")


class Cat(Animal):
    def speak(self):
        print("Cat meows")

    def greet(self):
        print(f"meow {self.name}")


# Inheritance example
class Pet(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # def speak(self): # as this is now ommited base class method will be triggered for speak method call from object derived from this class
    #     print("Pet speaks")

    def greet(self):
        print(f"hello {self.name}")



# Polymorphism example
animals = [Dog("Rex"), Cat("Whiskers"), Pet("Fluffy", 2)]
for animal in animals:
    animal.speak()
    animal.greet()
    animal.special()


# Here's a breakdown of the polymorphism and inheritance concepts in the code you provided:

# Base Class: Animal
    # The Animal class is the base class that defines the common attributes and methods for all animal objects.
    # It has an __init__ method that initializes the name attribute.
    # It has a speak method that prints "Animal speaks".
    # It has a greet method that prints "halo {name}".
    # It has a special method that prints "special method from animal".

# Derived Classes: Dog, Cat, Pet
    # The Dog, Cat, and Pet classes inherit from the Animal class using inheritance.
    # Each derived class overrides the speak and greet methods to provide their own implementations.
    # The Dog class overrides the speak method to print "Dog barks".
    # The Dog class overrides the greet method to print "woof {name}".
    # The Dog class overrides the special method to print "special method from DOG".
    # The Cat class overrides the speak method to print "Cat meows".
    # The Cat class overrides the greet method to print "meow {name}".
    # The Pet class overrides the greet method to print "hello {name}".
    # The Pet class adds an additional attribute age and omits the speak method, allowing the base class implementation to be used.

# Polymorphism and Inheritance Example
    # The animals list contains objects of different types (Dog, Cat, Pet).
    # The for loop iterates over the animals list.
    # The speak, greet, and special methods are called on each object.
    # Since the derived classes override the speak and greet methods, different implementations are executed based on the specific type of the object.
    # The special method is called on each object, and the base class implementation is executed because it is not overridden in the derived classes.