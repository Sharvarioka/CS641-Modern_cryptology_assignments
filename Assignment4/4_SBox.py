import numpy as np


S_Box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],
    [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9]],

    [[10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]


X_S_In = open("XS_inp_14.txt").read().split("\n")
X_S_Out = open("XS_out_14.txt").read().split("\n")
LOut = open("XExp_out_14.txt").read().split("\n")
Keys = np.zeros((8,64))


def SBoxOut(a, b, s):
    a = '{:0>6}'.format(format(a,"b"))
    b = '{:0>6}'.format(format(b,"b"))
    r1 = int(a[0])*2 + int(a[5])
    r2 = int(b[0])*2 + int(b[5])
    c1 = int(a[4]) + 2 *int(a[3]) + int(a[2]) * 4 + int(a[1])*8
    c2 = int(b[4]) + 2 *int(b[3]) + int(b[2]) * 4 + int(b[1])*8    
    return (S_Box[s][r1][c1])^(S_Box[s][r2][c2])


for i in range(len(X_S_In)):
    if X_S_In[i]=="":
        continue
    inpxs = X_S_In[i]
    outxs = X_S_Out[i]
    inpos = LOut[i]       #LHS of the final output expanded 
    for j in range(8):
        inx = int(inpxs[j*6:j*6+6], 2)
        outx = int(outxs[j*4:j*4+4], 2)
        inp_orig = int(inpos[j*6:j*6+6], 2)
        for k in range(64):
            if outx == SBoxOut(k, k^inx, j):
                key_cand = k^inp_orig
                Keys[j][key_cand] = Keys[j][key_cand] + 1


print(Keys)


import operator
max_key = []
average = []
index = []
for i in Keys:
    inde, value = max(enumerate(i), key=operator.itemgetter(1))
    max_key.append(int(value))
    index.append(inde)
    average.append(int(round(np.mean(i))))
print(max_key)
print(average)
print(index)


key = [24,27,21,6,11,15,
13,10,25,16,3,20,
51,34,41,47,29,37,
40,50,33,55,43,30,
54,31,49,38,44,35,
56,52,32,46,39,42]
vals = {}
keys = []
for i in key:
    keys.append(i-1)
Missing_Key = [-1 for i in range(56)]
keys_bin = []
k=0
for i in range(8):
    if i==0 or i==1 or i>3:
        keys_bin.append('{:0>6}'.format(format(index[i],"b")))
        for j in range(6):
            vals[keys[k*6+j]] = int(keys_bin[k][j])
        k=k+1
marked = [0 for i in range(56)]
for i in range(56):
    if i in keys:
        marked[i]=1
        Missing_Key[i] = int(vals[i])
print(Missing_Key)


Final_Keys = []
for i in range(2**20):
    tmp = list('{:0>20}'.format(format(i,"b")))
    done = 0
    mkey = [Missing_Key[j] for j in range(56)]
    for j in range(56):
        if Missing_Key[j]==-1:
            mkey[j] = int(tmp[done])
            done=done+1
    Final_Keys.append(mkey)

print(len(Final_Keys))

