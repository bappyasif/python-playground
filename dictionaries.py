# dictionaries
# most frequently used data structure in python
# in python dictionary is denoted with curly brackets {}
# dictionary is a collection of key-value pairs, which refers to a key and a value pair separated by a colon.
# values can be of any data type, including lists, tuples and dictionaries even.
# keys must be unique and immutable, and values can be mutable.
# keys must be of an immutable data type, including strings, integers, floats and tuples.

groceries = {
    "fruits": ['apple', 'banana', 'orange'],
    "vegetables": ['carrot', 'lettuce', 'onion'],
    "protein": ['chicken', 'beef', 'pork'],
    "carbs": ['bread', 'rice', 'pasta']
}

print(groceries)

# Accessing and writing values
# in contrast to other data structures such as lists and tuples, there are no built ways to use indexing and slicing values in a certain order from a dictionary.
# keys can be used to access values in a dictionary

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}

print(party_planning['Yes'])
print(party_planning['Location'])
print(party_planning['Date'])

# likewise values can be changed
party_planning['Yes'] = 100
print(party_planning['Yes'])

# similarlty a new key value pair can be added
party_planning['Guests'] = 50
print(party_planning)

# common built in functions

# len()
# returns the number of key-value pairs in a dictionary
# len takes a dictionary as an argument and returns an integer
print(len(party_planning))

# update()
# updates the dictionary with the key-value pairs from another dictionary
# update takes a dictionary as an argument and updates existing key-value pairs
# any new key-value pairs are added to the dictionary
# overwrites existing key-value pairs
party_planning.update({'Guests': 100})
print(party_planning)

shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

# keys and values
# keys() and values() methods return a list of the dictionary's keys and values, respectively
print(party_planning.keys())
print(party_planning.values())


# usecases
dictionary = {
  1: 'hello', 
  'two': True, 
  '3': [1, 2, 3], 
  'Four': {'fun': 'addition'}, 
  5.0: 5.5
}

# items()
# returns a list of the dictionary's key-value pairs through a dict_items object
print(dictionary.items())

# get()
# returns the value of a key in a dictionary
print(dictionary.get('two'))

# pop()
# removes a key-value pair from a dictionary
print(dictionary.pop(1))
print(dictionary)