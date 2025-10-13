# why object oriented programming?

## features of object orientation

> what each program has

it has data and behavior, where data is what program knows such as (is it complete? task description for a todo list app) and behavior is what a program can do for instace it can toggle a task complete or incomplete for a todo list app

## programming paradigms
* procedural
* object oriented
* functional
<!-- * declarative -->

### procedural programming:
both data and behavior is spread out in same set of step by step instructions

we manipulate data directly with behavior onto program set and thus changing overal state of our program

order of our code matters very much and our data is mutated directly as program carries out its behavior

### functional programming:
data and behavior is kept separate

if we want to change or mutate our data directly, we would abstract that with a corresponding behavior which would take new data into consideration and update data in program

we never mutatae data directly but rather through an abstracted pure functions to update a new copy of updated data

### object oriented programming:
data and behavior are groupped together as objects

object is a special entities in our program, which will have all data, attributes or method or behaviors into an easy to use container

for instance we would have one method for adding and another for toggle tast status and among others

#### four pillars of object orientation
* encapsulation
* abstraction
* inheritance
* polymorphism

#### encapsulation
groupping of data and behaviors into an object

for instance we would create a Task class with task data and its behaviors. 

every instantiations of that class for tasks would have those data and behavior groupped together for them to access and modify

it also limits data scope so that it cant interfere with other containers

it bundles data and behavior together that should be together and realted to each other

#### abstraction
ability to hide its copmplex logic from user, making coee easier to use in otehr places

for instance when you write up and send an email to people, you simple open up your email client and write and then send, without having to know what goes on underneath to make it happen

for our Task app examples, we are totally abstracting its behavior of how its actually toggling it by that toggle method and simply get data state with its isComplete data

#### inheritence
allows a class to have all data and functionalities of another class

which allows us to share code between multiple classes

reduces code duplications in codebase

for instance, lets say we have another TaskWithDeadline class wich has all data and behaviors of Task class but with deadline, so we can let out Deadline Task class inherits data and behavior from our Task class without have to rewriet any of that Task related code for TaskWithDeadline class

#### polymorphism
polymorphism likterally means having multiple forms

when we are using inhertence in our classes we can make use of polymorphism

we have to look at those instantiated objects from Task and DeadlineTask classes interms of their data types

>> when we are creating a class we are actually creating a data type

for instamnce from our Task we created object which would have accessed to its data and behavior with Task data type, whereas DeadlineTask would have accessed to its data and behavior with DeadlineTask data type

DeadlineTask would have all data and behavior of Task class as its being inherited by deadline class along with out data and methods related to deadline task type

in a nuttshell any methods that is accessible by task data types objects are also accessible form another data types objects its  an example of polymorphism


## comparisons with other programming paradigms
