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