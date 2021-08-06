from des import *
import os
import random

input_set = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

#input 
left_xor = ['0000','0000','0000','0000','1000','0000','0001','0000']  #00008010 
right_xor = ['0000','0000','0000','0000','0100','0000','0000','0000'] #00004000

username = "CodeNymro"
password = "NymroCode123"
level = "4" 


alphabet_map = {}
def alphabet_mapping(initial):
	global alphabet_map
	k=initial
	for i in input_set:
		alphabet_map[i]=bit_set[k]
		k = (k+1)%16


def findPair(inp, list_xor):
	tmp_list = list(inp)
	plaintext2 = []
	k = 0
	for i in tmp_list:
		t1 = list(alphabet_map[i])
		t2 = list(list_xor[k])
		result_xor = xor(t1, t2)
		for j in alphabet_map:
			if alphabet_map[j] == (''.join(result_xor)):
				plaintext2.append(j)
				break
		k += 1 
	plaintext2 = ''.join(plaintext2)
	return plaintext2	
	

# Returns the plaintext for the entered plaintext maintaining xor difference
# inp will be in the form - "16 chars : {L_0R_0}"
def generate_pair(inp):      
    L_10 = inp[:8]
    R_10 = inp[8:]
    L_20 = findPair(L_10, left_xor)
    R_20 = findPair(R_10, right_xor)
    return L_20 + R_20        

def random_string(characters, length):
    random_str = ''
    for i in range(length):
        character = random.choice(characters)
        random_str += character
    return random_str

def input_pairs():
    if os.path.isfile('input.txt'):
        os.remove('input.txt')

    f = open('input.txt','a+')
    count = 0
    f.write(username +"\n" +password +"\n" +level +"\nread\n")
    
    while count < 100:
        plaintext1 = random_string(input_set, 16)
        f.write(plaintext1+"\nc\n")
        plaintext2 = generate_pair(plaintext1)
        f.write(plaintext2 + "\nc\n")
        count+=1
    f.write("back\nexit\n")
    f.close()




alphabet_mapping(0)
input_pairs()









