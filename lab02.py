from SDES import *
  

def task1():
    #encryption
    text = insert_data(8)
    #text = ['1','1','1','1','0','0','0','0']
    #1. permutation
    permutation_f = ['1', '5', '2', '0', '3', '7', '4', '6']
    pf = generate_permutation(text, permutation_f)
    #2. encryption by 1st key
    keys = generate_keys()
    
    encryption_by_first_key = encryption_keys(keys[0], pf)
    #3. Crossing
    cross1 = encryption_by_first_key[0:4]
    cross2 = encryption_by_first_key[4:8]
    #TODO move cross to new function!!
    cross = [] #making an array with swapping the first 4 bits with the last four
    cross.extend(cross2)
    cross.extend(cross1)    
    #4. encryption by 2nd key    
    encryption_by_second_key = encryption_keys(keys[1], cross)
    #5. Opposite permutation
    permutation_r = ['3', '0', '2', '4', '6', '1', '7', '5']
    pr = generate_permutation(encryption_by_second_key, permutation_r)
    print(pr)
    return pr
   
def task2():
    #decryption
    text = insert_data(8)
    #text = ['1','1','1','1','0','0','0','0']
    permutation_f = ['1', '5', '2', '0', '3', '7', '4', '6']
    pf = generate_permutation(text, permutation_f)
    
    keys = generate_keys()
    encryption_by_second_key = encryption_keys(keys[1], pf)
    cross1 = encryption_by_second_key[0:4]
    cross2 = encryption_by_second_key[4:8]
    
    cross = [] #making an array with swapping the first 4 bits with the last four
    cross.extend(cross2)
    cross.extend(cross1)
   
    encryption_by_first_key = encryption_keys(keys[0], cross)
 
    permutation_r = ['3', '0', '2', '4', '6', '1', '7', '5']
    pr = generate_permutation(encryption_by_first_key, permutation_r)
    print(pr)
    return pr
 


task1()
task2()