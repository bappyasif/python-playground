# python containers:
# in python there are many ways to store and organize data. such as adding elements to a list, writing a key value pair to a dictionary, or even accessing data in a tuple.

# any object which stores data is called a container. we are familiar with python's builtin containers such as list, tuple, set, and dictionary. but there are others as well. each of those specializes in a specific job and can be imported into codebase as needed.

# lists: lists are ordered group of elements, where elements can be added, removed, accessed and modified.
products = ['t-shirt', 'shirt', 'pants', 'dress']
products.append('jacket')
print(products)
products.sort()
print(products)
products.remove('dress')
print(products)

# tuples: tuples are immutable objects which group multiple elements together, they are similar to lists except that they can not be modified. once created
searched_terms = ('clothes', 'store', 'app', 'clothes', 'store', 'phone', 'purchase')
print(searched_terms[2])
print(searched_terms.count('store'))

# dictionaries: dictionaries are unordered group of key/value pairs
orders = {'order_101': {'type': 'shirt', 'size': 'medium', 'color': 'blue', 'price': 12.99}, 'order_102': {'type': 'pants', 'size': 'large', 'color': 'black', 'price': 19.99}}

order_102 = orders['order_102']
order_102_price = order_102['price']
print(order_102_price)
order_102['color'] = 'red'
print(order_102)
print(len(orders))

# sets: sets afre unordered groups of elements that cannot contain duplicates, elements cannot be modified once added to set.
old_prods_set = {'t-shirt', 'shirt', 'pants', 'dress'}
new_prods_set = {'t-shirt', 'shirt', 'pants', 'jacket'}
updated_prods_set = old_prods_set | new_prods_set # union
print(updated_prods_set)
removed_prods_set = old_prods_set - new_prods_set # difference
print(removed_prods_set)
common_prods_set = old_prods_set & new_prods_set # intersection
print(common_prods_set)

# exercise:
company_name = 'BingDing'

company_location = (45.678, 12.345) # example of a tuple

company_products = ['t-shirt', 'shirt', 'pants', 'dress'] # example of a list

company_data = {'name': company_name, 'location': company_location, 'products': company_products} # example of a dictionary

print(company_data)


# collections module:
# now that we have a refresher on some of built in containers in python lets dive into `collections` module.

# classes from `collections` module are very similar to built in containers we've been already using but they contain new methods and utilities. each of these specialized containers focuses on a certain improvement to its builtin counterpart such as optimizing performance, better organization fewer steps for performing tasks and more

# in order to use classes from `collections` module we need to import them from the `collections` module. this is different than previous examples of containers we have been using which did not require us to import them.

# here are some ways importing will look like:
from collections import Counter, deque, defaultdict, namedtuple # import a single or multiple classes from `collections` module

from collections import * # import all classes from `collections` module

import collections # another way toimport all classes from `collections` module

# for a more specific example, here is what importing `ordereddict` from `collections` module will look like:
from collections import OrderedDict

orders = OrderedDict({'order_101': {'type': 'shirt', 'size': 'medium', 'color': 'blue', 'price': 12.99}, 'order_102': {'type': 'pants', 'size': 'large', 'color': 'black', 'price': 19.99}})

print(orders, 'intially')
orders.move_to_end('order_102')
print(orders, 'after moving order_102 to end')
orders.popitem()
print(orders, 'after removing last item')


# Deque:
# in python lists are one of most commonly used containers we use to work with data, unfortunately there are certain situations where they perform badly
# lets imagine a situation where we are processing a large document containing bug reports for an application. in order to prioritize most important bugs we want any higher priority bugs to be at front of list(kind of like a priorit list), and as we  fix those bugs we remove them from top of list
# progrma below is an example of what our implementation might look like using lists
bug_data = []

get_all_bug_reports = lambda: bug_data

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        bug_data.insert(0, bug)
    else:
        bug_data.append(bug)

# next_bugs_to_fix = bug_data.pop(0) # This will remove the first element from the list and return it

# observations:
# problem with this implementation is that lists are not optimized for appending and popping large amounts of data, although they are great at accessing data at any index which you might need
# to solvce this problem we can use `deque` containers, these are very similar to lists but they are optimized for appending and popping to front and back rather than having optimized accessing. because of this they are great for working with data where you dont need to access elements in middle very often or at all
# lets observe our same program but implemented with a `deque` container

from collections import deque

bug_data = deque()

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # with a deque, we can append to front directly
        bug_data.appendleft(bug)
    else:
        bug_data.append(bug)

# with a deque we can pop directly from front
# next_bugs_to_fix = bug_data.popleft()

# exercise:
import csv

supplies_data = ("item", "num_pallets", "num_boxes", "pallet_weight", "box_weight")

def process_csv_supplies():
    data = []
    with open('supplies_data.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            data.append(row)
    return data

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

supplies_deque = deque()

for row in csv_data:
    if(row[2] == 'important'):
        supplies_deque.appendleft(row)
    else:
        supplies_deque.append(row)

ordered_important_supplies = deque()
for row in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()
for row in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())


# named tuple:
# tuples are another common built-in container, are very useful for grouping data together data that does not need to be modified in future.
# tuples do however run into an issue when they host various data and even nested data
actor_data_tuple = ('Leonerdo Dicaprio', 1974, 'Titanic', 1997)
# in this example we are storing details about an actor that is unlikely to change(we can assume for now actor's name will not change)
# while tuple does a great job of creating a container that can keep ordered immutable data, it can become quite confusing to represent properties using numerical indices, for example actor_data_tuple[0] returns 'Leonerdo Dicaprio' instead of the actor's name, actor_data_tuple[1] returns 1974 instead of the actor's birth year, etc

# unless we explicitly define variable name that describes what indices represents, its very hard to tell what data we are talking about.
# we would also need to make separate variables for each property! thanks to `collections` module we have a solution to this problem

# `namedtuple` collection allows us to habe an immutable tuple object but every element becomes self documented.

from collections import namedtuple

# general structure: namedtuple(typename, fieldnames, *, rename=False, defaults=None, module=None)
ActorData = namedtuple('ActorData', ['name', 'birth_year', 'movie', 'release_year'])

# in this example we are defining an instance of namedtuple collection with a type name called 'ActorData' and a sequence of strings that represent the labels of each element in tuple that we want to store

# we are saying we want our `namedtuple` to be called `ActorData` and for it to have `name`, `birth_year`, `movie`, and `release_year` properties, its like creating a lebl system for type of data inside of our tuple

actor_data_tuple = ActorData('Leonerdo Dicaprio', 1974, 'Titanic', 1997)
print(ActorData._fields) # this will print the labels of each property inside of our tuple
print(actor_data_tuple.name, actor_data_tuple.birth_year, actor_data_tuple.movie, actor_data_tuple.release_year)

# some things to note about namedtuple:
    # you may have noticed we use a CapWords convention when defining our   `namedtuple` collection, this is because it actually returns a subclass and thus falls under conventions we use for `classes`
    # `field_names` argument can alternatively be a single string with each fieldname separated by whitespace and/or commas, for example `x y` or `x,y`
    # at first glance `namedtuples` might seem like it is trying to replicate a dictionary, while idea of labeling properties is same in both structures, `namedtuples` have some key advantages over a regular dictionary:
        # they are immutable and maintain their order while a dictionary doesnt
        # they are more lightweight than a regular dictionary, which is takes no more memory than a regular tuple

# there are other useful methods that a `namedtuple` uses such as converting from a `namedtuple` to a dictionary replacing elements and field names and even sewtting default values for attributes

# exercise:
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)

coat_cost = new_coat.price

updated_clothes_data = list()

for item in clothes:
    new_item = ClothingItem(item[0], item[1], item[2], item[3])
    updated_clothes_data.append(new_item)

print(updated_clothes_data)

# defaultdict
# dicrtionaries are another popular type of collection we use in our programs. although they are great for a lot of situations, applications that rely heavily on them always run into a common issue, this isuue deals with how to handle missing keys
# when we try to access a key-value pair in a dictionary but key doesnt exist, a dictionary will normally throw a KeyError
prices = {'t-shirt': 9.99, 'pants': 14.99, 'jacket': 19.99}
# print(prices['shoes']) # KeyError: 'shoes'

# dealing with frequent KeyError exceptions can be quite cumbersome and in certain cases it might be better to avoid throwing an error. one way pyhton offers to deal with this issue is by having a default missing value in dictionary and this is exactly what `defaultdict` does

from collections import defaultdict

validate_prices = defaultdict(lambda: 'No price assigned')

print(validate_prices['shoes']) # No price assigned
validate_prices['pants'] = 14.99
print(validate_prices['pants']) # 14.99

# notice following:
    # we set default value for missing keys to 'No price assigned' using a lambda function
    # anytime we try to access a key that doesnt exist it automatically updates our `defaultdict` object by creating new key-value pair using missing key and default value

# exercise:
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda: 'TODO: Add to website')

validated_locations.update(site_locations)

for product in updated_products:
    site_locations[product] = validated_locations[product]

print(site_locations)

# orderdict
# when keeping track of many different dictionaries with built in python containers we could try storing dictionaries in a list or even a dictionary of dictionaries. this may work in some cases but there are a few problems which might come up
# when storing dictionaries in a list order is preserved but we have to access elements by their index before we can access dictionary

first_order = {'order_2201': {'type': 'Shoes', 'size': 10, 'price': 19.99}}
second_order = {'order_2202': {'type': 'pants', 'size': 'medium', 'price': 19.99}}
thisr_order = {'order2203': {'type': 't-shirt', 'size': 'small', 'price': 9.99}}

list_of_dicts = [first_order, second_order, thisr_order]

print(list_of_dicts[0]['order_2201']['type']) # Shoes
print(list_of_dicts[1]['order_2202']['price']) # 19.99

# inorder to get price of a specif order we must know index of it before we can access dictionary data stored inside of it

# on other hand depending on python version `dict` container can preserve order but it is difficult to move elements around
dict_of_dicts = {}
dict_of_dicts.update(first_order)
dict_of_dicts.update(second_order)
dict_of_dicts.update(thisr_order)

print(dict_of_dicts['order_2201']['type']) # Shoes
print(dict_of_dicts['order_2202']['price']) # 19.99

# note `dict` class is unordered in earlier versions of python so implementing it this way must have version 3.6 or higher, to solve this issue we can make use of `OrderedDict` class from `collections` module

# `OrderedDict` container allows us to access values using keys but it also preserves order of elements inside of it

from collections import OrderedDict

orders = OrderedDict()

orders.update(first_order)
orders.update(second_order)
orders.update(thisr_order)
orders.update({'order_2204': {'type': 'dress', 'size': 'medium', 'price': 19.99}})

find_order = orders['order_2204'] # data can be accessed using keys like in a normal dictionary

print(find_order)

# order can be retrieved by converting it to a list then accessing by index
orders_list = list(orders.items())
third_order = orders_list[2]

print(third_order)

# when using an `OrderedDict` we are able to use its methods for moving data around, we can move an element to back or front and pop data from back or front of `OrderedDict`

# move an item to end of OrderedDict
orders.move_to_end('order_2201')
print(orders)

# pop last item
last_order = orders.popitem(last=True)
print(last_order)
print(orders)

# note these two methods also accept boolean arguments which determine if element is moved / popped from front or back of `OrderedDict`

# exercise:
# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
orders = OrderedDict(order_data)

to_move = list()
to_remove = list()

for key, value in orders.items():
    if value == 'returned':
        to_move.append(key)
    elif value == 'canceled':
        to_remove.append(key)

for order in to_remove:
    orders.pop(order)

for order in to_move:
    orders.move_to_end(order)

print(orders)

# chainmap
# there is another way to store dictionaries or other mappings in pyhton, we have looked at `defaultdict` and `ordereddict` so far and they handle a lot of situations so what else could we possibly need?
# `chainmap` container allows us to store many mappings in an ordered group but lookups(accessing values with key) are repeated for every mappings inside of chainmap until something is found or end is reached.
# if we try to modify data in any way then only first mapping in `chainmap` will recieve changes when accessing data one way to think of `chainmap` will recieve changes.
# when accessing data one way to think of `chainmap` is that it treats all of stored dictionaries as one large dictionary, where if there are repeated keys then first found result is returned

from collections import ChainMap

customer_info = {'name': 'john doe', 'age': 22, 'address': '123 main st', 'phone_number': '123-456-7890'}

shirt_dimensions = {'shoulder': 20, 'chest': 40, 'torso_length': 29}

pants_dimensions = {'waist': 31, 'leg_length': 40, 'hip': 22, 'thigh': 24, 'bottom': 18}

# next we initialize a `chainmap` with mappings which we want to use, in this case mappings are dimensions of dictionaries
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)

# now we can access values from any of these stored mappings using keys
customer_leg_length = customer_data['leg_length']

print(customer_leg_length) # 40

# we can directly modify data only in first dictionary inside of `chainmap`
customer_info['name'] = 'jane doe'

print(customer_data['name'])

customer_info['address'] = '456 main st'

print(customer_data['address'])

# in order to modify data from dictionaries which are deeper in `chainMap` we will need to iterate through dictionaries which are stored inside of it

# as we can see in this example above we create a new `ChainMap` using three different dictionaries, this allows us to access any of `key:value` pairs stored inside

# another interesting concept that `chainMap` uses is concept of a parent mappings, if we use `.parents` property all mappings except first one will be returned. this is because those mappings are considered to be parent mappings of first one. you can add a new child mapping to front of list mappings using `.new_child()` method

# exercise:
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
profit_map = ChainMap(*year_profit_data)

# def get_profits():
#     last_year_standard_profit = 0
#     last_year_holiday_profit = 0
#     for key, values in profit_map.items():
#         # print(key, values, 'iter')
#         if 'holiday' in key:
#             last_year_holiday_profit += values
#         else:
#             last_year_standard_profit += values

#     print(last_year_standard_profit, last_year_holiday_profit)
#     return last_year_standard_profit, last_year_holiday_profit

# def get_profits(year_profit_data):
#     last_year_standard_profit = 0
#     last_year_holiday_profit = 0
#     for item in year_profit_data:
#         # print(item, 'iter')
#         for key, values in item.items():
#             # print(key, values, 'iter')
#             if 'holiday' in key:
#                 last_year_holiday_profit += values
#             else:
#                 last_year_standard_profit += values

#     print(last_year_standard_profit, last_year_holiday_profit)
#     return last_year_standard_profit, last_year_holiday_profit

# get_profits(year_profit_data)

# When creating this function, you can loop through each of the keys in the ChainMap since it is treated like one big dictionary. If 'holiday' is in the key, then add the value to the total count for the holiday profit, otherwise add the value to the standard profit. remember to return both values.

def get_profits(input_map):
    total_standard_profit = 0
    total_holiday_profit = 0
    for key in input_map.keys():
        # print(key, values, 'iter')
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    print(total_standard_profit, total_holiday_profit)
    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

current_year_standard_profit, current_year_holiday_profit = get_profits(ChainMap(profit_map, *new_months_data))

# profit_map was not updated correctly with the new data from new_months_data. Expected 15 dictionaries to be stored, but got 12

# we can add new data to `ChainMap` using `.new_child` method

# exercise:
# Write your code below!
# current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map.new_child(new_months_data)) # getting unhashable type: dict error

# current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map.new_child(ChainMap(*new_months_data))) #profit_map was not updated correctly with the new data from new_months_data. Expected 15 dictionaries to be stored, but got 12

# current_year_standard_profit, current_year_holiday_profit = get_profits(ChainMap(profit_map, *new_months_data)) # profit_map was not updated correctly with the new data from new_months_data. Expected 15 dictionaries to be stored, but got 12

for item in new_months_data:
    profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

print(current_year_standard_profit, current_year_holiday_profit)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(year_diff_standard_profit, year_diff_holiday_profit)

# Counter
# one of most common tasks we might have to do in a program is to count instances of an element in a collection. below we will examine a python list and look at one particular way we count elements and then see how `collections` module allows us to improve upon our implementation using `counter` collection

clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 'blouse']

# if we wanted to create a representation of how many of each item exists in our collection we could use a loop and a dictionary to do just that

counted_items = {}

for item in clothes_list:
    if item in counted_items:
        counted_items[item] += 1
    else:
        counted_items[item] = 1

print(counted_items)

# while this is perfectly sound solution to our counting problem we can actually accomplish this much wuicker using `Counter` container
# `counter` container instantly counts elements for any hashable object, it stores data as a dictionary where keys are elements and values are counts of occurances

from collections import Counter

counted_items = Counter(clothes_list)

print(counted_items)

# this above approach allows us to create a much more elegant solution without many lines of code. additionally `Counter` class has methods that provide further utility when working with our data, these methods include mathematical operations for subtracting one count dictionary from another finding most common elements and even generating a new list of elements based on number of occurrences

# exercise:
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
def find_amount_sold(opening, closing, item):
    opening_count = Counter(opening)
    closing_count = Counter(closing)
    opening_count.subtract(closing_count)
    # diff_count = opening_count.subtract(closing_count)
    # return diff_count[item] # typeerror 'NoneType' object is not subscriptable
    # return diff_count[item]
    return opening_count[item]

print(find_amount_sold(opening_inventory, closing_inventory, 'dress')) 

tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')

print(tshirts_sold)


# container wrappers:
# in python wrappers are modifications to functions or classes which change behavior in some way, they are called wrappers because they wrap around existing code to modify it. this is most commonly used with function wrapping but we can also wrap classes

# first we need a class to wrap around
class Customer:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    
# next we create a wrapper class which stores an object of class we are wrapping around, it also includes some additional functionality

class CustomerWrap(Customer):

    def __init__(self, name, age, address, phone_number):
        self.customer = Customer(name, age, address, phone_number)

    def display_customer_info(self):
        print(f'Name: {self.customer.name}')
        print(f'Age: '+ str(self.customer.age))
        print(f'Address: {self.customer.address}')
        print(f'Phone Number: {self.customer.phone_number}')

# finally we can create an object from wrapper class to access new functionality and wrapped class contained inside.

customer = CustomerWrap('john doe', 22, '123 main st', '123-456-7890')

customer.display_customer_info()

# wrapper class allows us to create different variations of classes with different purposes while avoiding code duplication
# since we use an instance of wrapped class inside of it, it preserves all of attributes and methods from wrapped class and keeps us from having to re-type all code

# in case of containers `collections` class has three different wrappers set up for us to modify! because of this we can refer to them as wrapper containers. advanced containers which we have already been looking at variations of standard built-in containers, so using wrapper containers allows us to create our own versions as well

# three wrapper containers we will be looking at are:

# 1. `UserDict` class which is a wrapper for `dict` class

# 2. `UserList` class which is a wrapper for `list` class

# 3. `UserString` class which is a wrapper for `str` class


# UserDict:
# in this lesson we have seen advanced containers which modify functionality of a dictionary such as `defaultdict` or `orderedDict`
# `UserDict` container wrapper lets us create our own version of a dictionary. this class contains all of functionality of a normal `dict` except that we can access dictionary data through `data` property, here's an example of creating a modified dictionary:
from collections import UserDict

# create a class which inherits from UserDict class
class DisplayDict(UserDict):
    # a new method to increase dictionary's functionality
    def display_info(self):
        print("Number of keys: "+ str(len(self.keys())))
        print("Keys: "+ str(list(self.keys())))
        print("Number of values: "+ str(len(self.values())))
        print("Values: "+ str(list(self.values())))

    # we can also overwrite a method from dictionary class
    
    def clear(self):
        print("Deleting all items from dictionary")
        super().clear()

disp_dict = DisplayDict({'name': 'john doe', 'age': 22, 'address': '123 main st'})

disp_dict.display_info()

disp_dict.clear()

disp_dict.display_info()

# as shown in this code example we can add additional methods and overwrite methods from `UserDict` class. this is same as inheriting from regular python classes

# exercise:
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code
class OrderProcessingDict(UserDict):

    def clean_orders(self):
        for order in list(self.keys()):
            if self[order]['order_status'] == 'complete':
                self.pop(order)

order_dict = OrderProcessingDict(data)
order_dict.clean_orders()
print(order_dict)


# UserDict:
# not only can we create our own version of a dictionary, `UserList` wrapper conrtainer lets us create our own `list` as well
# this class contains all of functionality of a regular `list` but it also has a property called `data` which allows us to access list contents directly.

from collections import UserList

# create a class which inherits from UserList class
class CondenseList(UserList):

    # a new method to remove duplicate items from list
    def condense(self):
        self.data = list(set(self.data))
        print(self.data)

    # we can also overwrite a method from list class
    def clear(self):
        print("Deleting all items from list")
        super().clear()

condense_list = CondenseList(['t-shirt', 'jeans', 'jeans', 't-shirt', 'shoes'])
print(condense_list)

condense_list.condense()

condense_list.clear()

print(condense_list)

# exercise:
data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):

    def append(self, value):
        # append new value
        self.data.append(value)
        # then sort list
        self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)