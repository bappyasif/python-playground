# OOP pillar: inheritance
# allows a class to have all data and functionalities of another class
# which allows us to share code between multiple classes

class Dog:
    def bark(self):
        print("woof")
    
class Cat():
    def meow(self):
        print("meow")

# observations:
# these two classes define distinct animals with tehir own methods of communication
# now what if we wanted to give them both ability to eat method?
# we could write it in both classes but that would be a lot of code duplication, and also into other animal classes that we would create, instead we can use inhertance

class Animal:
    def eat(self):
        print("nom nom nom")
    
class Dog(Animal):
    def bark(self):
        print("woof")
    
class Cat(Animal):
    def meow(self):
        print("meow")

dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()

# observations:
# we can now use the eat method from animal class in both dog and cat classes
# we can also use the bark and meow methods from their respective classes
# not only can we re use methods from parents class but also able to create a relationship(parent/child) between entities

# exercise
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

class Admin(Employee):
    pass

e1 = Employee()
e2 = Employee()
e3 = Admin() # though it has no implementation except inhertance, it still able to access parent's class method and data

e1.say_id()
e2.say_id()
e3.say_id()


# overriding methods
# when implementing inhertance, a child class may want to change behavior of a method from its parent class, thus enter method overriding
# an overriding method in a subclass is one that has same difinition as its parent class but with different implementation

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("{} makes a noise".format(self.name))

pet = Animal("Fido")
pet.make_noise() # Fido makes a noise

# observations:
# animal class above has one attribute name and a method make_noise
# now if we want we can create a subclass of animal for another class with a different implementation of make_noise in them

class Cat(Animal):
    def make_noise(self):
        print("{} says meow".format(self.name))

pet2 = Cat("Fido")
pet2.make_noise() # Fido says meow

# observations:
# as we created a more specific kind of animal class and has all attributes and methods of Animal class
# however we have re implemented make_noise speciefic to Cat class, which is now overriding its parent class implementation

# exercise:
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

class Admin(Employee):
    def say_id(self):
        print("I am an admin and my id is {}".format(self.id))


e1 = Employee()
e2 = Employee()
e3 = Admin()

e1.say_id()
e2.say_id()
e3.say_id() 

# super()
# when overriding methods we sometimes want to still access behavior of parent method.
# to do that we need a way to call method of parent class by calling super()
# super() gives us a proxy object, with that we can invoke method of an object's parent class(a.k.a. superclass)
# we call required function as a method on super()

class Animal:
    def __init__(self, name, sound = "Grrrr"):
        self.name = name
        self.sound = sound
        
    def make_noise(self):
        print("{} says {}".format(self.name, self.sound))

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

pet_cat = Cat("Rach")
pet_cat.make_noise() # Fido says Meow

# observations:
# in above example we have animal classand cat sub class. animal class has two attributes, name and sound, one method make_noise
# cat subclass has an __init__ method which means __init__ method of its superclass
# Animal will not be called when creating an instance of Cat, __init__ method of its subclass is overriding its parent class __init__ method
# to still call __init__ method of its parent class we used super().__init__ with required two attributes values, doing this still allows us to make use of Animal class constructor from subclass Cat
# super() is used in subclass to invoke a needed behavior of a subclass method

# exercise:
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
        print("I am an admin....")


e1 = Employee()
e2 = Employee()
e3 = Admin()

e1.say_id()
e2.say_id()
e3.say_id()