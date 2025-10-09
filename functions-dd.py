# lambda function
# in python lambda function commonly referred to as anonymous function
# lambda function is a function that is defined without a name
# lambda function is a function that is defined with one line

# regular function
def add_two(inp):
    return inp + 2

# lambda function
add_two = lambda my_inp: my_inp + 2


print(add_two(2))
print(add_two(3))
print(add_two(4))

# observation:
# lambda function is stored in a variable called add_two
# lambda keyword is used to define lambda function
# rest remains same as regular function

def add_bang(sentence):
    return sentence + '!'

add_bang = lambda sentence: sentence + '!'

print(add_bang('hello'))

# lambda functions can get a bit too complicated
check_if_a_grade = lambda grade: 'Got an A' if grade >= 90 else 'Not an A'

print(check_if_a_grade(90))
print(check_if_a_grade(80))

# lambda functions are preferred way of creating small one liner functions
# reduced syntax assists readability
# and when need for function code reuse is not an objective
# when we need function complexity to be more than 1 line, we use regular functions, as doing so is more readable.

double_or_zero = lambda number: number * 2  if number % 2 == 0 else 0

print(double_or_zero(4)) # 8
print(double_or_zero(5)) # 0


# higher order functions
# higher order function is a function that takes a function as an argument or returns a function as a result

# functions as first class objects
# functions can be stored in variables
# functions can be passed as arguments to other functions
# functions can be returned from other functions

# in pithon functions are treated just like any other object, which in turn gives them flexibility and power to be used in a wide range of contexts / ways.

# first class objects can be stored in data structures such as lists and dictionaries

# assigning a function to a variable
uppercase = str.upper # now uppercase is a variable that holds a reference to the str.upper function
# we are now able to use this variable to call the function
loud = uppercase('louuud')
print(uppercase('hello'), loud)

string_manipulation_functions = [str.upper, str.lower, str.capitalize] # list of functions
print(string_manipulation_functions[0]('hello')) # HELLO
print(string_manipulation_functions[1]('HELLO')) # hello
print(string_manipulation_functions[2]('hello')) # Hello

# fact that fun ctions are first class objects in pythonand there have all the properties of any other object means that we can use them in a wide range of contexts and ways, including assigning them to variables, passing them as arguments to other functions, and returning them from other functions

