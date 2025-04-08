#Import libraries
from functions import *
import unittest

class TestCase(unittest.TestCase):
    def test_prime1(self):
        self.assertTrue(is_prime(7))
        
if __name__ == "__main__":
    unittest.main()
