import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.RSA import *


class AESTest(unittest.TestCase):
    
    def test_sieve(self):
        expected = [2,3]
        result = sieve(4)
        self.assertEqual(result,expected)

    def test_sieve_2(self):
        expected = [2,3,5,7,9]
        result = sieve(10)
        self.assertEqual(result,expected)
 
    def test_euclid(self):
        expected = (90,3,-25)
        result = euclid(8280,990)
        self.assertEqual(result,expected)

    def test_euclid_2(self):
        expected = (6,-7,83)
        result = euclid(1920,162)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()