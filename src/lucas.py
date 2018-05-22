import math

#method to remove duplicates from array
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

#method to check if number is prime 
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#method to change decimal number to binary
def get_binary(x):
    x = "{0:b}".format(int(x))
    return x

#method to calculate a^b mod c
def power_modulo(binary,number,modulo):
    tab = []
    i=0
    for r in binary:
        if r == 1:
            tab.append(pow(int(number),(pow(2,i))))
        i+=1

    tab_modulo = []
    for t in tab:
        tab_modulo.append(t%int(modulo))

    result = 1
    for m in tab_modulo:
        result=((result*m)%int(modulo))
    return result 
    
    
def fast_exponentation_modulo():
    print("\t Insert a number please:")
    a = input()
    print("\t Insert an exponent please:")
    b = input()
    print("\t Insert modulo please:")
    modulo = input()
    bb = get_binary(b) #change exp to binary
    binary = []
    for i in bb:
        if i == '0':
            binary.append(0)
        else:
            binary.append(1)
  
    rev_binary = binary[::-1] #reverse
    result = power_modulo(rev_binary,a,modulo)
    print("\n The result is: ",result)

    return result


def fast_exponentation_modulo_2(a,b,modulo):
    bb = get_binary(b) #change exp to binary
    binary = []
    for i in bb:
        if i == '0':
            binary.append(0)
        else:
            binary.append(1)
  
    rev_binary = binary[::-1] #reverse
    result = power_modulo(rev_binary,a,modulo)
 

    return result

def real_fast_exponentation_modulo(a,b,modulo):    
    bb = get_binary(b) #change exp to binary
    binary = []
    for i in bb:
        if i == '0':
            binary.append(0)
        else:
            binary.append(1)
  
    rev_binary = binary[::-1] #reverse

    result = power_modulo(rev_binary,a,modulo)

    return result


#   Found d in:
#   a = (2^k)*d

def found_d(number):
    tab=[]

    while number % 2 == 0:
        number = number/2
    tab.append(number)
    
 
    return tab[0] 


def find_dividers(d,x):
    is_true = True
    
    while is_true:
        yy = pow(x,2)
        y = yy-d
        if y >= 0 and math.floor(math.sqrt(y)) == math.sqrt(y):
            
            return (x,math.sqrt(y))
        else:
            x = x + 1
            
            is_true = x<(d+1)/2
    
        
def find_primes(d,y,primes):
    dividers = find_dividers(d,y)
    
    if dividers is None:
        return []
    sum = dividers[0]+dividers[1]
        
    diff = math.fabs(dividers[0]-dividers[1])
  
    if is_prime(diff):
        primes.append(diff)
    else:
        p1 = find_primes(diff,check_d(diff),primes)

    if is_prime(sum):
        primes.append(sum)
    else:
        p2 = find_primes(sum,check_d(sum),primes)
        
    if 1 in primes:
        primes.remove(1)

    return primes

def fermat_algorithm(x):

    d = found_d(x)
    y = check_d(d)
    primes = []
    primes = find_primes(d,y,primes)
    two_multiplication = int(math.log((x/d), 2))
    for i in range(0, two_multiplication):
        primes.append(2)
    primes_no_duplicates = remove_duplicates(primes)
    print("Primes: ",primes_no_duplicates)
    fold=[]
    for p in primes_no_duplicates:
        fold.append(primes.count(p))
    print("Folds: ",fold)
    return primes_no_duplicates


def fermat_algorithm_2(x):

    d = found_d(x)
    y = check_d(d)
    primes = []
    primes = find_primes(d,y,primes)
    two_multiplication = int(math.log((x/d), 2))
    for i in range(0, two_multiplication):
        primes.append(2)
    primes_no_duplicates = remove_duplicates(primes)
    
    fold=[]
    for p in primes_no_duplicates:
        fold.append(primes.count(p))
    return primes

def check_d(d):
    d_sqrt = math.sqrt(d)
    d_sqrt_floor  = math.floor(d_sqrt)
    
    if d_sqrt_floor == d_sqrt:
        return d_sqrt
    else:
        return d_sqrt_floor + 1

def lucas_test(n,q):

    fermat = fermat_algorithm_2(n-1) 
    is_prime = True
    for f in fermat:
        power = (n-1)/f
        print("The power is: ",power)
        x = real_fast_exponentation_modulo(q,power,n) #x is a value of modulo
        if x == 1: 
            is_prime = False
        print("X",x)
 
    return is_prime