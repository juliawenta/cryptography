from math import sqrt
from math import floor

#method to calculate Eratosthenes sieve        
def sieve(n):
    tab = []
    for i in range(0, n):
        tab.append(True)

    for i in range(2, int(sqrt(n))): #2 <= q <= sqrt(n)
            for j in range(pow(i,2), n, i):
                if tab[j] == True:
                    if j % i == 0:
                        tab[j] = False
    primes = [] 
    for i in range(2, n):
        if tab[i] == True:
            primes.append(i)
    return primes


#method to calculate the greatest common divisor of two ints
def euclid(a, b):
    '''
    x * a0 + y * b0 = a and x1 * a0 + y1 * b0 = b, 
    so greatest common divisor(a0, b0) = x · a0 + y · b0.
    '''
    x = 1
    y = 0
    x1 = 0
    y1 = 1

    while b != 0:
        mod = a%b
        q = floor(a/b)
        a = b
        b = mod

        i = x1
        j = y1
        x1 = x - q * x1
        y1 = y - q * y1
        x = i
        y = j

    #print("d: ", a , "x: " , x , "y: " , y)
    return a, x, y


def modular_inverse(a, m):
    q, x, y = euclid(a, m)
    if q != 1:
        raise Exception('No modular inverse')
    return x%m

