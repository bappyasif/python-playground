# iterables and iterators:

# iteratoir objects: __iter__() anbd iter()

dog_foods = ["chicken", "beef", "turkey", "fish"]
for food in dog_foods:
    print(food +" has "+ str(food)+ " in it")

# under hood forst step in for loop has to do is to convert our dictionary (iterable) of dog_foods to an iterator object
# an iterator object is a special ob ject that represents a stream of data that we can operate on, to accomplish this, it uses a built-in function called iter()

dog_food_iterator = iter(dog_foods)
print(dog_food_iterator)

# to go behind scenes even further, iter(dog_foods) is actually calling a method within iterable called __iter__()
# all iterables have this __iter__() method defined, we can even use python built-in function dir() to show that our dog_foods dictionary which is an iterable has a method called __iter__() defined

print(dir(dog_foods))

# in summary __ikter__() method simply returns  iterator object that allows us to iterate over iterables like lists and dictionaries
# calling dog_food.__iter__() will retrieve same iterator object as calling iter(dog_foods), this means that buit-in function iter() and iterable's object method __iter__()can be usewd interchangeably
# while object itself might not seem super useful just yet, we'll see how to manipulate stream of data inside of it soon enough

# exercise:
sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
print(dir(sku_list))
sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)

# iterator objects: __next__() and next()

# now that we used an iterator's __iter__() method to creat an iterator object, how does our for loop know which value to retrieve on each iteration?
# iterator object has a method called __next__() which retrieves iterators's next value

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)

next_sku = sku_iterator.__next__()
print(next_sku)

# similarly to __iter__() and iter(), there is a python built-in function called next() that we can use in place of calleing __next__() method.
# calling next() simply calls iterator object's __next__() method

next_sku = next(sku_iterator)
print(next_sku) # 7046538, same value as before with __next__()

# how does iterator object know when to stop retrieving values? does it keep calling __next__() indefinitely?
# luckily __next__() method will raise an exception called StopIteration when all items have been iterated through
# if we call __next__() a total of 5 times, one more than total number of SKU's on list, we will see StopIteration exception raised on last __next__() call

sku_iterator = iter(sku_list)

for i in range(5):
    if i < 4:
        next_sku = sku_iterator.__next__()
        print(next_sku)

# to sum up, we can finally see why we needed to create iterator object in previous exercise, creating it allows us to utilize next() or __next__ to work with stream of data one piece at a time.

# exercise:
dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1)
next_dog_food2 = dog_food_iterator.__next__()
next_dog_food3 = dog_food_iterator.__next__()
print(next_dog_food2)
print(next_dog_food3)
# next(dog_food_iterator) # will raise StopIteration exception

# iterators and For loops:
# now that we understand iterators and how they work behind scenes, we have all pieces to put big picture together
# lets look back at dog_foods dictionary and 'for' loop taht performs iteration on it

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags of food in it")

# to summarize three main steps are:
# `for` loop will first retrieve an iterator object for dog_foods dictionary using iter() function
# then next() is called on each iteration of `for` loop to retrieve next value from iterator object, value is then set to food_brand variable
# on each `for` loop iteration, `print` statement is executed, until finally `for` loop executes a call to next() taht raises StopIteration exception, at that point `for` loop ends and is finished iterating over dog_foods dictionary


# custom iterators:
# we havce seen that methods __iter__() and __next__() must be implemented for an object to be an iterator object.
# implementation of these methods is known  as iterator protocol

# if we desire to create our own custom iterator class, we must implement iterator protocol, meaning we need to have a class that defines at minimum __iter__() and __next__() methods

# to look at a scenario where we might require our own custom iterator, imagine we are recieving a shipment of new fish that we can now sell in our pet store. we dont have anyt `classes` to manage our fish inventory, so we need to create a custom `class` to do so. if we wanted to track available fish inventory, our custom class initializer may look something like this:

class FishInventory:
    def __init__(self, fishList):
        self.availableFish = fishList

# by default custom classes are not iterable, we cant just go around plugging our custom classes into `for` loops and expecting any results. this represents a problem if `class` that we are working with needs ability to be iterated over

# when we create a FishInventory class object, we want to iterate over all available fishes witin `self.availableFish` attribute, if we attempt to directly iterate over our custom FishInventory class object, we will recieve an error because we dont have not yet implemented iterator protocol for this custom class

# to make FishInventory class iterable we can simply define __iter__() and __next__() methods in our custom class

# exercise: we will see if we dont implement __iter__() and __next__() methods in our custom class, we will recieve an error

fish_inventory_cls = FishInventory(["Bubbles", "Dory", "Nemo", "Moby"])
# for fish in fish_inventory_cls:
#     print(fish)


# custom - iterators-II:
# to iterate over a custom class we must implement _iiter__() and __next__() methods in our custom class,
# in most cases two methods can do following:
    # __iter__() method must always return iterator object itself, typically this is accomplished by returning `self`. it can also include some class member initialization logic in it.
    # __next__() method must either return next value avaiable or raise an StopIteration exception. it can also include any number of operations in it.
# as we want to make our FishInventory class iterable to see all available fish.
# to make it iterable we have to first define __iter__() method, we can initialize a class member within __iter__() method called index that will help us track current position in available fish list

class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList

    def __iter__(self):
        self.index = 0
        return self

# observations:
# notice that _iter_() method returns itself since this class will be an iterator object.
# __iter__() method can return other iterator objects but typically object itself is returned here by using `return self`

# then we need to define __next__() method, where we can perform operations in it, like incrementing class members or traversing `for` loop for instance

class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next(self):
        fish_status = self.available_fish[self.index] + " is available!"
        self.index += 1
        return fish_status
    
# observations:
# we return next available fish status within a string value and increment our class member index by 1 to move to next fish
# iterating over this class object will eventually error out since we fail to do any checking for our index value against our available fish list length.
# we can avoid this and cleanly stop iterator by raising StopIteration exception in our __next__() method

class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.available_fish):
            fish_status = self.available_fish[self.index] + " is available!"
            self.index += 1
            return fish_status
        else:
            raise StopIteration
        

# now that we have defined __iter__() and __next__() methods in our custom class, we can iterate over it just like we did with a list

fish_inventory_cls = FishInventory(["Bubbles", "Dory", "Nemo", "Moby"])
for fish in fish_inventory_cls:
    print(fish)


# exercise:
class CustomerCounter:
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count >= 10:
            raise StopIteration
        else:
            self.count += 1
            return self.count
        
customer_counters = CustomerCounter()
for customer in customer_counters:
    print(customer)


# python Itertools: built-in iterators
# while building our own custom iterator classes can be useful, python offers a convenient, built-in method name itertools that provides ability to create complex iterator manipulations, these operators can input either a single iterable or combinatoin of them.
# there are three categories of itertool iterators:
    # infinite: infinite iterators will repeat an infinite number of times, they will not raise a StopIteration exception and will require some stop condition to exit from loop
        # examples: count(), cycle(), repeat()
    # input-dependent: iterators are terminated by input iterable(s) sequence length, this means that smallest length iterable parameter of an input sependent iterator will terminate iterator
        # examples: chain(), compress(), filterFalse()
    # combinatoric: iterators that are combinational, where mathematical functions are performed on input iterables
        # examples: product(), permutations(), combinations()

# we can use itertools module  by importing it from python standard library