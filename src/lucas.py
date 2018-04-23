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

