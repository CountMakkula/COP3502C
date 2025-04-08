#Import libraries
from functions import *
import unittest

class TestCase1(unittest.TestCase):
    def TestPrime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(-3))
        
