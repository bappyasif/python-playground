# context managers

# a familiar face: `with` statement
# one of most common ways to manage resources in python is to make sure that files are used in our scripts are closed after we are done with them
# `with` statment is most pythonic way of invoking a context manager

# lets see how to use `with` statement

with open('data/somefile.txt', 'w') as file:
    file.write('some text')

# observations commentary:
# `with` statement calls built-in open() function on "file_name.txt" with mode of "w" which represents write mode
# `as` clause assigns object opened file to a aterget variable named `file` which can be accessd inside of context manager
# `file.write()` writes a scentence top "file_name.txt"

# but what exactly does this have to do with resource management? in order to answer this question, we need to take a peek behind curtain and examine what our code looks like without use of a context manager like `with`

file = open('data/somefile.txt', 'w')
try:
    file.write('some text')
finally:
    file.close()

# observations commentary:
# open() function is called on "file_name.txt" with mode of "w" which represents write mode
# file.write() writes a scentence top "file_name.txt"
# file.close() is called at the end of the try block

# alternative to using `with` would require us to manually open using open() and close using close() file we were working on
# by using `with` statement in first example, it serves as a context manager where files are automatically closed after script completion and we dont ever have to worry about any possibvlity of forgetting to close a resource.
# remember leaving our resources open will hog up our finite computer resources and eventually cause us to run out of memory, we are never guranteed that python will close our resources for us, so we need to make sure we close our resources when we are done with them

# exercise: to read a file without usiong `with` statement
# open_file = open('./data/file_name.txt', 'r') # getting no file found error
# open_file = open('data/flie_name.txt', 'r')
# print(open_file.read())
# open_file.close()

try:
  open_file = open('data/file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

# now rewriting this using `with` statement
with open('data/file_name.txt', 'r') as open_file:
  print(open_file.read())


# class based context managers:
# now that we have an understanding of why we need context managers and power of `with` statement, it is essential for us to know what's happening under hood to gain a much deeper understanding of concept. best way to see internal workings of a context manager such as `with` statement is by creating our own

# one of two approaches of creating context managers is referred to as class-based approach. class based approach of writing context managers requires explicitly defining and implementing following two methods inside of a aclass:

    # __enter__
        # __enter__ method allows for setup of context managers, this method commmonly takes care of opening a resource like a file. this method also begins what what is known as runtime context - period of time in which a script runs. in our previous example, it was time in which code passed inside of `with` statement code was executed under hood 

    # __exit__
        # __exit__ method ensures breakdown of context manager. this method commonly takes care of closing open resources that are no longer in use 

# to visualize these methods and approach, lets take a look at the following example
class ContextManager:
   def __init__(self):
      print("initializing class....")
    
   def __enter__(self):
      print("entering context....")
    
   def __exit__(self, exc_type, exc_value, traceback):
      print("exiting context....")

# here we defined a new class called `ContextManager` and implemented required methods.
# by defining two methods in our class we are implementing a context manager - a guideline for context management protocol
# implementing context management protocols allows us to immediately invoke class using `with` statement
with ContextManager() as context:
   print("inside context")

# here we invoke `ContextManager` class with a `with` statement
# after running code our output of this context manager would be

# above code shows that our context manager class is executed in following sequence:

    # initializing class... __init__
    # entering context... __enter__
    # inside context  `with` statement
    # exiting context... __exit__

# exercise:
class PoemFiles:
   def __init__(self):
      print("initializing class....")
   
   def __enter__(self):
      print("opening peom file!")

   def __exit__(self, exc_type, exc_value, traceback):
      print("closing poem file!")
    
with PoemFiles() as manager:
   print("Hope is with feathers")
