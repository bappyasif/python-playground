# parameterizing tests:
# in previous examples we created test cases for times_ten() with various inputs, however actual logic of our tests didnt really changed! to decrease repitition python provides a specific toolset for tests with only minor differences, this is known as test parameterization.
# by parameterizing tests we can leverage functionality of a single test to get a large amount of coverage of different inputs.
# to accomplish this unittest framework provides us with subTest context manager

import unittest

# function we want to test
def times_ten(n):
    return n * 10

# test class
class TestTimesTen(unittest.TestCase):

    # test method
    def test_times_ten(self):
        for n in [0, 1000000, -10]:
            with self.subTest(n):
                expected_result = n * 10
                message = 'expected times_ten('+str(n)+') to return '+str(expected_result)
                self.assertEqual(times_ten(n), expected_result, message)


# observations:
# here in our test method test_times_ten() instead of writing individual test cases for each input of 0, 10 and 1000000 we can test a collection of inputs by using a loop followed by a 'with' statement and our subTest context manager

# by using subTest each iteration of our loop is treated as individual test, python will run run code inside of context manager on each iteration and if one fails it will return failure as a separate test case failure.

# just like before we are using assertEqual() method to check expected result and we are expecting (due to an error in times_ten()) that cases of using an input of -10 and 100000 wil fail.

# if we want to expand our test coverage, we can simply modify list of inputs to iterate over for our for loop, we can test a range of iputs simply by using context manager setup to achieve test parameterization

# optionally we can give our subsets better readbility by giving making a small change in our code for first argument of self.subTest()

# when working with large amounts of test inputs, its much easier to distinguish which case failed. we can acually use any message we want as first argument but using tested case is usually best way to increase readability for ourselves and other developers

# by using test parameterization we made our codebase more robust and easier to maintain

# run tests
# unittest.main()

# exercise: 
def get_daily_movies():
    print('Retrieving the movie set to play on today\'s flight...')
    # return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']
    return ['Parasite', 'Nomadland', 'Roma']


def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


class EntertainmentSystemTest(unittest.TestCase):

    def test_movie_license(self):
        daily_movies = get_daily_movies()
        licensed_movies = get_licensed_movies()

        for movie in daily_movies:
            with self.subTest(movie):
                self.assertIn(movie, licensed_movies)


# unittest.main()

# test fixures:
# one of most important principles of testing is that tests need to occur in a known state. if conditions in which a test runs are not controlled then our tests results could contain false negatives (invalid failed results) or false positives (invalid passed results), this is where test fixtures come in.

# a test fixture is a collection of objects that are created and destroyed during the execution of a test. test fixures guarantees that our tests are running in predictable conditions and thus results are reliable

# lets say we're testing a bluetooh device, bluetooth module can sometimes fail, when this happens device needs to be power cycle (turn off and turn on) to restore bluetooth functioality. we would not want to run our test if bluetooth module fails, because these results wont be valid, we would want to run our test only if bluetooth module works. furthermore if our tests cause bluetooth module to fail we want to restore it to a working state after running tests. so we add a test fixure to power cycle device before and after each test

def power_cycle_device():
    print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):

    def setup(self):
        power_cycle_device()

    def test_feature_1(self):
        print("Testing feature 1")

    def test_feature_2(self):
        print("Testing feature 2")

    def tearDown(self):
        power_cycle_device()

# unittest.main()

# observations:
# unittest framework automatically identifies setup and teardown methods based on their names, a method name 'setup' runs before each test and a method name 'tearDown' runs after each test

# niow we can gurantee that our bluetoo module is in a working state before each test and that it is restored to a working state after each test


# lets consider another scenario, perhaps our tests reply on working bluetooth but there is nothing in tests taht would cause bluertooth device ti fail, in that case it would be ineffecient to power cycle device before and after each test
# let refactor above exmaple sio that setup and teardown gets to run just once instead of for eachtest cases

class BluetoothDeeviceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        power_cycle_device()

    def test_feature_a(self):
        print("Testing feature a")

    def test_feature_b(self):
        print("Testing feature b")

    @classmethod
    def tearDownClass(cls):
        power_cycle_device()

unittest.main()

# observations:
# we replaced our setup method with setUpClass method and added @classMethod decorator, changed argument from self cls becuase of class method
# we also removed tearDown method and replaced with tearDownClass method


# in addition to functions we can also use setup methods to instantiate objects and or gather any otehr data needed, anything stored in our class will be available throughout out test functions
# generally its a good practice to create fixtures that run for every test, however if a fixure has large operating cost then it might make more sense to have it run once per test class rather than once per test

# exercise:

def power_on_kiosk():
    print('Powering on the check-in kiosk...')


def return_to_welcome_page():
    print('Returning check-in kiosk to Welcome Page')


def power_off_kiosk():
    print('Powering off the check-in kiosk...')

class CheckInKioskTests(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    power_on_kiosk()


  def setUp(self):
    return_to_welcome_page()

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def tearDownClass(cls):
    power_off_kiosk()

# unittest.main()

# skipping tests
# sometimes we have tests that should only run in a particular context, for example we might have a group of tests that only runs on windows operating system but not linux or macOS, fo rsituations like these its useful to skip tests

# unittest framework provides two different ways to skip tests, `@unittest` decorator and `skipTest` method

# skip decorator:
# there are two decorator options to accomplish goal of skipping a test 

import sys

class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("linux"), "Only runs on Linux!!")
    def test_linux_feature(self):
        print("Testing a linux feature!!!!")

    @unittest.skipIf(not sys.platform.startswith("linux"), "Linux Only!!")
    def test_other_linux_feature(self):
        print("Testing other linux feature!!!!")

# unittest.main()

# observations:
# skipUnless option skips test if condition evaluates to false
# skipIf option skips test if condition evaluates to true

# both share common requirements, firstly both of these skip decorators are prefaced with @unittest to denote decorator pattern.
# both take a condition as first argument and folowed by a string message as second

# in above example both decorators achieve same goal: skipping if os is not linux



# second way to skip tests is to call skipTest method of TestCase class

class LinuxTests(unittest.TestCase):

    print(sys.platform, "platform!!")

    def test_linux_feature(self):
        if not sys.platform.startswith("m"):
            self.skipTest("Test only on liunux!!")
        # print("Testing a linux feature!!!!")

    def test_other_linux_feature(self):
        if not sys.platform.startswith("m"):
            self.skipTest("Test only on liunux!!")
        # print("Testing other linux feature!!!!")


# unittest.main()

# observations:
# here we call skipTest method from within test function itself, it takes a single string message as its argument and always causes test to be skipped when called

# skip decorators are slightly more convenient and make it more readble to see under what condition tests are skipped
# when conditions for skipping a test are complex to pass into a skip decorator then skipTest method is recommended alternative

# exercise:
def regional_jet():
    print('This is a regional jet...')
    return True

def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'


def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is active')
    return True

def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 33.2

def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999

class EntertainmentSystemTests(unittest.TestCase):
    @unittest.skipIf(regional_jet(), "Not available on regional jets")
    def test_movie_license(self):
        licensed_movies = get_licensed_movies()
        daily_movies = get_daily_movies()
        self.assertIn(daily_movies, licensed_movies)

    @unittest.skipUnless(regional_jet(), "Not available on regional jets")
    def test_wifi_status(self):
        wifi_enabled = get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temp(self):
        if not regional_jet():
            self.skipTest("Not available on regional jets")
        device_temp = get_device_temp()
        self.assertLess(device_temp, 35)

    def test_maximum_display_brightness(self):
        if not regional_jet():
            self.skipTest("Not available on regional jets")
        brightness = get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)

unittest.main()
