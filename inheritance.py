# inheritance

# inheritance is a feature of oop that enables transfer of methods and properties of one class to another.
# inheritance allows for reusability of code.
# inheritance is a way of creating a new class that is a modified or extended version of an existing class.

# parent class

# parent class aks base class is a class whose methods and properties we want to transfer in child classes.
# we can define a parent class by using 'class' keyword as any other classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"Name: {self.name}, Age:  {self.age}")

p = Person("bappy", 20)
p.print_info()

# child class

# child class is a class that is derived class from its parent class.
# child class inherits methods and properties from parent class.
# child classes must contain following name of parent class in definition of child class.

class Student(Person):
    def __init__(self, name, age, subject):
        self.subject = subject

        # either of these works as well
        # Person.__init__(self, name, age)
        super().__init__(name, age) # with using super() or Person.__init__() child class will not have access to parent class methods and properties

    def print_info(self):
        print(f"Name: {self.name}, Age:  {self.age}, Subject: {self.subject}")

s = Student("bappy", 20, "python")
s.print_info()

# example

class House:
    def __init__(self, window, door):
        self.window = window
        self.door = door
    
    def print_info(self):
        print(f"Window: {self.window}, Door: {self.door}")

const = House(4, 2)
const.print_info()

class Apartment(House):
    def __init__(self, window, door, floor, unit):
        self.floor = floor
        self.unit = unit

        House.__init__(self, window, door)

    def print_info(self):
        print(f"Window: {self.window}, Door: {self.door}, Floor: {self.floor}, Unit: {self.unit}")

apt = Apartment(4, 2, 3, 1)
apt.print_info()