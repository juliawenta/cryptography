import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.RSA import *


class AESTest(unittest.TestCase):
    
    def test_name(self):
        result = name()
        self.assertEqual(result,expected)
 


if __name__ == '__main__':
    unittest.main()