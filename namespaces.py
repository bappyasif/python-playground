# built in namespaces
# global namespaces
# local namespaces / enclosing namespaces

# LEGB rule - Local, Enclosing, Global, Built-in
# namespaces are created at different times and have different lifetimes

# bilt-in namespace:
# one of four main types of namespaces in Python
# when Python starts up, it creates a built-in namespace that contains the built-in functions and exceptions that are always available in Python
# this namespace is created when the Python interpreter starts up and is destroyed when the interpreter shuts down as in when you exit the Python shell or when a Python script finishes executing
# the built-in namespace is global and can be accessed from anywhere in the code, including within functions and classes
# examples of built-in functions include print(), len(), range(), and type()
# examples of built-in exceptions include ValueError, TypeError, and IndexError
# since python provides this namespace, you don't need to import any modules or libraries to use these functions or exceptions in our code
# there are even constructs like True, False, and None that are part of the built-in namespace
# in total there are over 150 built-in functions, exceptions, types, and special attributes in Python
print(dir(__builtins__))

# global namespace:
# one of four main types of namespaces in Python
# the global namespace is created when a module is imported or when a script is executed
# global namespace exists one level below built-in namespace
# generally it includes all non nested names in a module or script we are choosing to run python interpreter on
# the global namespace is created when the module is imported or when the script is executed, as in when we run our main program and is destroyed when the module is unloaded or when the script finishes executing
import random

fName = "John"
lName = "Doe"

def print_variables():
    random_number = random.randint(1, 10)
    print(random_number)
    print(fName)
    print(lName)
    print(random.randint(1, 10))

print_variables()

# observations:
# our script consists of a few variables, a function and an import statement
# to see what is in the global namespace, we can use the globals() function which returns a dictionary representing the current global symbol table, and we can call it at any point in our code to see what is in the global namespace at that point
print(globals())
# however we can see form output that random_number is not in the global namespace as it is a local variable which is nested inside the function print_variables
# anytime we use import statement toi bring in a new module into our program, instead of adding each individual function or class from that module into our global namespace, python adds the module name itself into the global namespace
# which means there might be potentially multiple global namespaces in a single program if we import multiple modules, this will be masked away from us as we will always refer to the module name when we want to access any function or class from that module
# for example, if we had imported another module like math, then we would have two global namespaces, one for random and one for math
# we can see this by printing the globals()
import math
print(globals())
# we can see that both random and math are in the global namespace
# we can also see that fName and lName are in the global namespace
# we can also see that print_variables is in the global namespace as it is a function defined at the top level of our script
# we can also see that __name__ is in the global namespace, which is a special variable that is automatically created by Python and is used to determine if the script is being run as the main program or if it is being imported as a module

print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 

print(globals())

# Write Checkpoint 2 here: 

global_variable = 'global'


# Write Checkpoint 3 here: 

def print_global():
  global_variable='nested global'
  nested_variable='nested value'


print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here: 


print(globals())

# takeaways:
# global namespace only consists of names that are defined at the top level of a module or script and does not include names that are defined inside functions or classes
# depending on where we call the globals() function, the contents of the global namespace may vary


# local namespace:
# one of four main types of namespaces in Python
# the local namespace is created when a function is called and is destroyed when the function returns
# the local namespace contains all the names that are defined inside the function, including the function's parameters and any variables that are defined inside the function
# its deepest level is one level below the global namespace
# we can see this by defining a function and printing the locals() function which returns a dictionary representing the current local symbol table
global_var = 'global'

def add(a, b):
    local_var = 'local'
    print('Inside function:')
    print('Local Namespace:', locals())
    return a + b

print('Outside function:')
print('Global Namespace:', globals())
print('Local Namespace:', locals())
print(add(1, 2))

# observations:
# we can see that inside the function, the local namespace contains the function's parameters a and b, as well as the local variable local_var
# we can also see that outside the function, the local namespace is empty as we are not inside any function
# we can also see that the global namespace contains the global variable global_var and the function add

def add_two(n1, n2):
   sum = n1 + n2
   print('Inside function:')
   print(sum)
   print('Local Namespace:')
   print(locals())

add_two(3, 5)
print('Outside function:')
print('Local Namespace:')
print(locals())

# observations:
# we can see that the local namespace is created when the function is called and is destroyed when the function returns
# we can also see that the local namespace contains the function's parameters n1 and n2, as well as the local variable sum
# locals() function returns a dictionary representing the current local symbol table
# where we are calling the locals() function matters, as it will return different values depending on where it is called
# when called inside a function, it returns the local namespace of that function
# when called outside a function, it returns the local namespace of the module or script, as in it behaves like globals()
# when called at the top level of a module or script, it returns the global namespace
# when called inside a class, it returns the local namespace of that class
# when called inside a nested function, it returns the local namespace of the innermost function
# when called inside a lambda function, it returns the local namespace of the lambda function
# locals within a function does not include function it is nested within, since functions are not local variables and part of the local namespace

global_variable = 'global'



print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1/num2
  print(locals())

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())



print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:

divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:

multiply(4,50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())
print(globals())

# takeaways:
# locals() and globals() used outside a function behave the same way and return the global namespace
# locals() used inside a function returns the local namespace of that function


# enclosing namespace:
# one of four main types of namespaces in Python
# the enclosing namespace is created when a nested function is defined and is destroyed when the outer function returns
# the enclosing namespace contains all the names that are defined in the outer function, including the outer function's parameters and any variables that are defined in the outer function
# its deepest level is one level below the local namespace
# we can see this by defining a nested function and printing the locals() function which returns a dictionary representing the current local symbol table

# this is a special type of a local namespace
# enclosing namespaces are created when a nested function is defined
# just like with local namespace, it will only exist until function is done executing

global_variable = 'global'

def outer_function():
   outer_value = 'outer value'

   def inner_function():
      inner_value = 'inner value'
   inner_function()

outer_function()

# observations:
# we define a function called outer_function and nest another function inside it called inner_function
# to generate a namespace , functions needs to be called and executed, so we're calling them both
# here outer_function serves role of enclosing function and inner_function serves role of nested function or enclosed function
#  by this structure, we generate an enclosing namespace for outer_function and a local namespace for inner_function
# while python doesn't provide a built-in function to directly view the enclosing namespace, we can use the locals() function inside the inner_function to see the enclosing namespace
# to see locals of inner_function, we can add a print statement inside inner_function to print the locals() function
# locals() used within nested function will only show local variables of that nested function and not the enclosing function
# to see locals of outer_function, we can add a print statement inside outer_function to print the locals() function
# locals() used within outer_function will show local variables of that function, which also serves as the enclosing namespace for inner_function
global_variable = 'global'

def outer_function():
  outer_value = "outer"

  def inner_function():
    inner_value = "inner"
    print(locals())

  inner_function()
  # Added locals output
  print(locals())

outer_function()


# exercises:
print(globals())

def simple_math_func():
  x = 10
  y = 2
  mult = x * y
  add = x + y

print(locals())