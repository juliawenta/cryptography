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
    ##.Generating keys
    #First round
    key_0_0 = key[0:4]
    key_0_1 = key[4:8]            #Dividing key to use it for adding
    key_1_0 = key[8:12]
    key_1_1 = key[12:16]
    #adding:
    sbox = Sbox_e(key_1_1)
    on_key_0_0 =bitwise_or(key_0_0,sbox)
    key_1 = bitwise_or(on_key_0_0,['0','0','0','1'])
    key_2 = bitwise_or(key_1,key_1_0)
    key_3 = bitwise_or(key_2,key_0_1)
    key_4 = bitwise_or(key_1_1,key_3)
    #New key:
    new_key_first_round = []
    new_key_first_round.extend(key_1)
    new_key_first_round.extend(key_3)
    new_key_first_round.extend(key_2)
    new_key_first_round.extend(key_4)
    print("Key of first round: ",new_key_first_round)

    #Second round:
    k = new_key_first_round[0:4]
    k1 = new_key_first_round[8:12]
    k2 = new_key_first_round[4:8]           #Dividing key to use it for adding
    k3 = new_key_first_round[12:16]
    #adding:
    on_key_0_0_2 =bitwise_or(k,['0','0','1','0'])
    box_scndkey = Sbox_e(k3)
    key_1_2 = bitwise_or(on_key_0_0_2,box_scndkey)
    key_2_2 = bitwise_or(key_1_2,k1)
    key_3_2 = bitwise_or(key_2_2,k2)
    key_4_2 = bitwise_or(k3,key_3_2)
    #New key:
    new_key_second_round = []
    new_key_second_round.extend(key_1_2)
    new_key_second_round.extend(key_3_2)
    new_key_second_round.extend(key_2_2)
    new_key_second_round.extend(key_4_2)
    print("Key of second round: ",new_key_second_round)
    #5.Add key of first round to text
    k_first_text = []
    k_first_text = bitwise_or(res,new_key_first_round)
    print("Sum of key of first round and text: ",k_first_text)
    #6.Function SBox(E,t)
    s = k_first_text[0:4]
    s1 = k_first_text[4:8]
    s2 = k_first_text[8:12]
    s3 = k_first_text[12:16]
    s_box = Sbox_e(s)
    s1_box = Sbox_e(s1)
    s2_box = Sbox_e(s2)
    s3_box = Sbox_e(s3)
    text_box_2 = [] #array to keep text after usung function with sboxes
    text_box_2.extend(s_box)
    text_box_2.extend(s1_box)
    text_box_2.extend(s2_box)
    text_box_2.extend(s3_box)
    print("After Sbox second time: ",text_box_2)
    #7.Function ZK(t)
    zk = text_box_2[0:4]
    zk1 = text_box_2[4:8]
    zk2 = text_box_2[8:12]
    zk3 = text_box_2[12:16]
    text_zk_2 = []
    text_zk_2.extend(zk)
    text_zk_2.extend(zk1)
    text_zk_2.extend(zk2)
    text_zk_2.extend(zk3)
    print ("After Zk second time: ",text_zk_2)
    #8.Add key of second round to text
    k_second_text = []
    k_second_text = bitwise_or(text_zk_2,new_key_second_round)
    print("Encrypted text: ",k_second_text)




#task1();
task2();