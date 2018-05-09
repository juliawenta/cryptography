from math import sqrt

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

