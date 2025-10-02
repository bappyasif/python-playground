# lists
# lists are ordered collections of items that can contain different data types such as strings, integers, floats and many more.
# lists can be created with brackets [] with items separated by commas.

list = ['abc', 123, 10.8, 62, ['g', 'h', 1, 2]]
print(list)

# list indexing and slicing

# indexing
# items can be accessed with its index number
print(list[0])

# slicing
# we can slice a list to get a sub-list
print(list[0:2])



# common builtn in methods

# len()
# length of a list can be measured using 
print(len(list))

# append()
# adds an item to the end of a list
list.append(100)
print(list)

# remove()
# removes an item that is passed as an argument from a list
list.remove(100)
print(list)

# pop()
# removes the last item in a list
list.pop()
print(list)