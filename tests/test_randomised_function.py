import unittest
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    # def test_randomised_function(self):
    #     self.assertEqual('software', randomised_function())  # This will pass or fail randomly
    #     # TODO: Can we make this test deterministic? (HINT: Mock testing)



    # Taken from the solution as this is better than what I did
    @patch('lecture.is_small')  # Mock the is_small function
    def test_randomised_function_with_mock1(self, mymock_is_small):
        mymock_is_small.return_value = True
        self.assertEqual('software', randomised_function())

    @patch('lecture.is_small')  # Mock the is_small function
    def test_randomised_function_with_mock2(self, mymock_is_small):
        mymock_is_small.return_value = False
        self.assertEqual('engineering', randomised_function())

        
