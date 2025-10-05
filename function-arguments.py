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