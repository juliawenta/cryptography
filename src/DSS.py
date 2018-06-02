import unittest
import sys
import os.path
import hashlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.lucas import *
from resources import *
from src.io_module import *
from src.RSA import *
from src.ElGamal import *

project_path = os.path.abspath(os.path.dirname(__file__))


def count_vowels(name):
    #path = os.path.join(project_path, "../resources/long_text.txt")
    path = os.path.join(project_path, name)
    string = readFile(path)
    vowels = 0
    for s in string:
          if(s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U'):
                vowels = vowels + 1
    print("Number of vowels: ",vowels)
    return vowels

def count_consonants(name):
    path = os.path.join(project_path, name)
    string = readFile(path)
    consonants = 0
    for i in string:
            if(i=='b' or i=='c' or i=='d' or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l' or i=='m' or i=='n' or i=='p' or i=='q' or i=='r' or i=='s' or i=='t' or i=='v' or i=='x' or i=='y' or i=='z' or i=='w' or i=='B' or i=='C' or i=='D' or i=='F' or i=='G' or i=='H' or i=='J' or i=='K' or i=='L' or i=='M' or i=='N' or i=='P' or i=='Q' or i=='R' or i=='S' or i=='T' or i=='V' or i=='X' or i=='Y' or i=='Z' or i=='W'):
                consonants = consonants + 1
    print("Number of consonants: ",consonants)
    return consonants

def count_spaces(name):
    path = os.path.join(project_path, name)
    text = readFile(path)
    counter = 0
    for t in text:
        if ' ' == t:
            counter +=1
    print("Number of spaces: ",counter)
    return counter

def JHA(name):
    n1 = count_vowels(name)
    n2 = count_consonants(name)
    SP = count_spaces(name)
    exponent = (7 * n1) - (3*n2) + pow(SP,2)
    p = int(input("Insert p please: "))
    dividers = fermat_algorithm_2(p-1)
    q = max(dividers) #find the biggest prime divider max()
    if exponent <0:
        x = modular_inverse(q,p)
        exponent = abs(exponent)
        jha = fast_exponentation_modulo_2(x,exponent,p)
    else:
        jha = fast_exponentation_modulo_2(q,exponent,p)
    print("JHA(m,p,q): ",jha)
    return jha

def DSS(name):

    #I stage:
    p = int(input("Insert p please:     "))
    dividers = fermat_algorithm_2(p-1) #from lucas
    q = int(max(dividers)) #find the biggest prime divider max()
    g =int(input("Please insert g:     "))
    while real_fast_exponentation_modulo(g, q,p) != 1:
        g =int(input("Wrong g! please insert it again:     "))
    k =int(input("Please insert k:     "))
    while k>q:
       k =int(input("Wrong k! please insert it again:     "))
    public_key = real_fast_exponentation_modulo(g, k,p) #from lucas
    prk = [public_key,g,p,q]
    print("PRK: ",prk)

    #II stage:
    r =int(input("Please insert r:     "))
    while r>q:
       r =int(input("Wrong r! please insert it again:     "))
    x = public_key % q
    path = os.path.join(project_path, name)
    m = JHA(name)
    r_rev = modular_inverse(r, q)
    y = r_rev * (m + (k*x)) % q
    s = [x,int(y)]
    print("Siganture: ",s)