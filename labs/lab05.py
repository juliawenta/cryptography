import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.RSA import *


def task1():

    number = int(input("Insert index of prime number you would like to see: \n"))
    primes = sieve(number*16)
    print (primes[number-1])
    return primes






task1()