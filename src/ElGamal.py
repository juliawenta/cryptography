import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.lucas import *
from random import randint

#method to generate primitive roots of number
def find_primitives(n):
 
    ps = fermat_algorithm_2(n-1)
    if 1 in ps:
        ps.remove(1)
    
    squares = []
    for r in range(2,n):
        flag = True
    
        for p in ps:
            # Check if r^((n-1)/p) mod n is 1 or not:
            if real_fast_exponentation_modulo(r, int((n-1)/p),n) == 1:            
            #if pow(r, int((n-1)/p)) % n == 1:
                flag = False
                  
        if flag:
            squares.append(r)
    return squares

#method to generate random k
def generate_k(n):

    return randint(1, n-1)
    
#method to generate public and private key
def generate_keys(r,k,n):
    a = real_fast_exponentation_modulo(r,k,n)
    public_key = [n,r,a]
    print("Public key: ", public_key)
    private_key = [n,r,a,k]
    print("Private key: ",private_key)
    return a

#method to make a cipher
def cipher(j,t,r,n,a):
    c_1=real_fast_exponentation_modulo(r,j,n)
    c_2a = real_fast_exponentation_modulo(a,j,n)
    c_2 = c_2a *t % n
    #c_2=t*a**j %n
    print("Cipher: (",c_1,"," ,c_2,")")