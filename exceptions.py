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


# multiple exceptions:
# whiel handling a single exception is useful, python also allows us to handle multiple exceptions at once.
# we can list more than one exception class name in except clause, python will execute code in except block if an exception of any of the listed exception classes is encountered

try:
  print(undefined_variable)
  print(1 / 0)
except (NameError, ZeroDivisionError):
  print('An exception occurred!')

# observations:
# in above code we are catching NameError and ZeroDivisionError exceptions and printing custom message
# in above code we expect to encounter either NameError or ZeroDivisionError exception, we can list any muber of exceptions class as long as it make sense for try block
# this is where we can use 'as' clause since it allows us print or operate on specific exception that is caught
# in addition to catching multiple exceptions, we can also pair multiple 'except' clauses witha single 'try' clause, enabling us to handle specific exceptions in different ways

try:
  print(1/0, undefined_variable)
  print(1 / 0)
except NameError:
  print('NameError occurred!')
except ZeroDivisionError:
  print('ZeroDivisionError occurred!')
except TypeError:
  print('TypeError occurred!')
except Exception:
  print('An exception occurred! we hit an exception that is not name or zero division error or type error')

# observations:
# in above code will trigger exception that is not name or zero division error or type error, if not handled by those exception handlers, it will trigger a generic exception
# python will execute first one of the exception handlers that matches the exception that is encountered
# in this case and a valid startegy for exception handling, we use last 'except' as a generic exception handler if no other exception handlers match the exception that is encountered

# excercise:
instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Clarinet'
discount = '20'

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('Instrument not found')
except TypeError:
  print('Discount must be a number')
except:
  print('An exception occurred that is not KeyError or TypeError!')


# else clause:
# sometimes we want to execute code only if no exception is encountered
# we can use else clause to execute code only if no exception is encountered

x = 1
try:
  x = 1/0
except ZeroDivisionError:
  print('A zero division error occurred!')
else:
  x += 1
print(x)

# we've seen how exception handlers get executed when we encounter exceptions during a try clause but what if we want to execute code only if no exception is encountered?

def check_password():
  # raise ValueError('Password is incorrect!')
  pass

def login_user():
  print('User logged in!')
  pass

try:
  check_password()
except ValueError:
  print('Value error occurred!')
else:
  print('Password is correct!')
  login_user()


# we could also argue, that we could have executed else block code in try block to achieve the same result
try:
  check_password()
  login_user()
  # 20 other lines of imaginary code
except ValueError:
  print('Wrong Password! Try again!')

# python offers a bit of insight on this matter, use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except

# this aforementioned suggestion is valid in this case since alternatively value error could have occured in any of the other lines of code that is not detected in check_password function, and it would be challenging for us to tell where that came from.

# exercise:
customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Write your code below:
  try:
    rewards_number = customer_rewards[customer] 
  except KeyError:
    print('Customer not found')
  else:
    print('Rewards account number is: ' + str(rewards_number))


# customer = 'Zuigly'
customer = 'Guadalupe'
display_rewards_account(customer)

# finally clause
# finally clause is useful when we want to execute some code regardless if an exception is encountered or not

def load_footer():
  print('Footer loaded!')

try:
  check_password()
except ValueError:
  print('Wrong Password! Try again!')
else:
  login_user()
  # 20 other lines of imaginary code
finally:
  load_footer()

# observations:
# in above code we are loading footer regardless if an exception is encountered or not

# also be noted that finally clause can be used independently of exception handling or else block, this is convenient when we want to execute some code regardless if an exception is encountered or not

try:
  check_password()
finally:
  load_footer()
  # 20 other lines of imaginary code

# exercise:
# import database  # if we had to import it from another filoe named database.py, which i have hardcoded it in here for convenience
instruments = {
    'Kora': {
        'Family': 'Strings',
        'Origin': 'West Africa',
    },
    'Didgeridoo': {
        'Family': 'Wind',
        'Origin': 'Northern Australia',
    },
    'Guitar': {
        'Family': 'Strings',
        'Origin': 'Spain',
    }
}

def connect_to_database():
    print('Establishing connection to instrument database server...')

def disconnect_from_database():
    print('Destroying connection to instrument database server...')

def get_instrument_info(instrument):
    return instruments[instrument]

def display_instrument_info(instrument):
    info = get_instrument_info(instrument)
    print('Instrument: ' + instrument)
    print('Family: ' + info['Family'])
    print('Origin: ' + info['Origin'])

# instrument = 'Synthesizer'
instrument = 'Didgeridoo'
# database.connect_to_database()
connect_to_database()

try:
  # database.display_instrument_info(instrument)
  display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
# Write your code below: 
finally:
  # database.disconnect_from_database()
  disconnect_from_database()


# user defined exceptions:
# so far we've seen how to raise and manage built in exceptions, in most programs using builtin exceptions wont always be most detailed way to describe an error occuring
# what if we could create custom exceptions that are more specific to a program or module.
# python gives us ability to create user defined exceptions.

# user defined exceptions are exceptions that we create to allow for better readability in our program's errors

# custom exceptions are created by inheriting from the Exception class

class CustomError(Exception):
  pass

# observations:
# in above code we are creating a custom exception called CustomError, it inherits from Exception class
# now we can raise CustomError just like any other exception
# although not required, most custom exceptions end in Error similar to naming of built-in exceptions.

# first lets see how these custom exceptions helps us better document our errors

# lets imagine Intrument world has an optional delivery service for instruments, if someone tries to schedule a delivery but their address is too far, we want to raise a custom LocationTooFarAway exception, this is a custom exception that inherits from Exception class
class LocationTooFarError(Exception):
   pass

def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError
    else:
        print('Scheduling the delivery...')

# Write your code below:
try:
  schedule_delivery(10)
except LocationTooFarError:
  print('Location too far!')

# observations:
# in above code we are catching LocationTooFarError exception and printing custom message

# excercise:
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

#Write your code below (Checkpoint 2):
class InventoryError(Exception):
  pass

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  # Write your code below (Checkpoint 3 & 4): 
  if quantity > supply:
    raise InventoryError
  else:  
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 1
submit_order(instrument, quantity)


# customizing user defined exceptions:
# we've seen how defining a simple exception class can provide a more specific use useful error to users
# defining a simple class is just first step to create better exceptions in our programs, python does not stop us from customizing our custom exception classes even further

# lets say we wanted to expand our LocationTooFarError from earlier to also provide a custom error message

class LocationTooFarErr(Exception):
  def __init__(self, distance):
    self.distance = distance

  def __str__(self):
    return 'Location too far, not within delivery range of 10 miles! Distance: ' + str(self.distance)

# observations:
# in above code we are using __init__ method to provide custom message to user

# we can also use __str__ method to provide custom message string and return to user

def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarErr(distance_from_store)
    else:
        print('Scheduling the delivery...')

schedule_delivery(10)
# observations:
# in above code we are catching LocationTooFarErr exception and printing custom message

# exercise:
# Write your code below (Checkpoint 1 & 2)
class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply

  def __str__(self):
    return "Available supply is only "+str(self.supply)

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  # Write your code below (Checkpoint 3)
  if quantity > supply:
    raise InventoryError(supply)
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 2
submit_order(instrument, quantity)

# observations:
# in above code we are catching InventoryError exception and printing custom message

# excercise:
instrument_families = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

def print_instrument_families():
  for family in ['Strings', 'Percussion', 'woodwinds']:
    # print('Some instruments in the ' family + 'family are: ' + instrument_families[family]) # some errors here
    print('Some instruments in the ' + family + 'family are: ' + str(instrument_families[family]))

print_instrument_families()