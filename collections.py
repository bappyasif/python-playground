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