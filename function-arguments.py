# function arguments: a recap

# in python there are 3 common types of function arguments:
# 1. positional arguments: arguments taht are called by their position in function definition
# 2. keyword arguments: arguments that are called by their name
# 3. default arguments: arguments taht given a default value in function definition

# positional arguments
def print_name(first_name, last_name):
    print(f"First name: {first_name}, Last name: {last_name}")

print_name("John", "Doe") # first_name is "John", last_name is "Doe" mapped by positional order of arguments in function definition

# keyword arguments
def print_name_kw(last_name, first_name):
    print(f"First name: {first_name}, Last name: {last_name}")

print_name_kw(first_name="John2", last_name="Doe2") # notice order does not matter in keyword arguments, they are mapped by specified name

# default arguments
def print_name_default(first_name, last_name="Smith"):
    print(f"First name: {first_name}, Last name: {last_name}")

print_name_default("John3") # last_name uses default value "Smith"
print_name_default("John4", "Doe4") # last_name is overridden to "Doe4"

# we will explore what happens when we want to make our function arguments more flexible by taking a varying number of arguments

# exercise
tables = {
  1: ['Jiho', False], # customer name, is VIP or not
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# function to assign a table to a customer, with default VIP status (default is False)
def assign_table(table_number, customer_name, vip_status=False):
    tables[table_number] = [customer_name, vip_status]

# assign_table(2, "Alice", True)
assign_table(6, "Yoni", False)

assign_table(customer_name="Alice", vip_status=True, table_number=2) # keyword arguments can be in any order

assign_table(3, "Karla") # vip_status uses default value False

assign_table(customer_name="Bob", table_number=4) # vip_status uses default value False

print(tables)



# Variable number of arguments: *args
# to start exploring variable number of arguments, we will start with *args
print("\nVariable number of arguments: *args")
print("this", "is", "a", "print", "statement") # print function can take variable number of arguments

# notice how print function does not care how many arguments we pass to it, it just prints them all, it has no expectation whether we pass 1, 2, or 10 arguments or more
# how does print function do that? it uses *args
# in python there is an additional operator called unpacking operator: *
#  this unpacking operator allows us to give our functions variable number of arguments by performing whats known as positional argument unpacking

def my_function(*args): # *args allows function to take variable number of positional arguments, args can be any valid variable name, by convention we use args
    print(args) # args is a tuple of all arguments passed to the function
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4, 5)
my_function("a", "b", "c", "d", "e", "f")

# continuing tables example
def print_order(*order_items):
    print("Order items:")
    for item in order_items:
        print(f"- {item}")

print_order("burger", "fries", "soda")
print_order("pizza", "salad")



# working with *args and regular positional arguments
print("\nworking with *args and regular positional arguments")
# lets create a function takes in a number of arguents and prints them in uppercase

def shout_strings(*args):
    for s in args:
        print(s.upper())

shout_strings("hello", "world")
shout_strings("this", "is", "a", "test")

# this unpacking operator can be used with regular positional arguments as well, as in it cab be used in combination with regular positional arguments
def truncate_sentences(length, *sentences): # length is a regular positional argument, sentences is a variable number of positional arguments
    for sentence in sentences:
        print(sentence[:length]) # truncate each sentence to the specified length,  using slicing

truncate_sentences(4, "hello", "world", "this", "is", "a", "test")
truncate_sentences(2, "python", "is", "fun")

# Utilizing iteration and other positional arguments are two common ways we can increase the utility of our functions when using the unpacking operator (*). 

# restaurant exercise with dictionary
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    print(f"Table {table_number} order:")

    for item in order_items:
        print(f"- {item}")
    
assign_table(2, "Alice", True)
assign_and_print_order(2, "Steak", "Salad", "Wine")

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items

    for item in order_items:
      print(item)
    
    assign_table(2, "Arwa", True)
    assign_and_print_order(2, "Steak", "Seabass", "Wine Bottle")
#   assign_table(2,'Arwa',True)
#   assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')


# variable number of arguments: **kwargs
print("\nVariable number of arguments: **kwargs")
# python doesnt just support variable number of positional arguments, it also supports variable number of keyword arguments using **kwargs
# **kwargs allows us to pass a variable number of keyword arguments to a function.
# in python there is an additional operator called keyword unpacking operator: **
#  this unpacking operator allows us to give our functions variable number of keyword arguments by performing whats known as keyword argument unpacking

def my_function_kwargs(**kwargs): # **kwargs allows function to take variable number of keyword arguments, kwargs can be any valid variable name, by convention we use kwargs
    print(kwargs) # kwargs is a dictionary of all keyword arguments passed to the function
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function_kwargs(a=1, b=2, c=3)
my_function_kwargs(name="John", age=30, city="New York")

def arbitary_keyword_arguments(**kwargs):
    print(type (kwargs)) # kwargs is a dictionary
    print(kwargs)
    print(len(kwargs)) # number of keyword arguments passed
    print(kwargs.get('name_')) # get value of keyword argument 'name'
    print(kwargs.get('name', 'Not Found')) # get value of keyword argument 'name', if not found return 'Not Found'
    print(kwargs.get('anything_goes'))

arbitary_keyword_arguments(name="Alice", age=25, city="Los Angeles")
arbitary_keyword_arguments(this_arg='wowzers', anything_goes=101)

# **kwargs observations
# 1. **kwargs is a dictionary
# 2. **kwargs can take any number of keyword arguments
# 3. **kwargs can be accessed like a dictionary
# 4. **kwargs can be used to pass variable number of keyword arguments to a function
# 5. **kwargs can be used in combination with regular positional arguments and *args
# 6. **kwargs name is completely arbitrary, by convention we use kwargs


# continuing tables example with **kwargs
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    },
    'is_reserved': {
      'reserved_by': 'Manager',
      'time': '7:00 PM'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)



# working with **kwargs
print("\nworking with **kwargs")

# working with **kwargs looks very similar to its *args counterpart
# since **kwargs is a dictionary, we can iterate over its key-value pairs using items() method
# we can use values() method to get a list of all values in the dictionary
# we can use keys() method to get a list of all keys in the dictionary
# we can use get() method to get the value of a specific key in the dictionary
# we can use pop() method to remove a specific key-value pair from the dictionary
# we can use update() method to update the dictionary with new key-value pairs
# we can use clear() method to clear the dictionary
def print_data(**kwargs):
    for arg in kwargs:
      print(f"{arg}: {kwargs[arg]}") # access value using key

    for key, value in kwargs.items():
      print(f"{key}: {value}", "item")

    for value in kwargs.values():
      print(value, "value")

    for key in kwargs.keys():
      print(key, "key")

print_data(name="John", age=30, city="New York")

# we can use **kwargs in combination with regular positional arguments
def print_all(positional_arg, **kwargs):
    print(f"Positional argument: {positional_arg}")
    
    print("Kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}", "items")

print_all("This is a positional argument", name="Alice", age=25, city="Los Angeles")

# if we were to switch the order of *args and **kwargs in the function definition, we would get a syntax error
# def print_all(positional_arg, **kwargs, *args): # this would raise a syntax error
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks
  # tables[table_number]['order']['food_items'] = food
  # tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')

assign_food_items(2, food='Steak, Salad', drinks='Wine')
print(tables)


# all together now: regular positional arguments, *args, and **kwargs
print("\nall together now: regular positional arguments, *args, and **kwargs")
# we can use regular positional arguments, *args, and **kwargs all together in a function definition
# the order of arguments in the function definition must be: regular positional arguments, *args, standard keyword arguments, **kwargs
# if we were to switch the order of *args and **kwargs in the function definition, we would get a syntax error
def print_animals(animal1, animal2, animal3, *args, animal4, animal5, **kwargs):
    print("Regular positional arguments:")
    print(animal1, animal2, animal3) # regular positional arguments
    
    print("Additional animals: *args")
    for animal in args: # *args
        print(animal)
    
    print("standard keyword arguments:")
    print(animal4, animal5) # standard keyword arguments

    print("Animal details: **kwargs")
    for key, value in kwargs.items(): # **kwargs
        print(f"{key}: {value}")

print_animals("Dog", "Cat", "Rabbit", "Hamster", "Parrot", animal4="Fish", animal5="Turtle", color="Brown", size="Medium") # notice how we can use all three types of arguments in a single function definition, and how we can use keyword arguments to specify the values of standard keyword arguments and **kwargs.
# print_animals("Dog", "Cat", "Rabbit", animal4="Fish", animal5="Turtle", color="Brown", size="Medium", "Hamster", "Parrot") # this would raise a syntax error because *args must come before standard keyword arguments and **kwargs

def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)
  
# single_prix_fixe_order("Baby Beets", "Salmon", "Scallops", "Mashed Potatoes", "Vanilla, Cookies and Cream") # this would raise a syntax error because sides is a standard keyword argument and must be specified using a keyword
single_prix_fixe_order("Baby Beets", "Salmon", "Scallops", sides="Mashed Potatoes", dessert1="Vanilla", dessert2="Cookies and Cream") # correct way to call the function using keyword for sides and dessert scoops as keyword arguments
single_prix_fixe_order("Baby Beets", "Salmon", "Scallops", sides="Mashed Potatoes", scoops="Vanilla, Cookies and Cream") # correct way to call the function using keyword for sides and dessert scoops as a single keyword argument



# function call unpacking and beyond
print("\nfunction call unpacking and beyond")
# Not only can we use the operators when defining parameters in python, but we can also use them in function calls
def sum(n1, n2, n3):
    return n1 + n2 + n3

print(sum(1, 2, 3)) # 6

# that works fine when we know exactly how many arguments we want to pass to the function
# but what if we have a list or tuple of numbers that we want to pass to the function?
numbers = [1, 2, 3]
# print(sum(numbers[0], numbers[1], numbers[2])) # 6
print(sum(*numbers)) # 6, using unpacking operator to unpack the list into individual arguments

# by using unpacking operator, we can pass a list or tuple of arguments to a function that expects individual arguments, as long as the number of arguments in the list or tuple matches the number of parameters in the function definition
# thus we saved ourselves from having to manually index into the list or tuple to get each individual argument or writing a loop to iterate over the list or tuple to get each individual argument
# we can also use unpacking operator with dictionaries
numbers_dict = {'n1': 1, 'n2': 2, 'n3': 3}
# print(sum(numbers_dict['n1'], numbers_dict['n2'], numbers_dict['n3'])) # 6
print(sum(**numbers_dict)) # 6, using unpacking operator to unpack the dictionary into individual keyword arguments

# we can also use built in functions like map, filter, range, etc. in combination with unpacking operator to pass variable number of arguments to a function
print(sum(*map(int, ['4', '5', '6']))) # 15, using map to convert strings to integers and unpacking operator to pass them as individual arguments, sum(4, 5, 6) # 15
print(sum(*range(7, 10))) # 24, using range to generate a sequence of numbers and unpacking operator to pass them as individual arguments, sum(7, 8, 9) # 24

# possibilities of using *args and **kwargs are endless, and they can be used in many creative ways to make our functions more flexible and powerful

# unpacking parts of an iterable
print("\nunpacking parts of an iterable")
# we can use unpacking operator to unpack parts of an iterable into individual variables
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers # unpacking first two elements into individual variables and the rest into a list
print(first) # 1
print(second) # 2
print(rest) # [3, 4, 5]

a, *b, c = numbers # unpacking first element into individual variable, the rest except the last into a list, and the last into an individual variable
print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5

# merging iterables
print("\nmerging iterables")
# we can use unpacking operator to merge two or more iterables into a single iterable
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
merged_numbers = [*numbers1, *numbers2, *numbers3] # merging three lists into a single list
print(merged_numbers) # [1, 2, 3, 4,

my_tuples = (3, 6, 9)
merged_tuples = (0, *my_tuples, 12) # merging a tuple with individual elements into a single tuple
print(merged_tuples) # (0, 3, 6, 9, 12)


# combining unpacking and packing
print("\ncombining unpacking and packing")
# we can use unpacking operator to unpack an iterable into individual variables and packing operator to pack individual variables into an iterable
numbers = [1, 2, 3]
first, *rest = numbers # unpacking first element into individual variable and the rest into a list
print(first) # 1
print(rest) # [2, 3]
print([first, *rest]) # [1, 2, 3], merging individual variable and list into a single list
print((first, *rest)) # (1, 2, 3), merging individual variable and list into a single tuple
print({first, *rest}) # {1, 2, 3}, merging individual variable and list into a single set
# note: merging into a set may change the order of elements since sets are unordered collections
print({ 'first': first, **{f'rest_{i}': v for i, v in enumerate(rest)} }) # {'first': 1, 'rest_0': 2, 'rest_1': 3} 5, 6, 7, 8, 9]

num_collection = {3, 6, 9}

def power_two(*n):
    for num in n:
        print(num ** 2)

power_two(*num_collection) # 9, 36, 81 (order may vary since sets are unordered)
power_two(3, 6, 9) # 9, 36, 81
# both function calls above are equivalent, we just used unpacking operator to unpack the set into individual arguments in the first call
# power_two([3, 6, 9]) # this would raise a TypeError because we are passing a single argument which is a list, instead of three individual arguments
# power_two(*[3, 6, 9]) # this would work and is equivalent to power_two(3, 6, 9) because we are using unpacking operator to unpack the list into individual arguments

# continuing tables example
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

calculate_price_per_person(100, 15, 4) # 28.75
calculate_price_per_person(total=100, tip=15, split=4) # 28.75
calculate_price_per_person(100, tip=15, split=4) # 28.75
# calculate_price_per_person(tip=15, split=4, total=100) # this would raise a TypeError because positional argument must come before keyword arguments
table_num_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_num_total) # 128.28, using unpacking operator to unpack the list into individual arguments and passing them to the function as individual arguments instead of keyword arguments 
# calculate_price_per_person(**table_num_total) # this would raise a TypeError because keyword argument must come before positional arguments


# continue tables example
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

def un_assign_table(table_number):
    tables[table_number] = {}

un_assign_table(2)
print(tables)

# adjustments to calculate_price_per_person function so that it returns the value instead of printing it
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  return split_price