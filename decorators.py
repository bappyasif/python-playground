# decorators
# decorators are functions that modify the behavior of other functions
# decorators can be used to add functionality to functions, such as logging, caching, or authentication
# and it makes it so by making it more readable and maintainable

# we will be lookin at these 6 section: most of which are already covered extensively
# 
# 1. functions as first class objects
# 2. functions as arguments
# 3. functions as return values
# 4. decoratoring a function
# 5. decorators 
# 6. decorators w/ parameters

# 1. functions as first class objects
def add_five(x):
    print(x + 5)
    return x + 5
add_five(10) # 15
t = {"a": 1}
a = "a"
print(add_five, type(add_five), t, type(t), a, type(a)) # <function add_five at 0x7f6e2b4b6f40> # this is a function object
# without () it is a function object, with () it is a function call

# 2. functions as arguments: functions within functions
def add_5(func, x):
    def add_2(x):
        return x + 2
    
    print(func(x) + 5)
    return func(x) + 5 + add_2(x)
add_5(add_five, 10) # 17
add_5(lambda x: x + 5, 10) # 17

# 3. functions as return values
def get_math_function(operation):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    if operation == "+":
        return add
    if operation == "-":
        return subtract
    if operation == "*":
        return multiply
    if operation == "/":
        return divide
add = get_math_function("+")
subtract = get_math_function("-")
multiply = get_math_function("*")
divide = get_math_function("/")
print(add) # <function get_math_function.<locals>.add at 0x7f6e2b4b6f40>
print(subtract) # <function get_math_function.<locals>.subtract at 0x7f6e2b4b6f40>
print(multiply) # <function get_math_function.<locals>.multiply at 0x7f6e2b4b6f40>
print(divide) # <function get_math_function.<locals>.divide at 0x7f6e2b4b6f40>
print(add(10, 5)) # 15
print(subtract(10, 5)) # 5
print(multiply(10, 5)) # 50
print(divide(10, 5)) # 2


# 4. decoratoring a function

def add_title_decorator(func):
    def wrapper():
        print("Professor")
        func()
    return wrapper

def add_decor(func, name):
    def wrapper():
        print("Greetings")
        func(name)
    return wrapper
    
def print_my_name():
    print("John")
    return "John"
print_my_name() # John

def print_another_name():
    print("Jane")
    # return "Jane"
print_another_name() # Jane

def print_name(x="JJ"):
    print(x)
print_name("A. B.") # A. B.

decorated_function = add_title_decorator(print_my_name)
# print(decorated_function()) # Mr. John
decorated_function() # Mr. John

decorated_function = add_title_decorator(print_another_name)
# print(decorated_function()) # Mr. Jane
decorated_function() # Mr. Jane

decorated_function = add_title_decorator(print_name)
# print(decorated_function("A. B.")) # Mr. A. B.
# decorated_function("A. B.") # Mr. A. B.
print(decorated_function) # <function add_title_decorator.<locals>.wrapper at 0x7f6e2b4b6f40>
# print(decorated_function("A. B.")) # Mr. A. B # error for type eroor due to positional arguments

decorated_function = add_decor(print_name, "A. B.")
# print(decorated_function()) # Greetings A. B.
decorated_function() # Greetings A. B.


# 5. decorators
# in python, decorators are functions that are used to modify the behavior of other functions
# we denote decorators with the @ symbol

# instead of writing decorated_function = add_decor(print_name, "A. B.") and then decorated_function(), we can simply denote decorated_function = @add_decor(print_name, "A. B.") and then decorated_function() to get the same result

def greet_decor(func):
    def wrapper(name):
        print("Greetings")
        func(name)
    return wrapper

@greet_decor
def print_name_decorated(x):
    print(x)
print_name_decorated("<A. B.>") # Greetings A. B


# 6. decorators with arguments
def salutation_decor(func):
    def wrapper(*args, **kwargs):
        print("Dear earthling")
        func(*args, **kwargs)
    return wrapper

@salutation_decor
def print_name_decorated(x):
    print(x)
print_name_decorated("<A. B.>") # Dear earthling A. B.

@salutation_decor
def print_info(x, a):
    print(f"{x}, you are {a} years old")
print_info("<A. B.>", 20) # Dear earthling A. B., you are 20 years old

# observations:
# we can use decoirator without have to denote them with the @ symbol b ut using it with them makes syntax simpler (reference 4 and 6)
# decorators are pythons syntactic sugar, it is a way to make code more readable and maintainable