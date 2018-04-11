import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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


def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

def string_array_to_int_array(list):
   # list = ['1' , '2', '3']
    list2 = []
    for i in range(len(list)):
        t = int(list[i])
        list2.append(t)

    return list2


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

#work on int not strings!!
def binary_division_operation(xs,ys):
    result = []
    xs1 = fill_with_zero(xs,7)
    ys1 = fill_with_zero(ys,7)

    if xs1[0] == 0 and xs1[1] == 0 and xs1[2] == 0:        
        return xs[3:7]
    else:
        res = []
        for i in range(0,7):
            res.append((xs1[i]+ys1[i]) % 2)
        len2 = len(ys1) - 1
        if xs1[1] == 0:
            len2 = len2 - 1
        result = binary_division_operation(res,ys1[0:len2])
    return result

def int_to_string(xs):
    res = []
    for x in xs:
       res.append(str(x)) 
    return res

def binary_dot_operation_2(x,y):
    a =  ''.join(str(e) for e in x)
    b =  ''.join(str(e) for e in y)
    result = []
    bit1 = a
    bit2 = b
    g = []
    nobits = len(y)	
    #str = "x"+b;

    b=reverse(b)
    for i in range (0,nobits):
        if (b[i]=='0'):
            g.append(0)
        else:
            g.append(int((bit1[i])))
    res=int(g[0])
    for i in range (1,nobits):
        res = int(res) ^ int(g[i])
    print(res)
    return result


def multiplication(tab1, tab2):
    wynik = []

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

