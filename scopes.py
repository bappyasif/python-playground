# lets examine thsi puzzling example to understand local scope
def favorite_color():
    color = "blue"
    print(color)  # this will print "blue"

# print(color)  # this will raise an error because color is not defined in the global scope
favorite_color()
# observations:
# the variable color is defined within the function favorite_color and is not accessible outside of it
# this is an example of local scope, where variables defined inside a function are not accessible outside the function

# rule of thumb, any names created in a local namespace are usually also locally scoped
# however, there are exceptions to this rule, such as the use of the global keyword to modify a global variable from within a function
# or the use of the nonlocal keyword to modify a variable in an enclosing namespace from within a nested function
# but in general, if a name is created in a local namespace, it is usually locally scoped and not accessible outside the function
# this is an important concept to understand when working with functions and nested functions in Python, as it can help prevent naming conflicts and make code easier to read and maintain

# exercise:
def painting(paints_color, picture):
   painting_statement = f'To paint {picture}, use following colors: '
   for color in paints_color:
      painting_statement += color + ' '
   print(painting_statement)

# print(painting_statement)  # This will raise an error because painting_statement is not defined in the global scope
painting(['red', 'blue', 'green'], 'landscape')


# enclosing / nonlocal scope:
# similar to how nested functions form a unique namespace, within their enclosing functions (enclosing namespace)
# there also exist special rules that apply for accessing nested values.
# these rules make up enclosing scope aka nonlocal scope.

def outer_function():
   enclosing_val = 'enclosing value'

   def nested_function():
      nested_val = 'nested value'
      print(enclosing_val)  # accessing enclosing variable
      # print(nested_val)  # accessing nested variable
  
   nested_function()

outer_function() # calling the outer function to execute the code and see the output of the nested function, which prints the enclosing variable

# observations:
# enclosing scope allows any value defined in an enclosing function to be accessed in nested functions below it.
# we can observe this scope since nested_function can access a variable defined one level above it in enclosing outer_function

def outer_function():
  enclosing_value = 'Enclosing Value'
 
  def nested_function():
    nested_value = 'Nested Value'

    def second_nested():
       print(enclosing_value)
       print(nested_value)

    second_nested() 
  
  nested_function()

outer_function()

# observations:
# we can see that second_nested function can access both enclosing_value from outer_function and nested_value from nested_function
# this is because second_nested is nested within nested_function, which is in turn nested within outer_function
# thus, second_nested can access variables from both its immediate enclosing function (nested_function) and the outer enclosing function (outer_function)

# there are two caveats to enclosing scope:
# 1. flow of scope access only flows upwards, meaning nested functions can access variables from their enclosing functions, but not the other way around. or in other words, deppest levels have access to every enclosing namespace above it and not other way around.
# 2. immutable objects such as strings, integers, and tuples can be accessed in nested functions, but can not be modified. if we try to modify an immutable object in a nested function, it will create a new local variable with the same name, instead of modifying the variable in the enclosing function. to modify an immutable object in an enclosing function, we need to use the nonlocal keyword.

def outer_function():
    enclosing_value = 'Enclosing Value'
  
    def nested_function():
        # trying to modify the enclosing variable without nonlocal keyword
        # enclosing_value = 'Modified Enclosing Value'  # this creates a new local variable instead of modifying the enclosing variable
        # enclosing_value += ' Modified Enclosing Value'  # this will raise an UnboundLocalError because we're trying to modify an enclosing variable without declaring it as nonlocal
		 # to fix this, we need to use the nonlocal keyword
       print('Inside nested_function:', enclosing_value)  # prints the local variable
       nested_value = 'Nested Value'
       nested_value += ' Modified Nested Value'  # this is fine as nested_value is a local variable
       print('Inside nested_function:', nested_value)  # prints the modified local variable
  
    nested_function()
    print('Inside outer_function:', enclosing_value)  # prints the original enclosing variable

outer_function()


# exercise:
def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!
  
  def calc_gallons():
    return square_feet / 400
  
  return calc_gallons()

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))


# modifying scope behavior: nonlocal statement 
# we saw earlier that we access names from enclosing scope with nested functions but we can not modify them
# python however provides a way to modify names in enclosing scope using the nonlocal statement

def enclosing_function():
  var = "value"

  def nested_function():
    # var = "new_value" # this creates a new local variable instead of modifying the enclosing variable
    # print(var) # prints the local variable
    nonlocal var  # this tells python that we want to use the variable from the enclosing scope
    var += "new_value"  # this modifies the variable in the enclosing scope
    print(var)  # prints the modified variable

  nested_function()

  print(var)

enclosing_function()


# exercise:
walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):

  square_feet = 0

  def calc_square_feet():
    
    for width, height in wall_measurements:
      nonlocal square_feet # this tells python that we want to use the variable from the enclosing scope, without this line, square_feet would be treated as a local variable and we would get an UnboundLocalError
      square_feet += width * height

  def calc_gallons():
    return square_feet / 400

  calc_square_feet()

  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))


# global scope:
# at the top level of a module or script, we have the global scope
# at highest level of access, we have global scope, which is the outermost scope in a Python program
# names defined in the global scope can be accessed from any other scope, including local and enclosing scopes

gravity = 9.81  # global variable

def get_force(mass):
    # gravity += 1  # this will raise an error because we're trying to modify a global variable without declaring it as global
    force = mass * gravity  # accessing global variable
    return force

print(get_force(10))  # prints 98.1

# similar to local scope and enclosing scope, we can only access global variables, but can not modify them
# to modify a global variable from within a function, we need to use the global keyword

# exercise:
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}

def print_available(color):
#   paint_gallons_available = {
#     'red': 50,
#     'blue': 72,
#     'green': 99,
#     'yellow': 33
# }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
  for color in paint_gallons_available:
    print(color)

print_available('red')
print_all_colors_available()

# modifying global scope: global statement
# we can modify global variables from within a function using the global statement
# this is useful when we want to modify a global variable without declaring it as global

global_var = 10

def some_function():
  global_var = 20 # this creates a new local variable instead of modifying the global variable
  print(global_var) # prints the local variable value which is 20

some_function()

print(global_var)  # prints 10, because we did not modify the global variable

# observations:
# in above example, we created a local variable with the same name as the global variable
# this is called variable shadowing, where the local variable shadows the global variable
# global_var value remains unchanged because we did not modify it, we only created a new local variable with the same name as the global variable within the function

global_var = 10

def some_function():
  global global_var # this tells python that we want to use the global variable
  global_var = 20

some_function()

print(global_var) # prints 20, because we modified the global variable using the global statement

# in addition, global statement can be used even if name has not been defined in global namespace
# using global statement will create a new global variable if it does not already exist

def some_function():
  global x
  x = 30

some_function()
print(x) # prints 30, because we created a new global variable x using the global statement

# in summary , global statement is used to modify global variables from within a function which is in local scope
# this associatian between local variable and global variable is called variable shadowing
# and its only valid within local scope when the global statement is used

# exercise:
def print_available(color):
  global paint_gallons_available

  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)


# LEGB rule of name resolution: scope resolution
# scope resolution is the order in which Python looks for a name when it is referenced
# LEGB stands for Local, Enclosing, Global, Built-in
# when a name is referenced, Python first looks in the local scope, then in the enclosing scope, then in the global scope, and finally in the built-in scope
# this is the order in which Python resolves names

# scope resolution is a term used to describe a search procedure for a name in various namespaces.
# a set of rules dictates order that search needs to follow

#  in python, unofficial rule often referred to inliterature but does not exist in official documentation is known as LEGB rule
# LEGB stands for Local, Enclosing, Global, Built-in
# this rule describes the order in which python looks for a name when it is referenced

# scenario 1: name is defined in global scope
age = 27 

def func(): 

  def inner_func():
    print(age)
  inner_func()

func() # calling func to execute the code and see the output of inner_func, which prints the age variable from global scope, which is 27

# observations:
# in above example, age is defined in global scope
# when inner_func is called, it looks for age in its local scope first, then in enclosing scope, then in global scope, and finally in built-in scope
# since age is found in global scope, it is printed

# this process of scope resolution is crucial to understand when working with functions and nested functions in Python, as it can help prevent naming conflicts and make code easier to read and maintain
# keep in mind, order that pyton searches for a name is local, enclosing, global, built-in and in that order only

# scenario 2: name is defined in two scopes
age = 27 

def func(): 
  age = 42

  def inner_func():
    print(age)
  
  inner_func() 

func() # calling func to execute the code and see the output of inner_func, which prints the age variable from local scope, which is 42

# observations:
# in above example, age is defined in both global scope and enclosing scope
# when inner_func is called, it looks for age in its local scope first, then in enclosing scope, then in global scope, and finally in built-in scope
# since age is found in enclosing scope, it is printed which is 42 and did not continue searching in global scope
# if python did not find age in enclosing scope, it would have continued searching in global scope and printed 27, and failing that, it would have searched in built-in scope, and failing that, it would have raised a NameError

# exercise:
color = 'green'

# Fix the function below:
def change_color(new_color):
  to_update = new_color # local variable, initialised to new_color

  global color
#   color = to_update # we are updating the global variable before our intended use of it to show orginal and new color

  def disp_color():
    print('The original color was: ' + color)
    # to_update = new_color

  disp_color()
  color = to_update # we are updating the global variable, and now it will be the new color

  print('The new color is: ' + color)


change_color('blue')

# review exercise:
# Outer function
def function1():
  global var1
  var1 = 1
  var2 = 2
  # Inner function
  def function2():
    nonlocal var2
    global var3
    var2 += 1
    var3 = 3
    print(globals())
    print(locals())
  
  # Call inner function
  function2()

# Call outer function
function1()