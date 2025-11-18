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


# class based context managers II:
# now that we know structure of implementing our own class based context manager, lets walk through a context manager that manages actual files as well as explore each of methods we saw earlier 
class WorkWithFile:
   def __init__(self, file, mode):
      self.file = file
      self.mode = mode

   def __enter__(self):
      self.opened_file = open(self.file, self.mode)
      return self.opened_file
   
   def __exit__(self, *exc):
      self.opened_file.close()

# we have written a class based context manager called `WorkWithFile` lets breakdown each method and see what it does
# __init__ method:
    # __init__ method takes three arguments
      # 1. self: this is standard for any class we work with and allows us to work with methods properties we assign to an instance of a class
      # 2. file: since we are working with we need to be able to take in a file argument when we call class with a `with` statement
      # 3. mode: lastly we need to provide file a mode, this allows us to manage what our context manager will actually be doing, such as writing, reading or both!
   # both `file` and `mode` arguments allows us to accomplish following syntax: `with WorkWithFile('data/somefile.txt', 'w')`
# __enter__ method:
    # this is where we deal with opening file we want to work on, since any new instance of our context manager will have a `file` an d `mode` property we can pass them into `open()` function to open a specific file with a specific mode. then we save it as a variable called `self.opened_file` and return it. 
   #  by returning `self.opned_file` file will be passed into variable we define when we call it with `with` statement `with WorkWithFile('data/somefile.txt', 'w') as file` we will assign self.opened_file to a variable called `file` thus allowing us to use it in  `with` statement

# __exit__ method:
   # this method is used to close our file after we are done with it. we can use it to close any resources that are no longer in use.
   # here we are still taking `*exc` argument but we wont touch on that until we cover them soon, for now this module is solely responsible for closing our file

# now that we created our context manager we can now use it with `with` statement

with WorkWithFile('data/somefile.txt', 'w') as file:
   file.write('some text')

# here is breakdown of what's happening under hood:
   # 1. `with` statement executes and a context manager object is created  from class provided with values of arguments required in `__init__` method
   # 2. `__enter__` method is run
   # 3. __enter__ method calls `open()` function on "file_name.txt" with mode of "w" which represents write mode and return a handle to opened file
   # 4. then code block in `with` statement is executed and writes "some text" to "file_name.txt"
   # 5. finally block in `with` statement is executed and `__exit__` method is called
   # 6. `__exit__` method calls `close()` function on opened file

# exercise:
# Write your code below:
class PoemFiles:

  def __init__(self, poem_file, mode):
    print("Starting up a poem context manager")
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print("Opening poem file")
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
    
  def __exit__(self, *exc):
    print("Closing poem file")
    self.opened_poem_file.close()


with PoemFiles('data/somefile.txt', 'w') as open_poem_file:
   open_poem_file.write('Hope is the thing with feathers')


# handling exceptions I:
# rememebr this? `def __exit__(self, *exc)`, its time to address this big mystery, what is `*exc` argument?
# well, it allows us to catch any exception that occurs inside of context manager and deal with it. lets see how to do that

# context managers play an important role in handling exceptions, recall exceptions are errors that happen within runtime of a code, terminating it before its completion. within a context manager `__exit__` methoid is responsible for dealing with any excepttions. it can implement hoe to close any openened file and any other olperations that we want to perform if an exception occurs

# so far we have been using `*exc` to fill in argument requirements for our context managers `__exit__` method, if want to define it without using `*exc` will produce an error, this is because `__exit__` method needs total four argments! we ign ored this requirement by using `*exc` argument which allows us to pass any number of arguments to our context manager `__exit__` method

# __exit__ mtehod has three requirements in addition to `self`:
   # 1. an exception type: which indicates class of exception that occured (i.e. AttributionError or NameError)
   # 2. an exception value: actual value of occured error
   # 3. a traceback object: a report detailing sequence of steps that caused error and all details needed to fix it

# lets take an example context manager that deals with __exit__ method

class Openfile:

   def __init__(self, file, mode):
      self.file = file
      self.mode = mode

   def __enter__(self):
      self.opened_file = open(self.file, self.mode)
      return self.opened_file
   
   def __exit__(self, exc_type, exc_value, traceback):
      print(exc_type, exc_value, traceback)
      self.opened_file.close()

# in this `__exit__` method we are dealing with exceptions b y adding a script that prints exception values to console, we can see outcome of our simple exception handling when we run our `with` statement with an intentional failure

with Openfile('data/somefile.txt', 'r') as open_file:
   # open_file.see() # intentional error: AttributeError
   pass

# once `with` statement is run, we get above error message that tells us that we have an `AttributeError` that our object does not have `see()` method and provides a traceback object.
# when an error occurs, code stops and resources (i.e. files) are stil closed , values of these three arguments are then thrown or suppressed.
# in contrast if no error occurs in `with` statement above `__exit__` method would have printed out `None` for exception type, `None` for exception value and `None` for traceback object
# note that `exc_type`, `exc_value` and `traceback` arguments are completly arbitary names, we can use any names we want for these parameters as long as it does not hinder readability of our code, its best practice to be as descriptive as possible!

# exercise:
class PoemFiles:

   def __init__(self, poem_file, mode):
      print("Starting up a poem context manager")
      self.file = poem_file
      self.mode = mode

   def __enter__(self):
      print("Opening poem file")
      self.opened_poem_file = open(self.file, self.mode)
      return self.opened_poem_file
   
   def __exit__(self, exc_type, exc_value, traceback):
      print("Closing poem file")
      print(exc_type, exc_value, traceback)
      self.opened_poem_file.close()

# First
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second
with PoemFiles('data/poem.txt', 'r') as file2:
  print(file2.read())
  print("---- Exception data below ----")