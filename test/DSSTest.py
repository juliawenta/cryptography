import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.DSS import *


class AESTest(unittest.TestCase):
    
    def test_count_vowels(self):
        expected = 174
        result = count_vowels()
        self.assertEqual(result,expected)

    def test_count_consonants(self):
        expected = 299
        result = count_consonants()
        self.assertEqual(result,expected)
    
    def test_count_spaces(self):
        expected = 114
        result = count_spaces()
        self.assertEqual(result,expected)
    


if __name__ == '__main__':
    unittest.main()