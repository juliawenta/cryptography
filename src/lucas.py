import math

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

#   Found d in:
#   a = (2^k)*d
def found_d(result):
    #result = input()
    while True:
        modulo = result%2
        if modulo == 1:
            break
        result = result/2
    return result

def find_dividers(d,x):
    is_true = True
    while is_true:
        yy = pow(x,2)
        print("yy",yy)
        y = yy-d
        if y > 0 and math.floor(math.sqrt(y)) == math.sqrt(y):
            return (x,math.sqrt(y))
        else:
            x = x + 1
            is_true = x<(d+1)/2



def find_primes(d,y,primes):
    dividers = find_dividers(d,y)
    print (dividers)
    if dividers is []:
        #if len(dividers) == 1:
         #   primes.append(dividers[0])
        return primes
    sum = dividers[0::1]
    print(sum)
    
    diff = math.fabs(dividers[0]-dividers[1])
    print(diff)
    if diff == 1:
        return []
    p1 = find_primes(sum,y,primes)
    p2 = find_primes(diff,y,primes)
    if p1.size == 2:
        primes.append(p1[0])
        primes.append(p1[1])
    if p2.size == 2:
        primes.append(p2[0])
        primes.append(p2[1])
    
    return primes

def fermat_algorithm():
    d = found_d(78)
    y = check_d(d)
    primes = []
    primes = find_primes(d,y,primes)
    return d

def check_d(d):
    d_sqrt = math.sqrt(d)
    d_sqrt_floor  = math.floor(d_sqrt)
    if d_sqrt_floor == d_sqrt:
        return d_sqrt_floor
    else:
        return d_sqrt_floor + 1
