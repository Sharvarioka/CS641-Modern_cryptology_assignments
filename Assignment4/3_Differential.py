import numpy as np

temp_arr = open("out_cipher.txt")
dat = temp_arr.read().split("\n")
dct = {'f' : [0,0,0,0], 'g' : [0,0,0,1], 'h' : [0,0,1,0], 'i' : [0,0,1,1], 'j' : [0,1,0,0], 'k' : [0,1,0,1], 'l' : [0,1,1,0],
       'm' : [0,1,1,1], 'n' : [1,0,0,0], 'o' : [1,0,0,1], 'p' : [1,0,1,0], 'q' : [1,0,1,1], 'r' : [1,1,0,0], 's' : [1,1,0,1],
       't' : [1,1,1,0], 'u' : [1,1,1,1]}

inp = []
for i in range(len(dat)-1):
    if (len(dat[i]) != 16):
        print (i)
    tmp=[]
    for j in range(16):
        tmp = tmp+dct[dat[i][j]]
    inp.append(tmp)


Inverse_Final_Permutation = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8]


conc_inputs = [[inp[j][Inverse_Final_Permutation[i]-1] for i in range(64)] for j in range(len(inp))] 


# XOR of Inverse Permuted Input
X_inp = [list(np.bitwise_xor(conc_inputs[2*i+1],conc_inputs[2*i])) for i in range(int(len(inp)/2))]


# Expanding R5 = L6
Exp_Box = [32, 1, 2, 3, 4, 5, 4, 5,6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
Expanded_0ut = [[conc_inputs[j][Exp_Box[i]-1] for i in range(48)] for j in range(len(inp))] 

# Calculating XOR of Alphas Or Input To S-Boxes
X_S_In = [list(np.bitwise_xor(Expanded_0ut[2*i+1],Expanded_0ut[2*i])) for i in range(int(len(inp)/2))]


# Fiestal XORED, R6 and L5 XOR
L5 = [0,0,0,0,0,1]+[0 for z in range(26)]
Fiest_Out = [list(np.bitwise_xor(X_inp[i][32:64],L5)) for i in range(len(X_inp))]


# XOR output after S-Box
Inv_Permutation_Box = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]
X_S_Out = [[Fiest_Out[j][Inv_Permutation_Box[i]-1] for i in range(32)] for j in range(len(Fiest_Out))]

file = open("XS_inp_14.txt","w")
for i in X_S_In:
    string=""
    for j in i:
        string=string+str(j)
    file.write(string)
    file.write("\n")
file.close()

file1 = open("XS_out_14.txt","w")
for i in X_S_Out:
    string=""
    for j in i:
        string=string+str(j)
    file1.write(string)
    file1.write("\n")
file1.close()

file = open("XExp_out_14.txt","w")
for i in range(len(Expanded_0ut)):
    if i%2==1:
        continue
    string=""
    for j in Expanded_0ut[i]:
        string=string+str(j)
    file.write(string)
    file.write("\n")
file.close()

print (L5)