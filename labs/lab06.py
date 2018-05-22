import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ElGamal import *
from src.lucas import *

def task():
    n = int(input("Please insert n: \n"))
    if is_prime(n) == False:
        print("N is not a prime!")
    else:
        primitives = find_primitives(n)
        #print(primitives)
        r =int(input("Please insert r: \n"))
        if r not in primitives:
            print("R is not one of primitive roots of ",n, "!")
        else:
            k =int(input("Please insert k: \n"))
            a = generate_keys(r,k,n)
            j =int(input("Please insert j: \n"))
            t =int(input("Please insert t: \n"))
            cipher(j,t,r,n,a)


task()