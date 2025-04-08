#Import libraries
from functions import *
import unittest

class TestCase(unittest.TestCase):
    def prime1(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))

    def prime2(self):
        self.assertFalse(is_prime(-3))

    def prime3(self):
        self.assertFalse(is_prime(2))
