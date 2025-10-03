# sets

# sets are built-in data structures in python
# set is an immutable, unordered collection of unique elements that can consist of integers, floats, strings and tuples.
# sets however can not hold mutable elements such as lists, sets or dictionaries.
# set is create with curly brackets {} and items in it separated by commas.

set1 = {'jemmy', 26, 'parker', 30}
print(set1) # prints {'jemmy', 30, 26, 'parker'}

# builtin set() method can be used to create a set
# note that it will drop any duplicate values from list, as sets can only contain unique values
set2 = set(('jemmy', 26, 'parker', 30))
print(set2) # prints {'jemmy', 30, 26, 'parker'

set3 = ['jemmy', 26, 'parker', 30]
print(set3) # prints ['jemmy', 26, 'parker', 30
print(set(set3))

# accessing and writing values
# sets dont have indexes or keys, we can use "in" keyword to check if an element is in a set
print('jemmy' in set1) # prints True
print('jemmy' not in set1) # prints False

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
print('Chau' in students) # returns True
print('Chau' not in students) # returns False



# common built-in methods

# add()
# because sets are immutable, existing elements within sets can not be modified.
# however new elements can be added using built-in add() method
# add method takes an element as an argument and adds it to the set
# if an element already exists in the set, it will not be added
students.add('A B')
print('A B' in students) # prints True

# update
# builtin update() method takes in any iterable object such as a list, tuples, sets, or dictionaries and adds its elements to the set
# any duplicated elements will not be added

new_students = {'Chau', 'Dmitry', 'Jane', 'Carlos', 'Amy', 'Bridgette'}
 
students.update(new_students)
 
print(students) # prints {'Jane', 'Amy', 'Bridgette', 'Dmitry', 'Chau', 'Carlos'}

# union
# union method takes an iterable object and joins new object with existing object
# the union() method returns a new set containing all items from both sets
print(students.union(new_students))

# intersection
# intersection method takes an iterable object and returns a new set with the common items from both sets
print(students.intersection(new_students), "intersection")


# remove
# remove method takes an element as an argument and removes it from the set
# if the element does not exist in the set, it will raise an error
print(students.remove('Jane'))
print(students)

# discard
# discard method takes an element as an argument and removes it from the set
# if the element does not exist in the set, it will not raise an error
print(students.discard('Jane'))
print(students)

# for loops
# as sets are iterable objects, we can use for loops to iterate over them
for student in students:
    print(student)