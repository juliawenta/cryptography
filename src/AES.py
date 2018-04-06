
def insert_key():
    print ("Please insert 4 bits to fill key: (A, 0, 1, 1, 0, B, 1, 0, 1, 1, 1, C, D, 1, 1, 0)")
    a = input()
    b = input()
    c = input()
    d = input()
    key = [a,'0','1','1','0',b, '1', '0', '1', '1', '1', c, d, '1', '1', '0']
    print("Key: ",key)
    return key

def multiplication(a, b):

    return 

def Sbox_e(input):
    output = []
    if input == ['0','0','0','0']:
        output = ['1','1','1','0']
    elif input == ['0','0','0','1']:
        output = ['0','1','0','0']
    elif input == ['0','0','1','0']:
        output = ['1','1','0','1']
    elif input == ['0','0','1','1']:
        output = ['0','0','0','1']
    elif input == ['0','1','0','0']:
        output = ['0','0','1','0']
    elif input == ['0','1','0','1']:
        output = ['1','1','1','1']
    elif input == ['0','1','1','0']:
        output = ['1','0','1','1']
    elif input == ['0','1','1','1']:
        output = ['1','0','0','0'] 
    elif input == ['1','0','0','0']:
        output = ['0','0','1','1']
    elif input == ['1','0','0','1']:
        output = ['1','0','1','0']
    elif input == ['1','0','1','0']:
        output = ['0','1','1','0']
    elif input == ['1','0','1','1']:
        output = ['1','1','0','0']
    elif input == ['1','1','0','0']:
        output = ['0','1','0','1']
    elif input == ['1','1','0','1']:
        output = ['1','0','0','1']
    elif input == ['1','1','1','0']:
        output = ['0','0','0','0']
    elif input == ['1','1','1','1']:
        output = ['0','1','1','1']
    return output
    

def Sbox_d(input):
    output = []
    if input == ['0','0','0','0']:
        output = ['1','1','1','0']
    elif input == ['0','0','0','1']:
        output = ['0','0','1','1']
    elif input == ['0','0','1','0']:
        output = ['0','1','0','0']
    elif input == ['0','0','1','1']:
        output = ['1','0','0','0']
    elif input == ['0','1','0','0']:
        output = ['0','0','0','1']
    elif input == ['0','1','0','1']:
        output = ['1','1','0','0']
    elif input == ['0','1','1','0']:
        output = ['1','0','1','0']
    elif input == ['0','1','1','1']:
        output = ['1','1','1','1'] 
    elif input == ['1','0','0','0']:
        output = ['0','1','1','1']
    elif input == ['1','0','0','1']:
        output = ['1','1','0','1']
    elif input == ['1','0','1','0']:
        output = ['1','0','0','1']
    elif input == ['1','0','1','1']:
        output = ['0','1','1','0']
    elif input == ['1','1','0','0']:
        output = ['1','0','1','1']
    elif input == ['1','1','0','1']:
        output = ['0','0','1','0']
    elif input == ['1','1','1','0']:
        output = ['0','0','0','0']
    elif input == ['1','1','1','1']:
        output = ['0','1','0','1']
    return output