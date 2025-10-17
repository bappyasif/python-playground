# encapsulation
# grouping of data and behaviors into an object
# its a process of making data and behavior hidden inside a class they related to
# languages accomplish this with what are called access modifiers like public, private and protected

# we use private and protected to hide data and behavior from other classes
# in general public members can be accessed from anywhere, protected members can only be accessed from within the class and its subclasses, and private members can only be accessed from within the class

# python doesnt have any inbuilt mechanism for encapsulation, however there is a common way to achieve it by using _ and __ variables and methods

# there is a common convention among developers to use single _ to indicate that a member is protected.
# accessing protected memeber outside of module will not cause any error, it is added by developers to inform others taht they should be careful when accessing it in such a way

# similarly we can declare a memeber with double _ (aka name mangling) to indicate that it is private and should not be accessed outside of the class but can be accessed publicly, it is added by developers to inform others to prevent clashing member names of any importing modules

# note that thsi is different than dunder methods, which has two leading and two trailing underscores and is treated as special methods, dudnder methods are not mangled.

# exercise
class Employee:
    def __init__(self):
        self._id = 1
        self.__name = "A B"
    

e = Employee()
print(e._id) # 1

# dir is a built-in function that returns a list of all members of an object including dunder methods
print(dir(e)) 

print(e._Employee__name) # A B

# setters, getters and deleters:
# using setter, getter and deleter functions we can control how a member is accessed and modified, and are one way to implement encapsulation within python, where state of class attributes can be handled in a controlled way within class
# these functions are useful when we want to have more control over how a member is accessed and modified

class Animal:
    def __init__(self, name):
        self._name = name
        self.age = None

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    def del_name(self):
        del self._name
        print("name deleted")
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            raise TypeError("age must be an integer")
    
        # self.age = age

    def del_age(self):
        del self.age
        print("age deleted")

a = Animal("Fido")
print(a.get_name()) # Fido
print(a.get_age()) # None

a.set_name("Rover")
print(a.get_name()) # Rover

a.set_age(3)
print(a.get_age()) # 3

a.del_name()
# print(a.get_name()) # AttributeError: 'Animal' object has no attribute '_name'

a.del_age()
# print(a.get_age()) # AttributeError: 'Animal' object has no attribute 'age'

# observation:
# in above example we are using setter, getter and deleter functions to control how name and age members are accessed and modified
# in setters we can validate the values of name and age before setting them, this is known as validation
# we have a protected member age and a public member name in that class, we can access them from outside the class by using getter and setter functions
# we have there three different types of accessors, setter, getter and deleter functions, setter is used to set the value of a member, getter is used to get the value of a member, deleter is used to delete a member
# in setters we are validating the values of name and age before setting them, this is known as validation
# for deleting a member we can use del keyword, this is known as deleter

# excercise
class Employee:
    new_id = 1

    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be string")
        
    def del_name(self):
        del self._name
        print("name deleted")

e = Employee("A B")
print(e.get_name()) # A B

e.set_name("C D")
print(e.get_name()) # C D

e.del_name()
# print(e.get_name()) # AttributeError: 'Employee' object has no attribute '_name'


# wrap up of OOP pillars:
# we discussed four pillars of OOP, encapsulation, inheritance, polymorphism and abstraction

# inheritance:
# inheritance is a way to create a new class based on an existing class, this is known as inheritance. python allows classes to inherit on multiple levels, meaning a class can inherit from a base class as well as a derived class
# example of this is when we have a base class Animal and a derived class Cat, Cat is a subclass of Animal, and a Cat object can have access to all the attributes and methods of the Animal class, but also has its own attributes and methods
# pyton also supports multiple inheritance, which is when a class inherits from multiple base classes, this allows us to create a class that has access to all the attributes and methods of all the base classes

# polymorphism:
# polymorphism is a concept that allows functions and objects to behave in defferent ways based on context.
# say both a cat and a dog have the same eat method, but the cat will eat fish and the dog will eat meat, when we call the eat method on a cat object it will eat fish and when we call the eat method on a dog object it will eat meat, this can be an example of polymorphism

# abstraction:
# abstraction is a way to hide the implementation details of a class, this is known as abstraction
# python supports abstraction through the use of abstract classes and abstract methods
# python supports concept of abstraction by allowing objects with methods that have same name to be called in generic way
# further more python provides a built-in decorator @abstractmethod to define abstract methods and ABC class to define abstract classes which are not meant to be instantiated and is meant to be inherited from, usually they are used as a base class for other classes or as an interface

# encapsulation:
# encapsulation is a way to control how a member is accessed and modified, this is known as encapsulation
# python supports encapsulation through the use of private and protected members
# python supports concept of encapsulation by allowing objects with private and protected members to be accessed and modified within the class
# further more python provides a built-in decorator @property to define properties
# pythons' approach to encapsulation is unqiue compared to other oop languages, in python all members are publicly accessible by default but there are conventions to indicate that a member is private or protected to inform others that they should be careful when accessing it


# summary:
# encapsulation is a way to control how a member is accessed and modified, this is known as encapsulation
# inheritance is a way to create a new class based on an existing class, this is known as inheritance
# polymorphism is a concept that allows functions and objects to behave in defferent ways based on context.
# abstraction is a way to hide the implementation details of a class, this is known as abstraction

# exercise
from abc import ABC, abstractmethod


class AbstractedEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractedEmployee.new_id
        AbstractedEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class User():
    def __init__(self):
        self._username = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str):
            self._username = username
        else:
            raise TypeError("username must be a string")

    @username.deleter
    def username(self):
        del self._username
        print("username deleted")

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print(f"Adding employee with id: {employee.id}")
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)
    
class Employee(AbstractedEmployee, User):
    def __init__(self, username):
        super().__init__()
        User.__init__(self)
        self._username = username

    def say_id(self):
        print(f"My id is {self.id}")

    def say_username(self):
        print(f"My username is {self.username}")

e1 = Employee("A B")
e2 = Employee("C D")

m = Meeting()
m + e1
m + e2

print(len(m)) # 2

e1.say_id() # My id is 1
e1.say_username() # My username is A B

e2.say_id() # My id is 2
e2.say_username() # My username is C D
