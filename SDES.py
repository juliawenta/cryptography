
def insert_data(max_size):
    print ("Please insert some bits (max "+str(max_size)+")")
    text = []
    text = input()
    if len(text)- text.count(',')>max_size:
        print("Fail, text to long")
    if len(text)- text.count(',')<max_size:
        for i in range (len(text)- text.count(','),max_size):
            text = text + ',0'
    return text.split(',')


#This method allow to change order in key according to permutation
def generate_permutation(key,permutation):
    res = []
    for i in range (0,len(permutation)):
        res.append(key[int(permutation[i])])
    return res

def generate_permutation_sl1(key):
    permutation = []
    for i in range (0,len(key)):
        if i < len(key)-1:
            permutation.append(i+1)
        else: 
            permutation.append(0)
    return generate_permutation(key,permutation)
       
def generate_permutation_sl2(key):
    permutation = []
    for i in range (0,len(key)):
        if i < len(key)-2:
            permutation.append(i+2)
        elif i < len(key)-1:
            permutation.append(0)
        else: 
            permutation.append(1)
    return generate_permutation(key,permutation)


#Binary operation xor on xs,ys (must have same length)
def bitwise_or(xs,ys):
    result = []
    for i in range(0,len(xs)):
        or_operation = int(xs[i]) != int(ys[i])
        if or_operation is True:
            result.append('1')
        else: 
            result.append('0')
    return result
        
def get_decimal(x,y):
    if x == 0:
        if y == 0:
            return 0
        else: 
            return 1
    else:
        if y == 0:
            return 2
        else:
            return 3
     
def sbox1(xs):
    bits = [['0','0'],['0','1'],['1','0'],['1','1']]
    box = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    row = get_decimal(int(xs[0]),int(xs[3]))
    column =get_decimal(int(xs[1]),int(xs[2]))
    decimal_result = box[row][column]
    bit_result = bits[decimal_result]
    return bit_result

def sbox2(xs):
    bits = [['0','0'],['0','1'],['1','0'],['1','1']]
    box = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    row = get_decimal(int(xs[0]),int(xs[3]))
    column =get_decimal(int(xs[1]),int(xs[2]))
    decimal_result = box[row][column]
    bit_result = bits[decimal_result]
    return bit_result
      
def generate_keys():
    #1. Permutation P10 of the sequence of bits of kp described by the formula:
    key = ['1', '1', '0', '0', '0', '0', '0', '0', '1', '1']
    permutation10_order = ['2','4','1','6','3','9','0','8','7','5']
    permutation10 = generate_permutation(key,permutation10_order)
    #2.The division of received 10-bit string into two 5-bit 'k'
    k0 = permutation10[0:5]
    k1 = permutation10[5:10]
    #3. Shift of the received strings by one item 'in left' (sl1 permutation)
    sl1_k0 = generate_permutation_sl1(k0)
    sl1_k1 = generate_permutation_sl1(k1)
    #4.Key first round:
    sl1_sum = []
    sl1_sum.extend(sl1_k0)
    sl1_sum.extend(sl1_k1)
    permutation10_in_8order = ['5','2','6','3','7','4','9','8']
    k1 = generate_permutation(sl1_sum,permutation10_in_8order) #key of the first round
    #5.Key second round:
    sl2_k0 = generate_permutation_sl2(sl1_k0)
    sl2_k1 = generate_permutation_sl2(sl1_k1)
    sl2_sum = []
    sl2_sum.extend(sl2_k0)
    sl2_sum.extend(sl2_k1)
    permutation10_in_8order = ['5','2','6','3','7','4','9','8']
    k2 = generate_permutation(sl2_sum,permutation10_in_8order) #key of the first round
    tuple = (k1,k2)
    #print("Key of first round : ",k1)
    # print("Key of second round: ",k2)
    return tuple
   

def encryption_keys(key, text):
    #1.The division of text into two 4-bit 't'
    t1 = text[0:4]
    t2 = text[4:8]
    #2.Operation P4in8 on kopy of t2
    permutation = ['3', '0', '1', '2', '1', '2', '3', '0']
    t2_permutation_4in8 = generate_permutation(t2,permutation)
    #3.Binary operation on received text and key
    sum_permutation_key = bitwise_or(t2_permutation_4in8,key)
    sum1 = sum_permutation_key[0:4]
    sum2 = sum_permutation_key[4:8]
    #4.Sum1 and Sum2 modified by sboxes
    sbox_1 = sbox1(sum1)
    sbox_2 = sbox2(sum2)
    #5.Sum of sboxes and permutation
    sum = []
    sum.extend(sbox_1)
    sum.extend(sbox_2)
    permut = ['1','3','2','0']
    sequence_p4 = generate_permutation(sum,permut)
    #6.Binary sum of sequence_p4 and t1
    q = bitwise_or(t1,sequence_p4)
    #7.Final sum up of q and t2
    f_sum = []
    f_sum.extend(q)
    f_sum.extend(t2)
    return (f_sum)


 
    