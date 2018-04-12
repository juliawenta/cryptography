#converting arrays into strings from ints or from ints to strings 

def string_array_to_int_array(list):
    #list = ['1' , '2', '3']  -  > list = [1 ,2, 3]
    list2 = []
    for i in range(len(list)):
        t = int(list[i])
        list2.append(t)

    return list2

def int_to_string(list):
    #list = [1 , 2, 3]  -  > list = ['1' ,'2', '3']
    lis2 = []
    for x in list:
       list2.append(str(x)) 
    return list2
