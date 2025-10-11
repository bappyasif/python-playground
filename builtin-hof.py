# built in HOF

# in python built in functions are first class objects
# this means that they can be stored in variables, passed as arguments to other functions, and returned from other functions and stored in data structures such as lists and dictionaries

# we will look at some of the built in higher order functions, such as map, filter, and reduce

# map
# map is a built in function that takes two arguments, a function and an iterable
# map returns a map object, which is an iterator that contains the results of applying the function to each element of the iterable
# map can be used to apply a function to each element of an iterable and return a new iterable with the results

# example
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers)) # [1, 4, 9, 16, 25]

# when we called map, we passed a lambda function as the first argument, which is a function that takes one argument, x, and returns x squared

def double(x):
    return x * 2

doubled_numbers = map(double, numbers)
print(list(doubled_numbers), doubled_numbers) # [2, 4, 6, 8, 10], <map object at 0x7f6e2b4b6f40>

# observation:
# we defined a function double, taht take a value x and return x * 2, this function can be used anywhere in program not just in map function
# we also had a list of numbers, and we passed that list to map function, which applied the double function to each element of the list and returned a new list with the results
# if want to see actual results of map function, we need to convert it to a list using builtin list function

# hof likes of map work specially well with lambda functions, because lambda functions are very short and can be used to apply a function to each element of an iterable in one line, and also that lambda function is not going to be used else where in program, so it is very easy to use it in map function

doubled = lambda x: x * 2
doubled_numbers = map(doubled, numbers)
print(list(doubled_numbers)) # [2, 4, 6, 8, 10]

# exercise:
grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:

# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda x: x * 25 if x < 4 else x, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list
updated_grade_list = list(grades_100scale)

# print updated_grade_list
print(updated_grade_list)


# filter
# filter is a built in function that takes two arguments, a function and an iterable
# filter returns a filter object, which is an iterator that contains the elements of the iterable for which the function returns True
# filter can be used to filter out elements of an iterable based on a condition

# example
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers)) # [2, 4]

# observation:
# we passed a lambda function as the first argument, which is a function that takes one argument, x, and returns True if x is even, False otherwise

names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(list(M_names)) # ['margarita', 'Masako', 'Maki']

# observations:
# filter takes two parameters, a function and an iterable
# for each item in list of names, we check if first letter is M or m
# returned result is then converted to a list using builtin list function
# if want to see actual results of filter function, we need to convert it to a list using builtin list function

# exercise:
books = [
    ["Burgess", 1985],
    ["Orwell", "Nineteen Eighty-four"],
    ["Murakami", "1Q85"],
    ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
    ["Murakami", 1985]
]

# Your code below: 

# assign the result of your filter function to the variable  string_titles
string_titles = filter(lambda book: type(book[1]) != str, books)

# convert your filter object to a list stored in the variable string_titles_list
string_titles_list = list(string_titles)

# print the list string_titles_list
print(string_titles_list)



# reduce
# reduce has two distinct differences from built in hof that we have covered so far, namely map and filter
# in contrast to map and filter that are always available, reduce function must be imported from functools module to use it
# rather than returning a reduce object as might be expected after leaning map and filter, reduce returns a single value.
# to get to that single value reduce cumulatively applies a passed function to each sequential pair of elements in an iterable

# example
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers) # 15

# observations:
# in reduce function, we passed a lambda function as the first argument, which is a function that takes two arguments, x and y, and returns x + y
# in reduce function, we passed a list of numbers as the second argument

# example 2:
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list) # 1944

# observations:
# in reduce function, we passed a lambda function as the first argument, which is a function that takes two arguments, x and y, and returns x * y
# in reduce function, we passed a list of numbers as the second argument
# The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, to get a product of 18.
# Next, 18 was multiplied by the following element in the list, 9, to get 162.
# Continuing on, 162 was multiplied by the next element, 12, to get 1944.
# This last, final value—1944—is what was returned by reduce().

# exercise
letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function

# store the result of your reduce function in the variable word
word = reduce(lambda x, y: x + y, letters)

# print word
print(word) # reduce

# wrapping up:
# map function applies a passed function to each element in an iterable and returns a map object
# filter function filters out elements of an iterable based on a condition and returns a filter object
# reduce function cumulatively applies a passed function and returns a single value
# these three functions streamline code on their own but they are even easier to read when tehy are used in conjunction with lambda function