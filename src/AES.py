import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.convert_module import *
from src.SDES import *


def insert_key():
    print ("Please insert 4 bits to fill key: (A, 0, 1, 1, 0, B, 1, 0, 1, 1, 1, C, D, 1, 1, 0)")
    a = input()
    b = input()
    c = input()
    d = input()
    key = [a,'0','1','1','0',b, '1', '0', '1', '1', '1', c, d, '1', '1', '0']
    print("Key: ",key)
    return key


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


def binary_dot_operation(x,y):
    xs = string_array_to_int_array(x)
    ys = string_array_to_int_array(y)
    result = []
    matrix = [[0,0,0,ys[3]*xs[0],ys[3]*xs[1],ys[3]*xs[2],ys[3]*xs[3]],
              [0,0,ys[2]*xs[0],ys[2]*xs[1],ys[2]*xs[2],ys[2]*xs[3],0],
              [0,ys[1]*xs[0],ys[1]*xs[1],ys[1]*xs[2],ys[1]*xs[3],0,0],
              [ys[0]*xs[0],ys[0]*xs[1],ys[0]*xs[2],ys[0]*xs[3],0,0,0]]
    for i in range(0,7):
        sum = matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]
        modulo = sum % 2
        result.append(str(modulo))
    return result

def fill_with_zero(xs,length):
    r = length - len(xs)
    result = []
    for i in range(r):
        result.append(0)
    for x in xs:
        result.append(x)
    return result

#This method works on ints
def binary_division_operation(xs):
    result = []
    ys =  [1,0,0,1,1]
    xs1 = fill_with_zero(xs,7)
    ys1 = fill_with_zero(ys,7)

    if xs[0] == 0 and xs[1] == 0 and xs[2] == 0:        
        return xs[3:7]
    else:
        
        res = []
        for i in range(0,7):
            res.append((xs1[i]+ys1[i]) % 2)
        if res[0] == 0 and res[1] == 0 and res[2] == 0:        
            return res[3:7]
        len2 = len(ys1)
        
        if res[0] == 0 and res[1] == 0 and res[2] == 0:
            return res[3:7]
        elif res[0] == 0 and res[1] == 0:

            return binary_division_operation(res)
        elif res[0] == 0:
  
            ys =  [0,1,0,0,1,1]
            return binary_division_operation(res)
        elif res[0] != 0 and res[1] != 0 and res[2] != 0:
            return binary_diivision_operation(res)
  
    return result






    
