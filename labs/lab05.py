import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.RSA import *


def task1():
    print("Ex 1: ")
    number = int(input("Insert index of prime number you would like to see: \n"))
    primes = sieve(number*16)
    print ("\t Result: ",primes[number-1],"\n")
    return primes

def task2():
    print("Ex 2: ")
    a = int(input("Insert a please: \n"))
    b = int(input("And enter b: \n"))
    result = euclid(a,b)
    return result




task1()
print("\n")
task2()