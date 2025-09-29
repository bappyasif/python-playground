# OOP is programming paradigm which allows for organization of code with data states and functionalities.
# code with oop is modular and easy to maintain.

# classes
#  a class is blueprint that encapsulates data and functions for creating objects.
# to define a class use 'class' keyword followed by class name and colon. then in newline we define class body.
class Dog:
    # this is a blank class
    pass

# objects
# an object is an instance of a class.
# which means an object contains everything that class it has instantiated from.

# creating objects
my_dog = Dog()
print(my_dog) # prints object address here

# Constructors and Destructors
# in oop constructors are functions that are called when an object is created.
# destructors are functions that are called when an object is to be deleted.

# constructors
# constructors are special functions that are executed when an object is instantiated.
# in python __init__() method is used as constructor and is called when an object is created.

# init()
#  it is common practice for classes to contain python's built in __init__() method as constructor.
# and its going to be called everytime an object is created from that class.

class ClassSchedule:
    def __init__(self, course):
        self.course = course
        # self parameter in __init__() method refers to current instance and instance variable 'course' allows for input to assign a value.

# we can create a class instance by calling class with value for course as argument value.
first = ClassSchedule("Python")
print(first.course)

# destructors
# destructors are special functions that are called when an object gets deleted. 
# in python __del__() method is commonly used as destructor is called when an object is deleted.

# del()
# python's built in __del__() method represents destructor in a class. In example below __del__() method would be called every time an object initiated from ClassSchedule2 class is deleted.

class ClassSchedule2:
    def __init__(self, course):
        self.course = course

    def __del__(self):
        # self parameter in __del__() method refers to current instantiated object
        print("You successfully deleted you schedule")
    
second = ClassSchedule2("AI LLM")
print(second.course)
del second

# create a ClassSchedule object
sched = ClassSchedule2('Chemistry')
print(sched.course)

# delete the ClassSchedule object
del sched

# Access Modifications
# in programming access modifiers are used to control or restrict access to members, aka variables and methods in a class.
# these modifiers play an important role in limiting access to secure members within class.

# public access modifier
# by default all members within class are public and there is no need to specify access modifiers for public members.
# being public means that these members can easily be accessed from outside class, in another part of any program.

class ClassSchedule3:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
    
    def display_course (self):
        print(f"Your course is {self.course} and your instructor is {self.instructor}")
    
third = ClassSchedule3("Python", "Code Academy")
third.display_course()

# protected access modifier
# protected access modifiers are denoted with prefix "_"
# prevents members from being accessed outside of class unless its a subclass.

class ClassSchedule4:
    def __init__(self, course, instructor):
        self._course = course # its protected
        self._instructor = instructor # its protected

    def display_course (self): 
        print(f"Your course is {self._course} and your instructor is {self._instructor}")
    
fourth = ClassSchedule4("Python", "Code Academy")
fourth.display_course()

# private access modifier
# private access modifiers are denoted with prefix "__"
# declared members are to be accessed within class only
# membesr with this modifier will be marked private and trying to access them from outside class will cause an error.

class ClassSchedule5:
    def __init__(self, course, instructor):
        self.__course = course # its private
        self.__instructor = instructor # its private

    def display_course (self): 
        print(f"Your course is {self.__course} and your instructor is {self.__instructor}")
    
fifth = ClassSchedule5("Python", "Code Cademy")
fifth.display_course()
# print(fifth.__course) # this will cause an error