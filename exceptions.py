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
print_instrument_price('Piano')
