# polymorphism

# in computer programming, polymorphism is an ability to apply an identical operation onto different types of objects
# this can be useful when an object type may not be known at program runtime.
# polymorphism can be applied using python in multiple ways, one of which is through class inheritance which we already covered with inheritance, method overloading and operator overloading

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("{} makes a noise".format(self.name))

class Cat(Animal):
    def make_noise(self):
        print("{} says meow".format(self.name))


class Robot:
    def make_noise(self):
        print("beep beep")

# observations:
# above example shows how polymorphism can be used to call a method with different implementations depending on the object type
# above example shows an Animal class its subclass Cat and a standalon class Robot, eacch has a make_noise method which is polymorphic and has different output, this is due to method overloading
# identical method names with different implementations is a form of polymorphism

an_animal = Animal("Bear")
my_pet = Cat("Malissa")
my_vacuum = Robot()

objects = [an_animal, my_pet, my_vacuum]

for obj in objects:
    obj.make_noise()

# explanations:
# created three objects, an instance of Animal, an instance of Cat and an instance of Robot
# each object has its own implementation of make_noise method
# when we call make_noise method on each object we see different outputs
# thus polymorphism is used to call a method with different implementations depending on the object type, also known as method overloading

# exercise
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")


class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an admin")


class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am a manager")


e = Employee()
a = Admin()
m = Manager()

meeting = [a, e, m]

for obj in meeting:
    obj.say_id()




# dunder methods
# dunder methods are special methods that are called when certain operations are performed on an object
# these methods are called dunder methods, because they are double under score dunder

# code below will show that when working with different object types like int, str, list etc. + operator performs different functions, this is known as operator overloading and is another form of polymorphism

# for an int and an int the + operator will perform addition and return an int
4 + 4 == 8 # True

# for a string and a string the + operator will perform concatenation and return a string
"hello " + "world" == "hello world" # True

# for a list and a list the + operator will perform concatenation and return a list
# [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]
[1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6] # True


# to implement this behavior, we must first discuss dunder methods.

# every defined class in python has access to a group of these special methods
# we explored a few of these dunder methods, sucvh as __init__() and __repr__()
# name dunder methods derived from double underscores that surrounds name of each method.

# recall __repr__() is used to return a string that can be used to recreate the object, it takes only one parameter, self and must return a string
# __init__() is used to initialize the object

class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"
    
    def __add__(self, other):
        return Animal(self.name + other.name)
    

a1 = Animal("Dog")
a2 = Animal("Cat")
a3 = a1 + a2
print(a1) # Dog
print(a2) # Cat
print(a3) # DogCat

# observations:
# above example shows how we can implement operator overloading using dunder methods
# operator overloading is when we can use an operator to perform different operations depending on the object type
# above code has an Animal class with a __add__ method which is an operator overload, this defines "+" operator behavior when used on objects of this class type, method returns a new object of this class type with names concatenated
# line of code a3 = a1 + a2 invokes __add__ method on a1 and a2 objects, name attributes of a1 and a2 objects are concatenated using parameters self, other and returned a new string object to be stored in a3

# excercise
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1
    
class Meeting:
    def __init__(self):
        self.attendees = []
    
    def add_attendee(self, employee):
        print(f"Adding employeed with id: {employee.id}")
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)
    

e1 = Employee()
e2 = Employee()
e3 = Employee()

m = Meeting()
m.add_attendee(e1)
m.add_attendee(e2)
m.add_attendee(e3)

print(len(m)) # 3   