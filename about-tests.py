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
    return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']


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


unittest.main()