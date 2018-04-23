import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.lucas import *


class AESTest(unittest.TestCase):
    
    def test_power_modulo(self):
        rev_binary = [1,0,1,0,1]
        a = 4
        modulo = 7
        expected = 1
        result = power_modulo(rev_binary,a,modulo)
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()