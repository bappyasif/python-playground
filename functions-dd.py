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


# functions as arguments:
# functions can be passed as arguments to other functions
# this is called higher order function
def total_bill(func, value):
    total = func(value)
    return total

# observation:
# total_bill is a function that takes two arguments, func and value
# func is a function that is passed as an argument to total_bill
# value is a variable that is passed as an argument to total_bill
# total_bill returns the result of calling func with value as an argument

def add_tax(total):
    tax = total * .06
    new_total = total + tax
    print(new_total)
    return new_total

total_bill(add_tax, 100) # 106.0
total_bill(add_tax, 200) # 212.0

# observations:
# here total_bill is classified as HOF, because it takes in an argument which is an function called add_tax
# this might have been done via simply calling add_tax, but here it is being passed as an argument to total_bill, what if we want to pass another function as an argument to total_bill? maybe we want to pass a different function depending on the situation?
# we can do this by passing a function as an argument to another function

def add_tip(total):
    tip = total * .2
    new_total = total + tip
    print(new_total)
    return new_total

total_bill(add_tip, 100) # 120.0
total_bill(add_tip, 200) # 240.0

# observations:
# we can see that the total_bill function is still passing in a function as an argument, but this time, it is passing in a different function called add_tip
# true power of higher order functions lies in the ability to pass in functions as arguments to other functions, which allows us to create flexible and reusable code
# when we want to keep a consistent manipulation no matter what function is passed in.
# lets see this if we modify our total_bill so that it adds formatting to total amount owed in a consistent and friendly way, regardless of which function is passed in.

def total_bill(func, value):
    total = func(value)
    # formatted_total = '${:.2f}'.format(total)
    formatted_total = "The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)"
    print(formatted_total)
    return formatted_total

total_bill(add_tax, 100) # The total amount owed is $106.00. Thank you! :)
total_bill(add_tip, 100) # The total amount owed is $120.00. Thank you! :

# observation:
# now, no matter what function do we pass in as argument, and behavior we want this fucntion to accomplish, we can consistently format total amount owed in a consistent and friendly way
# whiel we are only adding small manipulation at this point, we can really do any consistent manipulation that increases our code reusability and make ourt code more modular
# this isnt only situation where higher order functions shine, they are also fantastic for situations involving iteration!


# function as arguments: iteration
# say, we have a list of of bills instead of just one and we want to add tax or tip to each bill depending on type of sale it is
# one way to accomplish this could be to write out separate loops: one for each sales that needs to be added tax and one for each sales that needs to be added tips
# to get a sense of it lets write out loop for adding tax first:
bills = [100, 200, 300]

new_bills = []

for bill in range(len(bills)):
    # total = total_bill(add_tax, bills[bill])
    total = add_tax(bills[bill])
    new_bills.append(total)
    new_bills.append(f"Total amount owed: {'{:.2f}'.format(total)}. Thank you!")
    # new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(new_bills) # ['Total amount owed: 106.00. Thank you!', 'Total amount owed: 212.00. Thank you!', 'Total amount owed: 318.00. Thank you!']

# now we could write another loop for adding tip but that would be repititive and not DRY
# a much more powerful solution would be to use a higher order function, which will allow us to use add_tax and add_tip functions as arguments

def total_bills(func, list):
    new_bills = []
    for bill in range(len(list)):
        total = func(list[bill])
        # new_bills.append(total)
        new_bills.append(f"Total amount owed: {'{:.2f}'.format(total)}. Thank you!")
    
    return new_bills

print(total_bills(add_tax, bills)) # ['Total amount owed: 106.00. Thank you!', 'Total amount owed: 212.00. Thank you!', 'Total amount owed: 318.00. Thank you!']
print(total_bills(add_tip, bills)) # ['Total amount owed: 120.00. Thank you!', 'Total amount owed: 240.00. Thank you!', 'Total amount owed: 360.00. Thank you!']

# observations:
# we can see that now we can use add_tax and add_tip functions as arguments to total_bills function
# and we can use the same function to add tax or tip to a list of bills
# being able to pass function as an argument to another function is a powerful feature of higher order functions and can be very handy when we need to perform the same operation on a list of values
# in fact its so handy that there's a built n function called map, which is a higher order function that allows us to perform the same operation on a list of values


# function as return value
# functions can also be returned from other functions
# this is another powerful feature of higher order functions
def make_box_volume_function(height):
    # define and returns a function that takes two numeric arguments, length and width and returns volume of a box based on given input
    def volume(length, width):
        return length * width * height
    return volume

box_volume = make_box_volume_function(10) # returns a function that takes two numeric arguments, length and width and returns volume of a box based on given input
print(box_volume(2, 3)) # 60

# observations:
# we can see that make_box_volume_function function returns a function that takes two numeric arguments, length and width and returns volume of a box based on given input
# and we can use this function to calculate volume of a box
# as we can see HOF with functions as return values are just as reuseable as higher order functions with functions as arguments and therefore also reduce repitition

def calculate_bonus(tax):
    def bonus (total):
        t = total + tax
        print(t, total, tax)
        return t * 0.1 + total
    return bonus

bonuses = calculate_bonus(10)
print(bonuses(100)) # 111.0

# to summarize:
# HOF are possible because functions are first class objects, meaning that they can be stored in variables, passed as arguments to other functions, and returned from other functions and stored in data structures such as lists and dictionaries
# HOF are functions that operate on other functions by taking another function as an argument, returning an function as a result, or both
# HOF can reduce code repitition, making code easier to read and less prone to mistakes