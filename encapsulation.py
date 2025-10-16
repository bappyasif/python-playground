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