# intro to testing

# when working with python or anby other language tehre is a lot that can go wrong with our code, such as syntax errors, exceptions and etc
# there are also mistakes in code logic which cause to behave in unexpected ways.
# for these reasons testing is crucial to create quality software, goal of testing isnt just to find bugs but to find them early and fix them
# leaving bugs unfound and unresolved can lead to massive consequences in real world

# by following some common practices and using tools built into python we can start creating quality tests in no time

# kinds of testing styles in python
# manual testing: a physical person interacts with software as a user in real world would. we have been manually testing code any time we run it and observe its behavior
# automated testing: tests are performed with code. generally automated tests are faster and more reliable than manual testing

# exercise:
flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  # print('Flight ' + flight + ' status: ' + status)
  print('Flight ' + str(flight) + ' status: ' + status)


# assert statement
# while previous example was simple to test, most code will be much more complex, it would be very tedius to have to perform these tests manually, our time will be better spent writing automated tests.

# luckily python provides an easy way to perform simple tests in our code, 'assert' statement can be used to test that a condition is met, if condition evaluates to false an assertion error will be raised wigth an optional custom message

def times_ten(number):
  return number * 10

result = times_ten(20)
assert result == 200, 'result should be 200, instead got ' + str(result)

# observations:
# here we want to test if our times_ten functions works as intended, we use assert statement to evaluate expression result === 200, if this is not the case (meaning some bugs are present), we raise an assertion error with custom message

# as assert statement is a quick and powerful way to verify that a program is in correct state, they can be used to catch mistakes early and make sure we avoid any catastrophes

# exercise:
destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
# destination = 'HND'
destination = 'BUD'


# Write your code below: 
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)


# unit testing

# assertion statements are a good start to ensure our programs are being tested but they dont necessarily tell us what we should test, generally we can start by testing smallest unit of program

# for example, in real world, if were testing functionality of a door, we could test a multitude of units, handle could be an example of a single unit that we must check to make sure door functions, followed by hinges and maybe even lock

# lets say we wanted to test a single function (a.k.a. a single unit), to test a single unit we might create several test cases. a test case validates that specific set of inputs produces an expected output for unit we are trying to test.

# unit we want to test
def times_ten(n):
  return n * 10

# a unit test function with a single test case
def test_multiply_ten_by_zero():
  assert times_ten(0) == 0, 'times_ten(0) should be 0, instead got ' + str(times_ten(0))

# now that we have a simple test case that validates that times_ten is behaving as expected for a valid input of 0, we can improve our testing coverage of this function by adding some more test cases with diffrent inputs.
# A common approach would is to create tests cases for specific edge case inputs as well as reasonable ones.
# lets tests out two extreme cases

def test_multiply_ten_by_one_million():
    assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000'

def test_multiply_ten_by_negative_number():
    assert times_ten(-10) == -1000, 'Expected times_ten(-10) to return -100'

# now we have sevaral tets cases for a wide vareity of inputs, we can create as many test cases as we see fit for a single unit, we should try to test all unique types of inputs our unit will  work with.

# exercise:
def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # location = 'middle'
    location = 'back'
  return location

# Write your code below:
def test_row_1():
  assert get_nearest_exit(1) == 'front', "Expected get_nearest_exit(1) to return 'front' but got " + get_nearest_exit(1)

def test_row_20():
  assert get_nearest_exit(20) == 'middle', "Expected get_nearest_exit(20) to return 'middle' but got " + get_nearest_exit(20)

def test_row_35():
  assert get_nearest_exit(35) == 'back', "Expected get_nearest exit(35) to return 'back' but got " + get_nearest_exit(35)

test_row_1()
test_row_20()
test_row_35()