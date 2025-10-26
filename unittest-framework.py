# python's unittest framework

# there are some problems with our previous unit test approach, that would make them difficult to maintain, as we had to call each fucntional specifically when a new tst is created, so we had no way of grouping them together, which is necesary when number of tests increases, perhaps most importantly if one test fails assertion error would prevent any remaining tests from running.

# luckily python provides a framework that solves these problemsand provides many other tools for writing unit tests, this framework is called unittest and is built on top of python's standard library and included in python's standard library.

import unittest

# class TetstTimesTen(unittest.TestCase): 
#     pass

# this class will serve as main storage of all our unit testing functions
# once we have class, we need to change our test functions so that they are methods of this class
# unittest module requires taht test functions begin with word 'test'

def times_ten(n):
    return n * 10

class TestrTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        # assert times_ten(0) == 0, 'times_ten(0) should be 0, instead got ' + str(times_ten(0))
        self.assertEqual(times_ten(0), 0, 'times_ten(0) should be 0, instead got ' + str(times_ten(0)))


    def test_multiply_ten_by_one_million(self):
        # assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000 but got ' + str(times_ten(1000000)) + " instead!"
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000 but got ' + str(times_ten(1000000)) + " instead!")



    def test_multiply_ten_by_negative_number(self):
        # assert times_ten(-10) == -1000, 'Expected times_ten(-10) to return -100 but got ' + str(times_ten(-10))
        self.assertEqual(times_ten(-10), -100, 'Expected times_ten(-10) to return -100 but got ' + str(times_ten(-10)))

    # now we can run our tests by calling unittest.main(), framework will workout which tests to run and run them and report results

# unittest.main()

# observarions:
# in above test we have 3 test functions, and report that 3 tests were run and 2 passed and 1 failed

# exercise:

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
class NearestExitTest(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual( get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
  def test_row_20(self):
    self.assertEqual( get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
  def test_row_40(self):
    self.assertEqual( get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


# unittest.main()



# Assert Methods I: equality and membership

# we saw how to check for equality between two values in unittest framework using assertEqual method of TestCase class
# framework relies on built in assert methods iunstead of assert statements to track results without acrtually raising any exceptions
# specific assert methods take arguments instead of a condition, and like assert statements they can take an optional custom message as an argument

# assert types:
 # assertEqual: assertEqual(value1, value2, '') method takes two values and an optional custom message as arguments, this method checks if value 1 is equal to value 2 and raises assertion error if they are not equal
    
 # assertIn: assertIn(value, container, '') method takes in two arguments, first one is value to check and second one is container, this method checks if value is in container and raises assertion error if it is not in container.
    
 # assertTrue: assertTrue(value, '') method checks if value is True and raises assertion error if it is not

# assert methods:

# assertEqual(a, b) a == b 

# assertNotEqual(a, b) a != b 

# assertTrue(x) bool(x) is True 

# assertFalse(x) bool(x) is False

# assertIs(a, b) a is b 

# assertIsNot(a, b) a is not b 

# assertIsNone(x) x is None 

# assertIsNotNone(x) x is not None 

# assertIn(a, b) a in b 

# assertNotIn(a, b) a not in b 

# assertIsInstance(a, b) isinstance(a, b)

# assertNotIsInstance(a, b) not isinstance(a, b)

# assertIsSubclass(a, b) issubclass(a, b) 

# assertNotIsSubclass(a, b) not issubclass(a, b)

# exercise:
import unittest
def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'


def get_licensed_movies():
    print('Retrieving the list of licensed movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is inactive')
    return False

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = get_daily_movie()
    licensed_movies = get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies, 'The daily movie is not in the list of licensed movies!')

  def test_wifi_status(self):
    wifi_enabled = get_wifi_status()
    self.assertTrue(wifi_enabled, 'WiFi is not enabled!')


# unittest.main()


# Assert method II: quantitative methods

# once we need to test conditions related to numbers, unittest module provides a handful of assert methods to achieve this
# lets take a look at two common assert methods related to quantitative comparisons, their general syntax and their equivalent assert statements

# assertLess: assertLess(value1, value2, '') method takes two numbers and an optional custom message as arguments, this method checks if value 1 is less than value 2 and raises assertion error if they are not less than each other.

# assertAlmostEqual: assertAlmostEqual(val1, val2, '') method takes two numbers and an optional custom message as arguments, this method checks if value 1 is close to value 2 and raises assertion error if they are not close to each other. its basically checks their difference when rounded to 7 decimal places is 0

# all methods:
# assertAlmostEqual(a, b) round(a-b, 7) == 0

# assertNotAlmostEqual(a, b) round(a-b, 7) != 0

# assertGreater(a, b) a > b

# assertGreaterEqual(a, b) a >= b

# assertLess(a, b) a < b

# assertLessEqual(a, b) a <= b

# assertRegex(s, r) r.search(s)

# assertNotRegex(s, r) not r.search(s)

# assertCountEqual(a, b) a and b have the same elements in the same number, regardless of their order.

# assertStartsWith(a, b) a.startswith(b)

# assertNotStartsWith(a, b) not a.startswith(b)

# assertEndsWith(a, b) a.endswith(b)

# assertNotEndsWith(a, b) not a.endswith(b)

# assertHasAttr(a, b) hastattr(a, b)

# assertNotHasAttr(a, b) not hastattr(a, b)

# exercise:

def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40

def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.9999999999999

# Write your code below:

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = get_daily_movie()
    licensed_movies = get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Write your code below:
  def test_maximum_display_brightness(self):
     brightness = get_maximum_display_brightness()
     self.assertAlmostEqual(brightness, 400)
  
  def test_device_temp(self):
     temp = get_device_temp()
     self.assertLess(temp, 50)

# unittest.main()



# Assert Methods III: exceptions and warning methods
# there is another group of assert methods that can be used to test for exceptions and warnings

# assertRaises: assertRaises() methods takes an exception type as first argument, a function reference as its second and an arbitary number of arguments as rest. it calls functions and checks if an exception is raised as a result, test passes if an exception is raised and is an error if another exception is raised or no exception is raised, this method can be sed with custom exceptions as well (e.g. assertException(Exception, function, *args))

# assertWarns: assertWarns() methods takes a warning type as its first argument, a function reference as its second and an arbitary amount of arguments as rest. it calls function and checks that warning occurs, test passes if warning is raised  and fails if it isnt (e.g. assertWarns(SpecieficWarningException, function, *args))

# there are no particular concise ways to replicate these tests using assert keyword, it recommended to use these methods instead when possible

# all methods:
# assertRaises(exc, fun, *args, **kwds) fun(*args, **kwds) raises exc

# assertRaisesRegex(exc, r, fun, *args, **kwds) fun(*args, **kwds) raises exc and the message matches regex r

# assertWarns(warn, fun, *args, **kwds) fun(*args, **kwds) raises warn

# assertWarnsRegex(warn, r, fun, *args, **kwds) fun(*args, **kwds) raises warn and the message matches regex r

# assertLogs(logger, level) The with block logs on logger with minimum level

# assertNoLogs(logger, level) The with block does not log on logger with minimum level

# exercise:
import warnings

class PowerError(Exception):
    pass

class WaterLevelWarning(Warning):
    pass

def power_outage_detected(outage_detected):
    if outage_detected:
        raise PowerError('A power outage has been detected somewhere in the system')
    else:
        print('All systems receiving power')

def water_levels_check(liters):
    if liters < 200:
        warnings.warn('Water levels have fallen below 200 liters', WaterLevelWarning)
    else:
        print('Water levels are adequate')


class SystemAlertTests(unittest.TestCase):
   def test_power_outage_detected(self):
    self.assertRaises(PowerError, power_outage_detected, True)

   def test_water_levels_check(self):
    self.assertWarns(WaterLevelWarning, water_levels_check, 100)


unittest.main()