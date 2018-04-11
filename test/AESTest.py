import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.AES import *


class AESTest(unittest.TestCase):
    '''
    def test_multiplication(self):
        m = ['0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1']
        text =  ['0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '1']
        expected = ['1','0','0','0','0','0','1','0','0','1','0','0','0','0','1','1']
        result = multiplication(m, text)
        self.assertEqual(result,expected)
    '''
    def test_binary_dot_operation(self):
        a = ['1', '0', '1', '1']
        b =  ['1', '1', '1', '1']
        expected = ['1','1','0','1','0','0','1']
        result = binary_dot_operation(a,b)
        self.assertEqual(result,expected)

    def test_binary_division_operation(self):
        a =  [1, 1, 0, 1,0,0,1]
        b = [1, 0, 0, 1,1,0,0]
        expected = [0,0,1,1]
        result = binary_division_operation(a,b)
        self.assertEqual(result,expected)
    
    def test_binary_division_operation_2(self):
        a =  [1, 0, 1, 0, 1, 0, 1]
        b = [1, 0, 0, 1,1,0,0]
        expected = [1,0,1,0]
        result = binary_division_operation(a,b)
        self.assertEqual(result,expected)

    def test_fill(self):
        a =  [1,1,0,1]
        b = 7
        expected = [0,0,0,1,1,0,1]
        result = fill_with_zero(a,b)
        self.assertEqual(result,expected)

    def test_string_to_int(self):
        a =  [1,1,0,1]
        expected = ['1','1','0','1']
        result = int_to_string(a)
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()