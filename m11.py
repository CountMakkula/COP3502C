#Import libraries
from functions import *
import unittest

class TestCase(unittest.TestCase):
    def test_prime1(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))

    def test_prime2(self):
        self.assertFalse(is_prime(-3))

    def test_prime3(self):
        self.assertFalse(is_prime(2))

if __name__ == "__main__":
    unittest.main()
