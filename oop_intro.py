# introduction to oop

# programming paradigm: a way to classify different programming languages and unique features that they offered

# as we explore python deeper our code might fall into multiple paradigm categories at once. this is because most mordern day languages offer more than once specific paradigm we can program in, one of which is OOP

# OOP:
# there must be ability to create programs around classes and objects
# is a paradigm which uses classes and objects to group data and behavior together

class Dog:
    sound = "woof"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return self.sound + " " + Dog.sound
    
dog = Dog("Fido", 3)
print(dog.name)
print(dog.age)
print(dog.bark())

# obsrevbations:
# in above example we are representing a real world entity as a class with properties and methods
# these features make up core of OOP paradigm that which ultimately allows us to build more intricate programs
# with features like inheritance, polymorphism, abstraction and ancapsulations we can do much more than just simple entity objects

# exerceise:

class Employee:
    new_id = 1

    # def __init__(self):
    #     self.id = self.new_id
    #     self.new_id += 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()
