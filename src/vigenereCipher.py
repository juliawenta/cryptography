import string

#This method changes every string of letters to array of numbers
def get_indexed_string(str):
    indexed_str = [] 
    for k in str:
        indexed_str.append(string.ascii_lowercase.index(k))              
    return indexed_str

#This method changes numbers back to letters
def parse_numbers(numbers):
    text = [] #array to hold letters
    for n in numbers:
        text.append(chr(n+97))
    return ''.join(text)


#This method takes text to encrypt and the key and returns new encrypted text
def encrypt (text, key):    
    indexed_text = get_indexed_string(text)
    indexed_key = get_indexed_string(key)
    
    cryptogram=[] #new array of numbers
    it = 0 #indexes 0,1,2 etc
    ik = 0
    for t in indexed_text:
        new_letter = indexed_text[it] + indexed_key[ik] #each letter is sum of indexed letter from text and key
        if new_letter>=26: #compare to 26 because it a number of letters in english alphabet
            new_letter=new_letter-26
        cryptogram.append(new_letter)
        ik = ik + 1
        it = it + 1
        if ik > len(indexed_key) - 1:
            ik = 0
    
    return parse_numbers(cryptogram)


#This method count letters in text
def count_letters(text,letter):
    counter = 0
    for c in text:
        if letter == c:
            counter +=1
    return counter


#This method calculate the coincidence index
def get_coincidence_index(text):
    length = len(text)
    indexes = []
  
    for i in range(0,25):
        indexes.append(i)
    alphabet = parse_numbers(indexes)
    sum = 0
    for c in alphabet:
        n = count_letters(text,c)
        sum = sum + (n*(n-1))
    return sum/(len(text)* (len(text)-1))

#This method creates matrix with columns with user's size
def create_text_matrix(text,column_size):

    matrix = []
    for i in range(0,column_size):
        array = []
        matrix.append(array)

    ic = 0
    for it in range(0,len(text)):
        array = matrix[ic]
        array.append(text[it])
        matrix[ic]= array
        it += 1
        ic += 1
        if ic > column_size - 1:
            ic = 0
    return matrix
   
#This method calculate coincidence index for each column with user's size
 
def if_coincidence_index_for_column_size(text, column_size):
    text_matrix = create_text_matrix(text, column_size)
    ok = 0
    for i in range(0,column_size):
        ic = get_coincidence_index(text_matrix[i])
        if ic > 0.064 and ic < 0.069:
            ok += 1     
    if ok == column_size:   #If in every column propability equal to english value 
        return True
    else:
        return False

#This method calculate mutual coincidence index
def get_mutual_coincidence_index(column_1,column_2):
    length_1 = len(column_1)
    length_2 = len(column_2)
    indexes = []
  
    for i in range(0,25):
        indexes.append(i)
    alphabet = parse_numbers(indexes)
    sum = 0
    for c in alphabet:
        n1 = count_letters(column_1,c)
        n2 = count_letters(column_2,c)
        sum = sum + (n1*n2)
    return sum/(length_1 * length_2)
