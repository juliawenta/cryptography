import unittest

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.vigenereCipher import *
from src.io_module import *

project_path = os.path.abspath(os.path.dirname(__file__))


class VigenereCipherTest(unittest.TestCase):
    
    def test_get_indexed_key_simple_key(self):
        self.assertEqual(get_indexed_string('abc'),[0, 1, 2])
 
    def test_get_indexed_key_complex_key(self):
        self.assertEqual(get_indexed_string('politechnika'),[15, 14, 11, 8, 19, 4, 2, 7, 13, 8, 10, 0])
                
    def test_if_parse_numbers_parse_simple(self):
        self.assertEqual(parse_numbers([1,2,3]),'bcd')
    
    def test_if_encrypt_return_cryptogram_simple(self):
        self.assertEqual(encrypt('bc', 'de'),'eg')
    
    def test_if_encrypt_return_cryptogram_complex(self):
        self.assertEqual(encrypt('krypto', 'abc'),'ksapuq')

    def test_count_letters(self):
        self.assertEqual(count_letters('kotek','k'),2)

    def test_get_coincidence_index_simple(self):
        self.assertEqual(get_coincidence_index('aaa'),1)
   
    def test_get_coincidence_index_complex(self):
        self.assertEqual(get_coincidence_index('kotek'),0.1)
    
    def test_get_coincidence_index_alphabet(self):
        path = os.path.join(project_path, "../resources/text.txt")
        text = readFile(path)
        ci = get_coincidence_index(text)
        res = False    
        if ci > 0.064 and ci < 0.069:
            res = True     
        self.assertEqual(res,True)
    
    def test_create_text_matrix_two_column(self):
        matrix = [['p','l','n'],['o','a','d']]
        self.assertEqual(create_text_matrix('poland', 2), matrix)
    
    def test_create_text_matrix_two_column_not_equal(self):
        matrix = [['h','l','n'],['o','a','d']]
        self.assertNotEqual(create_text_matrix('poland', 2), matrix)
    
    def test_if_coincidence_index_for_column_size(self):
        path = os.path.join(project_path, "../resources/text.txt")
        text = readFile(path)
        self.assertEqual(if_coincidence_index_for_column_size(text, 1),True)

if __name__ == '__main__':
    unittest.main()