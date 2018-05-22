import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ElGamal import *


class AESTest(unittest.TestCase):
    
    def test_find_primitives(self):
        x=257
        expected = 3
        result = find_primitives(x)
        self.assertEqual(result,expected)
    
    def test_find_primitives(self):
        x=827
        expected = 2
        result = find_primitives(x)
        self.assertEqual(result,expected)
    

if __name__ == '__main__':
    unittest.main()