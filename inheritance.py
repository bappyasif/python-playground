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

# exercise
class Student:
    id_num = 1

    def __init__(self, name, prog):
        self.id = Student.id_num
        self.name = name
        self.prog = prog
        Student.id_num += 1
    
    def identify_student(self):
        print("Student bearing id: {} know as {} from {} program".format(self.id, self.name, self.prog))

s = Student("John", "Computer Science")
s.identify_student()

class Undergrad(Student):
    def __init__(self, name, prog, session):
        super().__init__(name, prog)
        self.session = session
    
    # def identify_student(self): super().identify_student() # without it we would have same result due to inheritance

    def identify_me(self):
        # super().identify_student()
        print("I am in session {}".format(self.session))


u = Undergrad("<John 2>", "Computer Science", "2020/2021")
u.identify_me()
u.identify_student()

class Postgrad(Student):
    def __init__(self, name, prog, session):
        super().__init__(name, prog)
        self.session = session
    
    # def identify_student(self): super().identify_student()
    def identify_me(self):
        print("im a postgrad student")
        print("I am in session {}".format(self.session))


p = Postgrad("<John 3>", "Computer Science", "2020/2021")
p.identify_me()
p.identify_student()

# multiple inheritance: part - 1
# a subclass can inherit from multiple superclasses
# one form of multiple inheritance is when there are multiple levels of inheritance (i.e. A => B => C)
# which means C is a subclass of B which is a subclass of A, so instance of C will have access to all attributes and methods of A, B and C
class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))

class Cat(Animal):
  pass

class Angry_Cat(Cat):
  pass

my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!

# observations:
# above we have three classes, Animal, Cat and Angry_Cat
# Angry_Cat is a subclass of Cat which is a subclass of Animal
# when creating instance of Angry_Cat we can access all attributes and methods of Animal, Cat and Angry_Cat

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
        print("I am an admin")

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am a manager")


e = Manager()
e.say_id()

# multiple inheritance: part - 2
# another form of multiple inheritance is when there are multiple superclasses for a subclass (i.e. A => (B, C))
# which means, subclass A has inherited from both B and C, so instance of A will have access to all attributes and methods of B and C

class Animal:
  def __init__(self, name):
    self.name = name
 
class Dog(Animal):
    def action(self):
        print("{} wigs tail".format(self.name))

class Wolf(Animal):
    def action(self):
        print("{} bites".format(self.name))

class Hybrid(Dog, Wolf):
    # def __init__(self, name):
    #     super().__init__(name)
    
    def action(self):
        super().action()
        # print("{} howls".format(self.name))
        Wolf.action(self)
        # Dog.action(self) # repeat of line 290
        print("{} howls".format(self.name))

h = Hybrid("Wolfy")
h.action() # Wolfy wigs tail \n Wolfy howls

# observations:
# above we have three classes, Animal, Dog and Wolf
# Hybrid is a subclass of Dog and Wolf
# when creating instance of Hybrid we can access all attributes and methods of Dog and Wolf
# whereas both Dog and Wolf class cant access attribites and methods of each other

# this form of multiple inheritance can be used by adding functionality from a class that does not fit in with current design scheme of current classes

# care must be taken when creating an inheritance structure like this, specially wghen using super() method. in above example super().action() inside hybrid class invokes .action() method of Dog class. this is due to being listed first in inheritance structure, as in listed before Wolf in Hybrid(Dog, Wolf) definition

# Wolf.action(self), calls Wolf class action method itself, here self is passed as arguments to Wolf.action(self) so that it recieves Hybrid class instance to output correct name

# exercise
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

class User:
    def __init__(self, username, role="customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"Username: {self.username}")
        print("Role: {}".format(self.role))


class Admin(Employee, User):
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "admin")

    def say_id(self):
        super().say_id()
        print("I am an admin")

e = Admin()
e.say_id()
e.say_user_info()

# observations:
# above we have three classes, Employee, User and Admin
# Admin is a subclass of Employee and User
# when creating instance of Admin we can access all attributes and methods of Employee and User

# exercise
class Object:
    roll = 1

    def __init__(self):
        self.id = Object.roll
        Object.roll += 1

    def say_id(self):
        print(f"Object number: {self.id}")

class Circle():
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * self.rad ** 2

class DrawCircle(Object, Circle):
    def __init__(self, rad):
        Object.__init__(self)
        Circle.__init__(self, rad)


dc = DrawCircle(10)
dc.say_id()
print(dc.area()) # 314.0

# observations:
# above we have three classes, Object, Circle and DrawCircle
# DrawCircle is a subclass of Object and Circle
# when creating instance of DrawCircle we can access all attributes and methods of Object and Circle
