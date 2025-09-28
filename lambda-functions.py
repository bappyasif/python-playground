# more concise way to write a small anonymous function
# lambda functions are defined using a lambda keyword
# these functions are used for simple tasks
# unlike regular def functions they dont have any names and used inline for small tasks

# regular function
def add(num1, num2):
    return num1 + num2

print(add(1, 2))

# lambda function
sqrd = lambda n2: 2 ** n2

print(sqrd(2))

# syntax of lambda functions
# lambda [arg1, arg2, ....]: [expression]

addBy2 = lambda n1,n2: n1 + n2 + 2

print(add(1, 2))

greet = lambda name: f"Hello {name}"

print(greet("Bappy"))

# using lambda functions with map, filter, sorted higher order functions

# higher order functions are functions that operate on other functions

# map
# map applies given lambda function on each item in an iterable

nums = [1, 2, 3, 4, 5]

squared = map(lambda num: num **2, nums)

print(list(squared))

# filter
nums = [1, 2, 3, 4]

evens = list(filter(lambda n: n%2 == 0, nums))

print(evens)

# sorted
students = [("Alice", "A", 95), ("Bob", "B", 88), ("Charlie", "C", 92)]

sorted_students = sorted(students, key=lambda student: student[2])

print(sorted_students)

studs = [{"name": "Alice", "grade": "A", "score": 95}, {"name": "Bob", "grade": "B", "score": 88}, {"name": "Charlie", "grade": "C", "score": 92}]

srtd_studs = sorted(studs, key=lambda studs: studs.get("score"))

print(srtd_studs)

# Advantages and Limitations

# Advantages:
# they are concise and easy to read for simpler tasks
# they are convient for small and throw away functions, specially as arguments for other functions like higher order functions

# disadvantages:
# they can only contain expression and not statements
# they are limited to a single expression
# tey can be harder to debug due to their lack of names

# best practices: 

# use them when:
# you need a simple and short function
# you need to pass a function as an argument to another function

# don't use them when:
# you need a complex function which requires multiple lines of code
# you need to reuse same function multiple times the use a regular function with def instead