import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.AES import *
from src.SDES import *


def task1():
    #Getting bits
    text_1 = insert_data(4)
    print("First: ",text_1)
    text_2 = insert_data(4)
    print("Second: ",text_2)


def task2():
    #1. Add key to the text
    text_t = ['0',' 0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1']
    key = ['1',' 0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0']
    #key_p = insert_key()
    result = bitwise_or(text_t,key)
    print ("Sum: ",result)
    #2.Function SBox(E,t)
    first = result[0:4]
    second = result[4:8]
    third = result[8:12]  #divide result to make sbos operation
    fourth = result[12:16]
    first_box = Sbox_e(first)
    second_box = Sbox_e(second)
    third_box = Sbox_e(third)
    fourth_box = Sbox_e(fourth)
    text_box = [] #array to keep text after usung function with sboxes
    text_box.extend(first_box)
    text_box.extend(second_box)
    text_box.extend(third_box)
    text_box.extend(fourth_box)
    print("After Sbox: ",text_box)
    #3.Function ZK(t)
    fst = text_box[0:4]
    scnd = text_box[4:8]
    previous = text_box[8:12]
    last = text_box[12:16]
    text_zk = []
    text_zk.extend(fst)
    text_zk.extend(scnd)
    text_zk.extend(last)
    text_zk.extend(previous)
    print ("After Zk: ",text_zk)
    #4.Multiplying                  TODO
    m = ['0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1']
    res = multiplication(m,text_zk)
    print("Multiply: ", res)
    #5.Generating keys
    new_key = []
    key_0_0 = key[0:4]
    key_1_0 = key[4:8]            #Dividing key to use it for adding
    key_0_1 = key[8:12]
    key_1_1 = key[12:16]
    #adding:
    on_key_0_0 =bitwise_or(key_1_1,['0','0','0','1'])
    
    box_on_key_0_0 = Sbox_e(on_key_0_0)
    key_1 = bitwise_or(key_0_0,box_on_key_0_0)
    key_2 = bitwise_or(key_0_0,key_1_0)
    key_3 = bitwise_or(key_0_1,key_1_0)
    key_4 = bitwise_or(key_1_1,key_0_1)
    new_key.extend(key_1)
    new_key.extend(key_2)
    new_key.extend(key_3)
    new_key.extend(key_4)
    print(new_key)
    #print(key_2)
    

#task1();
task2();