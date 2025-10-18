# @property decorator:
# is used to create a property in a class, this is known as property
# a more pytnonic way to use getter, setters and deleter functions in object orienbtred programs.

# lets recall getter, setters are useful tool for acheving encapsulation in python, in other words to prevent direct modifications of class attributes

# we can define a private attribute and the use a getter and setter expose them to access and modify it

# further getter and setter methods allow us to create complex behavior such as limiting access under certain conditions or performing validation before setting a value

class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight
    
    def setWeight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.__weight = weight

# observations:
# above we have a Box class with a private attribute __weight
# we can access this attribute using a getter method getWeight and a setter method setWeight
# notice, though we are using double underscore to indicate that this is a private attribute, we are still able to access it from outside of the class
# also, we are imposing some validation on the weight before setting it, this is known as validation

box = Box(10)
print(box.getWeight()) # 10
# print(box.__weight) # AttributeError: 'Box' object has no attribute '__weight'
box.setWeight(20)
print(box.getWeight()) # 20

# box.setWeight(-10) # ValueError: Weight cannot be negative

# additional observation:
# notice that we need to call methods instead of accessing attributes directly, this is because we are using getter and setter methods to access and modify private attributes
# what if we could have best of both worlds? meaning, there would be a way to directly interact with private attributes but still benefit from the validation and access control provided by getter and setter methods, this is where property decorator comes in

# builtin property function:
# is a built-in function in python that can be used to create properties in a class, this is known as property
# this function is used to create a property in a class, it takes in two arguments, one is the name of the property and the other is a function that returns the value of the property

# python built-in property() function accepts four optional argumenbts: fget, fset, fdel and doc
# first three of those represent getter, setter and deleter methods repectively and last one is for the docstring of the property

class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight
    
    def setWeight(self, weight):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self.__weight = weight
    
    def del_weight(self):
        del self.__weight

    weight = property(getWeight, setWeight, del_weight, "The weight of the box")

# observations:
# notice we have added one additional method del_weight to delete private attribute __weight, which will be used as deleter method for property
# though its not strictly required, we will add it show how to show full potential of property() function
# we then called property() function with arguments getWeight, setWeight and del_weight to create a property weight in Box class qalong with a docstring

box = Box(10)
print(box.weight) # 10
box.weight = 20
print(box.weight) # 20
del box.weight
# print(box.weight) # AttributeError: 'Box' object has no attribute 'weight'

box = Box(10)

print(box.weight, "direct") #this calls .getWeight()

box.weight = 5 #this called .setWeight()

print(box.getWeight(), "getter")

del box.weight #this calls .delWeight()

# box.weight = -5 #box.__weight is unchanged 

# observations:
# with those changes, our programs gains a few immediate benefits:
    # we can now use weight property as if it was public, we no longer have to call getWeight and setWeight methods directly, thus giving ou program much more simpler syntax
    # even though we no longer have to call methods directly, we stll can maintain constraints such as weights validation in our program, thus best of both worlds
# if we had a large codebase that used our methods multiple times in multiple places, a single change to method name would mess up our program since we have to change it in multiple places, we no longer have this issue with property function since we never have to call methods directly

# while this is a big advantage for our programs to be more pythonic, we can go ven further by using decoratr pattern to replace need of property() function

# @property decorator
# most pythonic way to define getter, setters and deleter methods in a class is by using @property decorator
# this decorator is a syntactic sugar for property() function and helps our code look much cleaner

class Box:
    def __init__(self, weight): 
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("Weight cannot be negative")

    @weight.deleter
    def weight(self):
        del self.__weight

box = Box(10)
print(box.weight) # 10
box.weight = 20
print(box.weight) # 20
del box.weight
# print(box.weight) # AttributeError: 'Box' object has no attribute 'weight

# observations:
# first we renamed all our methods from getWeight, setWeight and del_weight to weight()
# then we denoted a getter method with @property decorator, this marks this method to be used as a prefix for decorating setter, deleter methods
# lastly we added setter and deleter methods with @weight.setter and @weight.deleter decorators respectively
# this is equivalent as calling property() function with arguments getWeight, setWeight and del_weight respectively

# wrap-ups: we learned about
# limitations of using regular setter, getter methods
# how to use property() function to create cleaner getter, setter and deleter methods
# use of @property decorator to create cleaner getter, setter and deleter methods

# when using decorator, be mindful about these three rules:
    # all three methods must use same member name
    # first method must be getter and is identified using @property decorator
    # decorations for setter and deleter are defined by name of method @property is used with

# keep @property decorator in mind when approaching any object oriented program! it will save time and keep our programs more pythonic, cleaner and maintainable.
