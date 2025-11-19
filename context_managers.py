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


# handling exceptions II:
# printing exceptions isnt only way can handle them in `__exit__` method, an exception that occurs in a context manager can be handled in two ways
   # 1. if we want to throw an error when an error occurs we can either:
      # return`False` after `close` method is called
      # or do nothing and let the error propagate
   # 2. if we want to suppress an error, we can:
      # return `True` after `close` method is called

# lets see how to do that
class OpenFile:

   def __init__(self, file, mode):
      self.file = file
      self.mode = mode

   def __enter__(self):
      self.opened_file = open(self.file, self.mode)
      return self.opened_file
   
   def __exit__(self, exc_type, exc_value, traceback):
      print(exc_type, exc_value, traceback)
      print("Exception has been handled")
      self.opened_file.close()
      return True
   
# notice above that nothing changed except for adding of `retrun True` to implement suppression of an error. To see this in action, we'll call two `with` statements using this context manager, one that wil throw an exception and another that will not

with OpenFile('data/somefile.txt', 'r') as file:
   # .see() # intentional error: AttributeError
   print("---- Exception data below ----")
   file.see()
   print(file.see())


with OpenFile('data/somefile.txt', 'r') as file2:
   file2.read()

# here's what we see:
   # error message we manually coded is printed but there is no automatic error message thrown by program
   # both `with` statements ran

# if we did not return `True` second and all proceeding `with` statements would not have run since an exception would be hit
# additionally we can choose to handle a specific exception while suppresssing it. this is useful if we want our context manager to not block execution of other code but also customize output if a certain exception occurs.
# here is an example of working with a TypeError

class OpenFile:

   def __init__(self, file, mode):
      self.file = file
      self.mode = mode

   def __enter__(self):
      self.opened_file = open(self.file, self.mode)
      return self.opened_file
   
   def __exit__(self, exc_type, exc_value, traceback):
      self.file.close()
      if isinstance(exc_value, TypeError):
         print("TypeError has been handled")
         return True

# notice `if` statement that compares `exc_value` to a specific exception we are trying to catch. anything we want to happen for this specific exception can occur in conditional code block. lastly we return `True` to make sure we suppress exception from arising and stopping rest of our code from running

# cause for an typerror
# with OpenFile('data/somefile.txt', 'r') as file:
#    # file.read() # intentional error: TypeError
#    print("---- Exception data below this ----")
#    file.read()

# remember that `__exit__()` method's primary responsibility is to close resource context manager is working with. in this example, we close file first before handling error so that it will always run

# exercise:
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below: 
    self.opened_poem_file.close()
    if isinstance(exc_value, AttributeError):
      return True
    

with PoemFiles('data/poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('data/poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")


# Contextlib introduction:
# we have learned that we can create our own context managers using class based method but there's an even simpler way of creating context managers. we can use a built in python module called `contextlib` 

# `contextlib` module allows for creation of a colntext manager with use of a generator function(a function that uses `yield` instead of `return`) and contextlib decorator `@contextmanager`
# instead of creating a class and defining `__enter__` and `__exit__` methods, we can use `@contextmanager` decorator function to create a context manager

# there are few steps in setup so lets take it slow and break it down each step, first we''ll need to import built-in module into our script and grab `@contextmanager` decorator

from contextlib import contextmanager
# once we have successfully imported module we can automatically use `@contextmanager` decorator to wrap a simple generator function

@contextmanager
def open_file_contexxtlib(file, mode):
   opened_file = open(file, mode)

   try:
      yield opened_file
   finally:
      opened_file.close()

# we are doing a few things here
   # we have written a generator function called `open_file_contextlib` with expectation that it will take two arguments a file and a mode
   # we then used built-in `open()` function to open a file that we recieved as an argument and save it to a variable called `opened_file`
   # function then will attempt via a `try` statement to yield opened file and complete whatever code we pass to it when we use it in conjunction with `with` statement
   # lastly resource (file) will be closed once all code is done executing

# if we think about this structure in sections relative to class based approach, it essentially breaks down into this:
# @contextmanager
# def generator_name(<parameters>):
#    <setup section - equivalent to __enter__>
#    try:
#       yield <return value>
#    finally:
#       <cleanup section - equivalent to __exit__>

# once we have created this function and denoted it as a context manager using `@contextmanager` decorator, we can immediately use it like before in a `with` statement
with open_file_contexxtlib('data/somefile.txt', 'w') as file:
   file.write('some text, We just made a context manager using contexlib!')

# following this pattern of creating context managers allows us to quickly convert generator functions to become context managers without need of to create any extra classes. now lets remake our poem context managers following this pattern

# exercise
@contextmanager
def poem_files(file, mode):
  print("Opening File")
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print("Closing File")
    open_poem_file.close()

with poem_files('data/poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')

# contextlib error handling:
# in previous exercise we explored how to create a context manager using `contextlib` module. however we didnt go over to deal with errors just as we did with class based approach.
# like anyother pattern you may run into error when invoking your context manager using @contextmanager decorator.

# for class based context manager `__exit__` method dealt with exceptions, for decorator method errors are most commonly dealt with within an `except` block. we will build on top of our `try/finally` block by incorporating `except`, there are two main ways to handle errors when using `contextlib` module:
   # 1. to throw an error and stop execution of our entire program, we can:
      # simply do nothing by excluding an `except` block
   # 2. to catch errors and continue execution our program, we can:
      # handle exception in an `except` block

@contextmanager
def open_file_contextlib(file, mode):
   open_file = open(file, mode)

   try:
      yield open_file

      # exception handling
   except Exception as exception:
      print("We hit an exception: ", exception)
   finally:
      open_file.close()

with open_file_contextlib('data/somefile.txt', 'w') as file:
   # file.write('some text, We just made a context manager using contexlib!')  # this okay
   file.sign('some text, We just made a context manager using contexlib!')  # this will throw an error

# observations:
# inclusion of `except` clause
# `except` attempts to catch a generic exception, if its hit it save it to a variable called `exception`, note we can use any exception object, not just a generic one, if we know what type of exception is being thrown we can use that instead
# handler print out a message and continue execution of our program

# with this context manager is called in `with` statement above, it will hit exception block because `.sign ()` is not a file method, and that tells us what our error is, so we know how to fix it.

# exercise
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  #Write your code below: 
  except AttributeError as e:
    print(e)

  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('data/poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.sign('Buzz is big city. big city is buzz.')

# nested context managers:
# so far we have only been using context managers within context of one file. in most programs there might be a need to use context managers for a couple of different scenarios that include working with multiple files, for example we might want to:
   # work with information from multiple files
   # copy same information to multiple files
   # copy information from one file to another
# to accomplish this goal of working with multiple resources at once, context managers can be nested together in a `with` statement to manage multiple resources simultaneously 

# lets imagine we have two files: `teacher.txt` and `student.txt` and we want to copy information from one to the other
# with open('data/teacher.txt', 'w') as teacher_file, open('data/student.txt', 'w') as student_file:
#    teacher_file.write(student_file.read())

# notice:
# `with` statement is being called once but invoking two context managers, this is a single line nested `with` statement
# each context manager is separated by a comma and has its own target variable
# our `teacher.txt` is opened in write mode because it will be written into and our `student.txt` is opened in read mode because we are attempting to copy text into teacher's file
# teacher.txt file will now include everything that was in student.txt file
# here we have chosen to use `open` built-in function rather than a custom context manager. it is entirely possible to use our own in place of `open` function as well

# we can also write above `nested` context managers in a slightly different way:
# with open('data/teacher.txt', 'w') as teacher_file:
#    with open('data/student.txt', 'r') as student_file:
#       teacher_file.write(student_file.read())

# notice this syntax is almost similar to first method however there are some differences:
   # `with` statement is called twice
   # `with` statement to open `student.txt` in read mode is nested in code block of `with` statement that opens `teacher.txt` in write mode
   # this method, though slightly longer gives a clearer visual of nesting and is preferable when working with multiple context managers

# exercise:
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File')
    open_card_file.close()

# Write your code below: 
# with card_files('data/card.txt', 'w') as card_file, poem_files('data/poem.txt', 'a') as poem_file:
#   card_file.write(poem_file.read())
with poem_files("data/poem.txt", "r") as poem: 
  with card_files("data/card.txt", "w") as card:
    print(poem)
    print(card)
    card.write(poem.read())

# review:
# we have explored many of core concepts behind context managers.
# context managers:
   # context managers are a form of resource management in python invoked by `with` statement 
   # they ensure that resources are closed/released after usage regardless opf whether or not an error occurs
   # they can be created from scratch using either class-based method or `contextlib` decorator based method
   # behind every contetx managre there's an `__enter__` and `__exit__` method taking place
   # context managers can be nested together to work with resources simultaneously

# class based context managers:
   # they can be created from scratch with manual implementation of `__enter__` and `__exit__` method
   # `__exit__` method takes three arguments: an exception type, an exception value and a traceback object, method can then handle exceptions

# decorator based context managers:
   # they can be created from scratch using `contextlib` module decorator `@contextmanager`
   # `contextlib` method `except` block handles exceptions code block