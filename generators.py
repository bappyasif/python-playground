# Introduction to Generators
# in python a generator allows for creation of iterators without having to implement __iter__() and __next__() methods
# generators improve code readability, save memory by allowing for iterative access of elements and allow for traversal of infinite streams of data.

# there are two types of generators in python:
# 1. Generator Functions
# 2. Generator Expressions

# both of these return a generator object that can be looped over similar to a list, but unlike a list, contents of generator object are not stored in memory, allowing for complex and even infinite iteration of data.

# yeild vs return:
# generator functions are similar to regular functions except that they must return an iterator. but instead of using a `return` statement, generator functions use an exception called `yield`

# how does `yield` differ from `return` statement?
# any code that is written after a `yield` expression will execute on next iteration of iterator, whereas code after a `return` statement will never execute as the function terminates immediately.

# follwoing example shows how `yield` works in a generator function:
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
# usage of generator function
counter = count_up_to(5)
for number in counter:
    print(number)

def course_generator():
    yield "Mathematics"
    yield "Physics"
    yield "Chemistry"
    yield "Biology"

# usage of course_generator
courses = course_generator()
for course in courses:
    print(course)

# function `course_generator` will return an iterator that contains string values of courses. on each iteration of iterator each yield will return its corresponding course value until all values have been yielded.

# another key difference between `yield` and `return` is that `yield` expression will suspend execution of function and preserve any local variables that exist within function's scope. `return` statement on other hand will terminate function, discard any local variables that exist and return result to caller.

# like all objects, iterator object returned by a generator can be stored ina  variable to be used later. it can then  be iterated over using a loop as needed.

# exercise:
def class_standing_generator():
    yield "Freshman"
    yield "Sophomore"
    yield "Junior"
    yield "Senior"

# usage of class_standing_generator
class_standings = class_standing_generator()
for standing in class_standings:
    print(standing)



# next() and StopIteration:
# generator functions return an iterator object that contains traversable values. to retrieve next value from a generator object, we can use python built-in function `next()` which will cause generator function to resume its execution until next `yield` expression is encountered. after next `yield` expression found function will pause execution again and return yielded value to its caller.

# if no additional `yield` expressions are found in a generator function that means code has finished and a StopIteration exception will be raised to signal that there are no more values to be retrieved from generator object.

# generator functions are not limited to just single `yield` staements, they can also include loops where `yield` occurs multiple times based on loop conditions.

# to see this in action, imagine we have a dictionary of students and their student ID numbers. we want to hold a raffle where every student whose student ID is a multiple of 3 wins a prize A and every student whose ID is a multiple of 5 wins prize B. any student whose ID is a multiple of both 3 and 5 wins prize C.

def prize_generator():
    student_info = {
        "joan stark": 355,
        "jackie chan": 120,
        "brad pitt": 33,
        "angelina jolie": 25,
    }

    for student in student_info:
        name = student
        id = student_info[student]

        if id % 3 == 0 and id % 5 == 0:
            yield f"{name} wins prize C"
        elif id % 5 == 0:
            yield f"{name} wins prize B"
        elif id % 3 == 0:
            yield f"{name} wins prize A"

# since this is a generator function, local variable dictionary `student_info` is preserved while function executes with each `next()` call.
prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))
# print(next(prizes)) # will raise StopIteration

# exercise:
def student_standing_generator():
    student_standings = ["Freshman", "Sophomore", "Junior", "Senior", "Freshman"]

    for standing in student_standings:
        if standing == "Freshman":
            yield 500
    

standing_values = student_standing_generator()

print(next(standing_values))  # 500
print(next(standing_values))  # 500
# print(next(standing_values))  # StopIteration raised



# generator Expressions:
# generator expressions allow for a clean, single line definition and creation of an iterator object.
# by using a generator expression, there is no need to define a full generator function as shown earlier.
# generator expressions resemble syntax of list comprehensions, however they do differ in following ways:
    # 1. generator expressions returns newly defined iterator instead of a list
    # 2. generator expressions uses parentheses () instead of square brackets []

# lets look at an example of how two compare:

# list comprehension
squares_list = [x**2 for x in range(1, 6)]
print(squares_list)  # Output: [1, 4, 9, 16, 25]

# generator expression
squares_gen = (x**2 for x in range(1, 6))
print(squares_gen)  # Output: <generator object <genexpr> at 0x7f8b8d8c1c50>

# observations:
# squares_list will be a list containing all squared values from 1 to 5, while squares_gen will be a generator object that can not be accessed directly like a list. it needs to be iterated over to retrieve its values.

# sincer generator expressions return an iterator object, we can use a loop or the `next()` function to access its values one at a time.
for square in squares_gen:
    print(square)


# exercise:
def cs_generator():
    for i in range(1, 6):
        yield f"Computer Science {i}"

cs_courses = cs_generator()
for course in cs_courses:
    print(course)

# generator expression equivalent
cs_courses_gen = ("Computer Science "+str(i) for i in range(1, 6))
for course in cs_courses_gen:
    print(course)




# Generator Methods: send()
# python provides a few special methods to manipulate generators, one of which is `send()`.
# `send()` method allows us to send a value to a generator using `yield` expression.
# if you assign `yield` to a variable the nargument passed to `send()` method will be assigned to that variable. calling `send()` will also cause generator to perform an iteration.

# lets look at following example to see behavior of `send()` method:
# ex:01
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

echo = echo_generator()
# echo.send("Hello World")  # raises TypeError: can't send non-None value to a just-started generator
next(echo)  # prime the generator
echo.send("Hello World")  # Output: Received: Hello World
echo.send("Python Generators")  # Output: Received: Python Generators


# ex02:
def count_generator():
    while True:
        n = yield
        print(f"Counted to: {n}")

my_generator = count_generator()
next(my_generator)  # first iteration output:
next(my_generator)  # second iteration output: None
my_generator.send(10)  # Output: Counted to: 10
next(my_generator)  # fourth iteration output: None

# observations:
#  in code example ex02 above, generator definition contains line `n = yield`, this assigns value in `yield` to `n` which will be `None` unless a value is sent using `send()` method.
# last 4 lines of code are 4 iterations, 3 using `next()` function and 1 using `send()` method.
# 1st iteration produces no output since execution stops at `n = yield` which is before print statement.
# second call to `next()` resumes execution from where it left off, assigns `None` to `n` and prints `Counted to: None`.
# third call to `send(10)` resumes execution again, value 10 is passed through `yield` and assigned to `n` and prints `Counted to: 10`.
# fourth call to `next()` resumes execution again, assigns `None` to `n` and prints `Counted to: None`.

# send method can control value of generator when a second variable is introduced, one variable holds iteration count and other holds value passed through `yield`

def generator():
    count = 0
    while True:
        n = yield count

        if n is not None:
            count = n
        else:
            count += 1

my_generator = generator()
print(next(my_generator))  # Output: 0
print(next(my_generator))  # Output: 1
print(my_generator.send(10))  # Output: 10
print(next(my_generator))  # Output: 11
print(my_generator.send(20))  # Output: 20
print(next(my_generator))  # Output: 21

# observations:
# in above example, generator function defines `count = 0` as iteration value. 
# `n` is used to hold value provided by yield, just like next(), send() method returns value of recent iteration.
# in this example returned values are printed directly using print statements.

# `n = yield count` line has 2 behaviors:
    # 1. at start of each iteration value provided by `yield` is assigned to `n`, this value will be `None` ehen `next()` causes an iteration or it will be equal to value passed to `send()`
    # 2. end of each iteration value stored in `count` is yielded back to caller by generator.

# if `n` is not `None` value stored in `n` can be assigned to iterator variable `count`, this allows iterator to only change value of `count` when a value is sent using `send()` method. if `n` is `None` then iterator variable `count` is simply incremented by 1.

# exercise:
MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    yield student_id
    
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
  
  print(i)


# exercise:
MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
  if i == 1:
    i = student_id_generator.send(45)
  print(i)


# generator methods: throw()
# generator method `throw()` provides ability to throw an exception inside generator from caller point.
# this can be useful if we need to end generator once it reaches a certain value or condition.

def generator():
    i = 0
    while True:
        yield i
        i += 1

my_generator = generator()
for item in my_generator:
    print(item)
    if item > 5:
       break
        # my_generator.throw(ValueError, "Value exceeded limit of 5") # raises ValueError exception inside generator
        # my_generator.throw(StopIteration)  # raises StopIteration exception to end generator

# observations:
# in above example, generator function defines an infinite iterator that starts counting from 0.
# in for loop, each value yielded by generator is printed until value exceeds 5.
# once value exceeds 5, `throw()` method is called on generator object, which raises ValueError exception inside generator.
# if StopIteration exception is raised using `throw()` method, it will signal end of generator and terminate iteration.


# exercise:
def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  # Write your code below:
  if student_id > 100:
    break
    # student_generator.throw(ValueError, "Invalid student ID") # raises ValueError exception inside generator
  print(student_id)


# generator methods: close()
# generator method `close()` is used to terminate a generator early.
# once `close()` method is called generator is finished just like end of a loop, any further attempts to iterate over generator will raise StopIteration exception.

def generator():
   i = 0
   while True:
      yield i
      i += 1

my_generator = generator()
next(my_generator)  # Output: 0
next(my_generator)  # Output: 1
my_generator.close()  # Close the generator
# next(my_generator)  # Raises StopIteration

# observations:
# in above example, generator function defines an infinite iterator that starts counting from 0.
# first two calls to `next()` function retrieve values 0 and 1 from generator.
# then `close()` method is called on generator object, which terminates generator.
# any further attempts to call `next()` on closed generator will raise StopIteration exception.

# `close()` method works by raising a GeneratorExit exception inside generator, which signals generator to terminate. this exception is generally ignored but can be handled using try-except block inside generator if needed.

def generator():
      i = 0
      while True:
        try:
            yield i
        except GeneratorExit:
            print("Early exit, byeee!!")
            break
        i += 1

my_generator = generator()
for item in my_generator:
   print(item)
   if item >= 5:
      my_generator.close()

# observations:
# in above example, generator function defines an infinite iterator that starts counting from 0.
# inside generator, a try-except block is used to catch GeneratorExit exception raised by `close()` method.
# when generator is closed after yielding value 5, exception is caught and message "Early exit, byeee!!" is printed before generator terminates.

# putting `yield` expression in a `try` block we can handle `GeneratorExit` exception. in this case we simply print a message and break out of loop to end generator gracefully.
# because we interrupted normal flow of generator using `close()` method, we must also use `break` statement to exit loop, otherwise a `RuntimeError` will be raised indicating that generator ignored `GeneratorExit` exception.

# exercise:
def student_counter():
   for i in range(1, 200):
      yield i

student_generator = student_counter()
for student_id in student_generator:
   if student_id > 100:
      student_generator.close()
      break
   print(student_id)


# connecting generators:
# there are some cases where it is useful to connect multiple generators into one. this allows us to delegate operations of one generator to another sub generator.
# connecting generators is similar to using itertools `chain()` function combine iterators into a single iterator but connecting generators allows for more complex interactions between generators.

# in order to connect generators we use `yield from` statement, an example of how it is used is shown below:
def cs_courses():
   yield "Computer Science 101"
   yield "Computer Science 102"

def art_courses():
   yield "Art History 101"
   yield "Painting 101"

def all_courses():
   yield from cs_courses()
   yield from art_courses()
   yield "Physical Education 101"

combined_generator = all_courses()

# print(next(combined_generator))  # Output: Computer Science 101
# print(next(combined_generator))  # Output: Computer Science 102
# print(next(combined_generator))  # Output: Art History 101
# print(next(combined_generator))  # Output: Painting 101
# print(next(combined_generator))  # Output: Physical Education 101
# print(next(combined_generator))  # Raises StopIteration

for course in combined_generator:
   print(course, "!!")

# observations:
# in above example, we have 3 generator functions: `cs_courses()`, `art_courses()`, and `all_courses()`.
# `all_courses()` generator uses `yield from` statement to delegate yielding of values to `cs_courses()` and `art_courses()` generators.
# when we iterate over `combined_generator`, it will yield all courses from both sub generators as well as "Physical Education 101".
# `yield from` statement simplifies code by eliminating need for nested loops to iterate over sub generators. it also allows for seamless integration of multiple generators into a single generator function.

# exercise:
def science_students(x):
   for i in range(1, x+1):
      yield i

def non_sceience_students(x, y):
   for i in range(x, y+1):
      yield i

def all_students():
   yield from science_students(5)
   yield from non_sceience_students(6, 10)
   yield from non_sceience_students(20, 29)

student_generator = all_students()

for student_id in student_generator:
   print(student_id)


# generator pipelines:
# generator pipelines allows us to use multiple generators to perform a series of operations all within one expression.
# we can break down complex operations into smaller, more manageable parts where they can be pipelined together to achieve desired output.

# to pipeline generators, output of one generator function can be input of another generator function, resulting generator can then be used as input for another generator function and so on.

# pipeline generators are also often referred to as "nested generators", we can use a pipeline generator like this below:

def number_generator():
   i = 0
   while True:
      yield i
      i += 1

def even_number_generator(numbers):
   for number in numbers:
      if number % 2 == 0:
         yield number

even_numbers = even_number_generator(number_generator())

for even in even_numbers:
   print(even)
   if even >= 10:
      break
   
# observations:
# in above example, we have two generator functions: `number_generator()` and `even_number_generator()`.
# `number_generator()` generates an infinite sequence of numbers starting from 0.
# `even_number_generator()` takes an input generator and yields only even numbers from that generator.
# we create a pipeline by passing the output of `number_generator()` as input to `even_number_generator()`.
# when we iterate over `even_numbers` generator, it will yield even numbers from the infinite sequence generated by `number_generator()`.
# we use a break condition to stop iteration once we reach an even number greater than or equal to 10.
# output is finite since `number_generator()` is infinite but `even_number_generator()` filters out odd numbers, resulting in a finite sequence of even numbers.

# to note, even_numbers generator variable holds an `even_number_generator()` object with `number_generator()` object as its input.
# when we iterate over even_numbers only even numbers from infinite sequence are yielded.

# exercise:
def course_generator():
   yield("Computer Science", 5)
   yield("Mathematics", 4)
   yield("Physics", 3)
   yield("Biology", 4)

def add_five_students(courses):
   for c, n in courses:
      yield (c, n+5)

increased_students = add_five_students(course_generator())

for course in increased_students:
   print(course, course[0], "now has", course[1], "students")


# review:
# in this lesson we learned how to:
# 1. create generator functions using `yield` expression
# 2. implement generator expressions for concise iterator creation
# 3. use generator methods like `send()`, `throw()`, and `close()`
# 4. connect generators into single generator using `yield from`
# 5. use nested generators to create generator pipelines for complex data processing tasks.

# exercise:
def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'
# Write your code below:
# def graduation_countdown(days):
#    while days >= 0:
#       yield days
#       days -= 1

# refactor graduation_countdown so that we can make use of `send()` method
# def graduation_countdown(days):
#    while days >= 0:
#       new_day = yield days
#       if new_day is not None:
#          days = new_day
#       else:
#          days -= 1

# Modify the graduation_countdown() generator function to accept values sent using send(). Use a local variable called days_left to store sent values. Use an if/else statement to check for sent values.
def graduation_countdown(days):
   while days >= 0:
      days_left = yield days
      if days_left is not None:
         days = days_left
      else:
         days -= 1
days = 10
# countdown_generator = graduation_countdown(days)
# generator expression for descending days that is equivalent to graduation_countdown function

countdown_generator = (day in range(days, -1, -1) for day in range(days, -1, -1))

grad_days = graduation_countdown(days)

for day in grad_days:
   if day == 15:
      grad_days.send(10)
   print(f"Days Left: {day}")

gpas = [3.2, 4.0, 3.6, 2.9]

def honors_generator(gpas):
   for gpa in gpas:
        if gpa >= 3.9:
             yield from summa()
        elif gpa >= 3.7:
             yield from magna()
        elif gpa >= 3.5:
             yield from cum_laude()

honors = honors_generator(gpas)
for honor in honors:
   print(honor)