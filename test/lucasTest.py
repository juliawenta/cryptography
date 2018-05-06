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
        print("cos")
        result = power_modulo(rev_binary,a,modulo)
        self.assertEqual(result,expected)
        
    def test_found_d(self):
        res = 5148
        expected = 1287
        result = found_d(res)
        self.assertEqual(result,expected)


    def test_check_d(self):
        res = 39
        expected = 7
        result = check_d(res)
        self.assertEqual(result,expected)

    def test_find_dividers(self):
        d = 39
        y = 7
        expected = (8,5)
        result = find_dividers(d,y)
        self.assertEqual(result,expected)


    def test_find_primes(self):
        d = 39
        y = 7
        primers = []
        expected = [3,13]
        result = find_primes(d,y,primers)
        self.assertEqual(result,expected)

    def test_find_primes_2(self):
        d = 1287
        y = 36
        primers = []
        expected = [3,11,3,13]
        result = find_primes(d,y,primers)
        self.assertEqual(result,expected)

    def test_fermat_algorithm(self):
        number = 5148
        expected = [3,11,3,13,2,2]
        result = fermat_algorithm(number)
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()