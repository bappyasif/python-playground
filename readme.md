<!-- python gotcha: Mutable default arguments -->

# A python gotcha:
## when writing a functionwith default arguments, it can sometimes be tempting top include an empty list as default argument to that function

> for instance lets suppose, we were building an application for a school. we want to have a function that can generate new students and return a dictionary of students name, age and grades. since most students enter schools without anjy grades so we can assume to store an empty lists for that.

```python
def createStudent(name, age, grades=[]):
    return {"name": name, "age": age, "grades": grades}

# lets create two students
chris = createStudent("chris", 20, 15)
bree = createStudent("bree", 19)
print(chris, bree)

# for adding a grade
def addGrade(student, grade):
    student["grades"].append(grade)
    print(student, student["grades"])

    return student

addGrade(chris, 100)
addGrade(bree, 90)

# expected output for addGrade
[100]
[90]


# actual output
[100]
[100, 90]

```
that doesnt look right, whyt does bree has 100 grade of chris into hers?

>> which is know as gotcha, a counterintuitive feature of a programing language taht often leads to mistakes in programs.

```python
def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order
# first order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})
# second order, pasta
order2 = update_order({'item': 'pasta', 'cost': '8.00'})

# whats in that second order again?
print(order2) # [{'item': 'burger', 'cost': '3.50'}, {'item': 'pasta', 'cost': '8.00'}] and not just pasta, its both burger and pasta.
```

# Mutables and Functions
> to understand this gotcha we must first establish what python classifies as mutable.

a mutable object refers to various containers in python that are intended to be modified. a list for example is a mutable object with its append, remove operations. sets and dictionaries are also mutable.

some of objects are not mutables in python and are therefore OK to be used as default arguments. int, float and other numbers cant be mutated(arithmatic operations will return a new number).

tuples are a kind of immutable list, and strings are also immutable since operations that update a string will all return a completely new string.

> when using a mutable object in function arguments, its important to note: deault parameters values are evaluated from left to right, when function is defined and that same "pre computed" value is used for each call

this means when we call a function, default values we provide for parameters are created only once, and used for each subsequent calls of that function.

which means our `grades=[]` from our earlier example was only created once and anytime we tried to access it, that same list was being modified.

we can even see that memory id of grades for each student is also same using builtin in id() function, confirming our above finding.

```python
print(id(chris["grades"]))
print(id(bree["grades"]))

# expected output
# some memory id that are same for chris and bree both
```

while this may seem like a headscratcher for many, tehre is a walkaround this gotcha if we ever do want to use mutable default argument. we use keyword `None` to get around this gotcha.

# None workaround
if we want an empty list as a potential default argument value, we can use `None` as a special value to indicate we did not recieve anything.

after we check whether an argument was provided we can instantiate a new list if it wasnt earlier.

```python
def createStudent(name, age, grades=None):
    if grades is None:
        grades = []
    return {"name": name, "age": age, "grades": grades}

def addGrade(student, grade)
    student["grades"].append(grade)
    return student

# lets create two students
tom = createStudent("tom", 20)
sue = createStudent("sue", 19)
print(tom, sue)

addGrade(tom, 100)
addGrade(sue, 90)

print(id(tom["grades"]))
print(id(sue["grades"]))

# expected output
[100]
[90]

# actual output
[100]
[90]
```

> While it may seem more cumbersome to write the `if` clause, this is one of the most common (and flexible) ways to avoid running into issues with mutable default arguments.

