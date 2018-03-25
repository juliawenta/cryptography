import unittest

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.SDES import *


class SDESTest(unittest.TestCase):
    
    def test_generate_permutation(self):
        key = ['1','0','1','0']
        permutation = ['3','1','0','2']
        expected = ['0','0','1','1']
        result = generate_permutation(key,permutation)
        self.assertEqual(result,expected)

    def test_generate_permutation_4in8(self):
        key = ['1','0','0','0']
        permutation = ['3', '0', '1', '2', '1', '2', '3', '0']
        expected = ['0', '1', '0', '0', '0', '0', '0', '1']
        result = generate_permutation(key,permutation)
        self.assertEqual(result,expected)

    def test_generate_permutation_10in8(self):
        key = ['0','1','0','0','0','1','1','0','0','1']
        permutation = ['5','2','6','3','7','4','9','8']
        expected = ['1','0','1','0','0','0','1','0']
        result = generate_permutation(key,permutation)
        self.assertEqual(result,expected)


    def test_generate_permutation_sl1(self):
        key = ['1','2','3','4']
        expected = ['2','3','4','1']
        result = generate_permutation_sl1(key)
        self.assertEqual(result,expected)

    def test_generate_permutation_sl2(self):
        key = ['1','2','3','4']
        expected = ['3','4','1','2']
        result = generate_permutation_sl2(key)
        self.assertEqual(result,expected)

    def test_bitwise_or(self):
        xs = ['1','0','1','0']
        ys = ['0','1','1','0']
        expected = ['1','1','0','0']
        result = bitwise_or(xs,ys)
        self.assertEqual(result,expected)

    def test_get_dicemal(self):
        x = 1
        y = 0
        expected = 2
        result = get_decimal(x,y)
        self.assertEqual(result,expected)

    def test_sbox1(self):
        bits = ['1', '1', '1', '0']
        expected = ['1','1']
        result = sbox1(bits)
        self.assertEqual(result,expected)

    def test_sbox2(self):
        bits = ['0', '0', '1', '1']
        expected = ['0','0']
        result = sbox2(bits)
        self.assertEqual(result,expected)

    def test_generate_keys(self):
        keys = generate_keys()
        expected = (['1', '0', '1', '0','0', '0', '1', '0'], ['0', '0', '0', '0', '1', '1', '1', '1'])
        self.assertEqual(keys,expected)


if __name__ == '__main__':
    unittest.main()