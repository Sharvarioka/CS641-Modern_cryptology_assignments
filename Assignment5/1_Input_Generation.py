import numpy as np


username = "CodeNymro"
password = "NymroCode123"
level = "5" 
commands = ["go", "wave", "dive", "go", "read"]
filenames = ['input/input1_1.txt', 'input/input1_2.txt', 'input/input2_1.txt', 'input/input2_2.txt', 'input/input3_1.txt',
             'input/input3_2.txt', 'input/input4_1.txt', 'input/input4_2.txt', 'input/input5_1.txt', 'input/input5_2.txt',
             'input/input6_1.txt', 'input/input6_2.txt', 'input/input7_1.txt', 'input/input7_2.txt', 'input/input8_1.txt',
             'input/input8_2.txt' ]

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i,"b"))
    numi = int(num[3]) + 2 *int(num[2]) + int(num[1]) * 4 + int(num[0])*8
    mapping[num] = chr(ord('f')+numi)
k=0
file1 = open("input.txt","w+")
for i in range(8):
    
    file = open(filenames[k],"w+")
    file.write(username +"\n" +password +"\n" +level +"\n")
    for x in commands:
        file.write(x +"\n")
    for j in range(0,64):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        file.write(strr)
        file1.write(strr)
        file1.write(" ")
        file.write("\nc\n")
    file.write("back\nexit\n")
    file.close()
    k=k+1
        
    file = open(filenames[k],"w+")
    file.write(username +"\n" +password +"\n" +level +"\n")
    for x in commands:
        file.write(x +"\n")
    for j in range(64,128):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        file.write(strr)
        file1.write(strr)
        file1.write(" ")
        file.write("\nc\n")
    file.write("back\nexit\n")
    file1.write("\n")
    file.close()
    
    k=k+1
file1.close()

