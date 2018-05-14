import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ElGamal import *


class AESTest(unittest.TestCase):
    
    def test_name(self):
        x=1
        expected = 1
        result = name(x)
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()