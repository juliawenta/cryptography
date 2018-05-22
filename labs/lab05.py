import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.RSA import *
from src.lucas import *

def task1():
    print("Ex 1: ")
    number = int(input("Insert index of prime number you would like to see: \n"))
    primes = sieve(number*16)
    print ("\t Result: ",primes[number-1],"\n")
    number2 = int(input("Insert index of prime number you would like to see: \n"))
    primes2 = sieve(number2*16)
    print ("\t Result: ",primes2[number2-1],"\n")
    return primes

def task2():
    print("Ex 2: ")
    a = int(input("Insert a please: \n"))
    b = int(input("And enter b: \n"))
    result = euclid(a,b)
    return result

def task3():
    print("Ex 3: ")
    i = int(input("Enter i: \n"))
    i1 = sieve(i*16)
    j = int(input("Enter j: \n"))
    j1 = sieve(j*16)
    
    p = i1[i-1]
    q = j1[j-1]
    print("p: ",p) 
    print("q: ",q) 

    n = p*q
    m = (p-1)*(q-1)
    print("n: ",n) 
    print("m: ",m)
    
    e = int(input("Enter e: \n"))
    euc = euclid(e,m)
    #print("euc: ",euc)

    x=euc[1]
    print("x: ",x)
    
    if x>0:
        d=x
    elif x <=0:
        d= modular_inverse(e, m)
    print("d: ",d)

    key_public = (n,e)
    key_private = (n,d)

    print("key_public: ",key_public)
    print("key_private: ",key_private)

    t = 21969
    s = fast_exponentation_modulo_2(t,e,n)
    print("s",s)

    t = fast_exponentation_modulo_2(s,d,n)
    print("t",t)

    return t,s



task1()
print("\n")
task2()
print("\n")
task3()