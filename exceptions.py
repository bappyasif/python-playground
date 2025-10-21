# exceptions

# exercise
sale_instruments = ['Violin', 'Conga', 'Clavinet']

# print('The following ' + len(sale_instruments) + ' instruments are on sale:')
# print('The following ' + {} + ' instruments are on sale:'.format(len(sale_instruments)))
print('The following ' + str(len(sale_instruments)) + ' instruments are on sale:')
print(sale_instruments[0])
print(sale_instruments[1])
# print(sale_instruments[3])
print(sale_instruments[2])
print(TypeError.__bases__)

# raising exceptions
# encountering exceptions is not always an accident, we can throw an exception at any time by using raise keyword, even when python normally would not throw it.

# we want to raise an error anytime we think a mistake has or will occur in our program, this lets us stop program execution immediately and povide a clear error message instead of allowing mistakes to occur and may be difficult to debug at a later point of time

# one way to use `raise` keyword is to pair with a specific exception class name, we can class by itself or call a contructor and provide a specefic error message.

# raise NameError

# or

# raise NameError('NameError: name not defined, custom message')

# when only class name is provided (as in first example), python will call the class constructor with no arguments(thus no custom message is provided)

# when both class name and custom message are provided, python will call the class constructor with the custom message


# For a more concrete example, let’s examine raising a TypeError for a function that checks if an employee tries to open the cash register but does not have the correct access:
def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    # Alternatives: raise TypeError() or TypeError('Message')
    raise TypeError

# observations:
# when an employee status is not authorized, the function raises a TypeError exception, alternatively, when no builtin exceptions makes sense for type of error our program might experience, it might be better to use a generic exception with a custom message

def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    raise Exception('Employee does not have access!')
# observations:
# now we are using a generic exception with a custom message
# As a general rule of thumb, use an exception that provides the best explanation for the expected error for both the user and anyone that will read the code

# exercise:
instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  # Write your code below:
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(instrument + " is not found in instrument catalog!")
    # raise NameError(instrument + " is not found in instrument catalog!")
#   if instrument not in instrument_catalog:
#     raise NameError('Instrument not found')
#   else:
#     print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))


print_instrument_price('Marimba')
print_instrument_price('Flute')
# print_instrument_price('Piano')


# try / except
# so far exceptions we've encountered caused our programs to stop executing. however its possible for programs to continue executing even after encountering an exception. this is known as exceptions handling and is accomplished using python try / except block

# start => Execute try calause code
# except => Execute except clause code
# else => Execute else clause code
# finally => Execute finally clause code
# end => Execute end clause code

# python will first attempt to execute code inside try clause code block
# if no exception is encountered in code, exception clause is skipped and program execution continues to next execution block

# if an exception does occur inside of try block, python will immediately execute the code in the except block, sometimes called a catch block or a handler

# finally block is executed whether or not an exception is encountered

colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}

for color in ('red', 'green', 'yellow'):
  try:
    print('The hex value of ' + color + ' is ' + colors[color])
  except:
    print('An exception occurred! Color does not exist.')
  print('Loop continues...')

# colors = ["red", "blue", "yellow"]
for color in colors:
  try:
    print("Hex value: " + colors[color])
  except:
    print("An exception occurred! Color does not exist.")
  print("Loop continues...")

# observations:
# in above code try block runs until it hit an exception
# when exception is hit, code in except block is executed
# however exceptions was handled so python continues to next execution block

# exceptions handling is a powerful tool that lets us gain more flexibility in dealing with errors in our applications
# we can use it multiple times to handle different types of errors or until it 

# excercise:
staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Write your code below:
  try:
    print_staff_report(location, staff)
  except:
    print(f"An exception occurred! Location: {location} does not exist.")
  # print_staff_report(location, staff)


# catching specific exceptions:
# exception handlers from previous exercise handled any exception hit during try clause
# however in most cases we will have an idea exception that we want to handle specifically within our program
# it is generally a good idea to use specific exception handlers for specific exceptions
# we can achieve this by using except keyword followed by exception class name

try:
  print(1 / 0)
except ZeroDivisionError:
  print('Cannot divide by zero!')

# observations:
# in above code we are catching ZeroDivisionError exception and printing custom message

try:
  print(undefined_variable)
except NameError:
  print('Variable does not exist!')

# observations:
# in above code we are catching NameError exception and printing custom message

# when we specify exception class name, python will only execute code in except block if an exception of that type is encountered, python allows us to use AS keyword to assign the exception object to a variable

try:
  print(unknown_variable)
except NameError as err:
  print('Variable does not exist!')
  print(err, "!!")

# exercise
staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  # Write your code below:
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location)
      print(e)
