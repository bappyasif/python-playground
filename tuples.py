# tuples

# tuples are builtin data structure in python
# just like lists tuples can hold a sequence of items and have a few key advantages.
    # tuples are more memory effecient than lists
    # tuples have a slightly faster speed than lists
# this is mostly because tuples are immutable, meaning we cannot modify a tuple after being created, and do not require an extra memory block like lists. and reasons why its great to work with if you are working with a dataset that wont be changing in your code.

# tuples are defined with parenthesis with comma separated values.
# just like lists tuples can hold objects of different data types.

my_tuple = ('a', [1, 2], 3)
print(my_tuple)



# tuples indexing and slicing

# indexing
# items can be accessed with its index number
print(my_tuple[0])

# slicing
# we can slice a tuple to get a sub-tuple
print(my_tuple[0:2])



# common builtn in methods

# len()
# length of a tuple can be measured using len method with tuple as argument
print(len(my_tuple))

# max()
# maximum value of a tuple can be measured using max method with tuple as argument
# Note that this function requires all of the values to be of the same data type.
an_tuple = (1, 2, 3, 4, 5)
print(max(an_tuple))
# print(max(my_tuple)) # TypeError: max() arg is a sequence of different types

# min()
# minimum value of a tuple can be measured using min method with tuple as argument
# Note that this function requires all of the values to be of the same data type.
an_tuple = (1, 2, 3, 4, 5)
print(max(an_tuple))
# print(min(my_tuple)) # TypeError: min() arg is a sequence of different types

# sum()
# sum of a tuple can be measured using sum method with tuple as argument
# Note that this function requires all of the values to be of the same data type.
an_tuple = (1, 2, 3, 4, 5)
print(sum(an_tuple))
# print(sum(my_tuple)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# index()
# index of an item in a tuple can be measured using index method with item and tuple as arguments
print(my_tuple.index(3))

# count()
# count of an item in a tuple can be measured using count method with item and tuple as arguments
print(my_tuple.count(3))


# examples

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple)) 

print(my_tuple.index('abc'))
print(my_tuple.index(789)) 