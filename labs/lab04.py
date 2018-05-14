import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.lucas import *

def task1():
   result = fast_exponentation_modulo()
   print("\n")
   return result

def task2():
    print("\t Insert a number please:")
    number = input()
    result = fermat_algorithm(int(number))
    print("\n")
    return result

def task3():
    print("\t Insert n please:")
    n = int(input())
    print("\t Insert q please:")
    q = int(input())
    result = lucas_test(n,q)
    if result:
        print("The number is prime!")
    else:
        print("The test does not determine if the", n , "is prime.")

    return result

task1()
task2()
task3()