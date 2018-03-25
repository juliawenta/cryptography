import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.vigenereCipher import *
from src.io_module import *

project_path = os.path.abspath(os.path.dirname(__file__))


def task1():
    path = os.path.join(project_path, "../resources/tekst_Vigenere2.txt")
    text = readFile(path)
    cipher = encrypt(text,'yes')
    result_path = os.path.join(project_path, "../resources/result.txt")
    saveFile(result_path,cipher)
    print ('Text saved to file.')

#column_size can be changed by user

def task2():
    path = os.path.join(project_path, "../resources/result.txt")
    text = readFile(path)
    column_size = 3;
    text_matrix = create_text_matrix(text, column_size)
    for i in range(0,column_size):
        ic = get_coincidence_index(text_matrix[i])
        print('Column '+str(i))
        print(ic)

def task3():
    path = os.path.join(project_path, "../resources/result.txt")
    text = readFile(path)    
    column_size = 5;
    text_matrix = create_text_matrix(text, column_size)
    next = 1
    for ci in range(0,column_size-1):
        for ci2 in range(next, column_size):
           if ci != ci2: # Statement made to not print the same columns ex: 1 and 1 
               mci = get_mutual_coincidence_index(text_matrix[ci],text_matrix[ci2])
               print('Mutual conicidence index for columns  '+str(ci)+' '+str(ci2))
               print(mci)

task1()
task2()
task3()