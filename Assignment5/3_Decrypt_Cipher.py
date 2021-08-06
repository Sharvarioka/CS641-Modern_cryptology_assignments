import numpy as np
np.set_printoptions(threshold=np.inf)
from pyfinite import ffield

mapping = {'0000': 'f', '0001': 'g', '0010': 'h', '0011': 'i', '0100': 'j', '0101': 'k', '0110': 'l', '0111': 'm', 
            '1000': 'n', '1001': 'o', '1010': 'p', '1011': 'q', '1100': 'r', '1101': 's', '1110': 't', '1111': 'u'}

F = ffield.FField(7)
exp_store = [[-1]*128 for i in range(128)]
exponent = [[] for i in range(8)]       #possible exponents
diagonal = [[[] for i in range(8)] for j in range(8)]   #possible diagonal values

def block_to_byte(c):
    plainText = ""
    for i in range(0, len(c), 2):
        plainText += chr(16*(ord(c[i]) - ord('f')) + ord(c[i+1]) - ord('f'))
    return plainText


def Expo (no, pow):
    if exp_store[no][pow] != -1:
        return exp_store[no][pow]

    result = 0;
    if pow == 0:
        result = 1
    elif pow == 1:
        result = no
    elif pow%2 == 0:
        sqrt_no = Expo(no, pow>>1)
        result = F.Multiply(sqrt_no, sqrt_no)
    else:
        sqrt_no = Expo(no, pow>>1)
        result = F.Multiply(sqrt_no, sqrt_no)
        result = F.Multiply(no, result)

    exp_store[no][pow] = result
    return result


def LinearTransformation (mat, elist):
    mult = [0]*8
    Add = [0]*8
    for row, elem in zip(mat, elist):
        for i, j in enumerate(row):
            mult[i] = F.Multiply(j, elem)
        for i, (e1, e2) in enumerate(zip(mult, Add)):
            Add[i] = e1 ^ e2    
    return Add


input_file = open("input.txt", 'r')
output_file = open("out_cipher.txt", 'r')

for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    inpString = []
    outString = []
    #Converting each input to hex
    for hexi in iline.strip().split(" "):
        inpString.append(block_to_byte(hexi)[ind])
    for hexo in oline.strip().split(" "):
        outString.append(block_to_byte(hexo)[ind])
        
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for inps, outs in zip(inpString, outString):
                #iterate all possible values and check if input maps to output
                if ord(outs) != Expo(F.Multiply(Expo(F.Multiply(Expo(ord(inps), i), j), i), j), i):
                    flag = False
                    break
            if flag:
                exponent[ind].append(i)
                diagonal[ind][ind].append(j)
input_file.close()
output_file.close()
print("Possible diagonnal")
print(diagonal)
print("Possible corresponding exponents")
print(exponent)
print("\n")


input_file = open("input.txt", 'r')
output_file = open("out_cipher.txt", 'r')
for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    #Considering only first 6 pairs
    if ind > 6 :
        break
    inpString = []
    outString = []
    #Converting each input to corresponding hex values
    for hexi in iline.strip().split(" "):
        inpString.append(block_to_byte(hexi)[ind]) 
    for hexo in oline.strip().split(" "):
        outString.append(block_to_byte(hexo)[ind+1])
        
    for i in range(1, 128):
        #We loop over all possible pairs of exponents and diagonal values
        for p1, e1 in zip(exponent[ind+1], diagonal[ind+1][ind+1]):
            for p2, e2 in zip(exponent[ind], diagonal[ind][ind]):
                flag = True
                for inp, outp in zip(inpString, outString):
                    if ord(outp) != Expo(F.Multiply(Expo(F.Multiply(Expo(ord(inp), p2), e2), p2), i) ^ F.Multiply(Expo(F.Multiply(Expo(ord(inp), p2), i), p1), e1), p1):
                        flag = False
                        break
                if flag:
                    exponent[ind+1] = [p1]
                    diagonal[ind+1][ind+1] = [e1]
                    exponent[ind] = [p2]
                    diagonal[ind][ind] = [e2]
                    diagonal[ind][ind+1] = [i]
input_file.close()
output_file.close()
#print(diagonal)
#print(exponent)


def EAEAE (plaintext, Linear_Matrix, Exponen_Matrix):
    plaintext = [ord(i) for i in plaintext]
    Output = [[0 for j in range (8)] for k in range(8)]
    
    for ind, elem in enumerate(plaintext):
        Output[0][ind] = Expo(elem, Exponen_Matrix[ind])

    Output[1] = LinearTransformation(Linear_Matrix, Output[0])

    for ind, elem in enumerate(Output[1]):
        Output[2][ind] = Expo(elem, Exponen_Matrix[ind])

    Output[3] = LinearTransformation(Linear_Matrix, Output[2])

    for ind, elem in enumerate(Output[3]):
        Output[4][ind] = Expo(elem, Exponen_Matrix[ind])
    return Output[4]


for index in range(6):
    next = index + 2
    
    exp_list = [e[0] for e in exponent]
    lin_trans_list = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            lin_trans_list[i][j] = 0 if len(diagonal[i][j]) == 0 else diagonal[i][j][0]
    inp = open("input.txt", 'r')
    out = open("out_cipher.txt", 'r')
    for ind, (iline, oline) in enumerate(zip(inp.readlines(), out.readlines())):
        if ind > (7-next):
            continue
        inpString = [block_to_byte(msg) for msg in iline.strip().split(" ")]
        outString = [block_to_byte(msg) for msg in oline.strip().split(" ")]
        for i in range(1, 128):
            lin_trans_list[ind][ind+next] = i
            flag = True
            for inps, outs in zip(inpString, outString):
                if EAEAE(inps, lin_trans_list, exp_list)[ind+next] != ord(outs[ind+next]):
                    flag = False
                    break
            if flag:
                diagonal[ind][ind+next] = [i]
    inp.close();
    out.close();
lin_trans_list = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lin_trans_list[i][j] = 0 if len(diagonal[i][j]) == 0 else diagonal[i][j][0]


Linear_Transformation_Matrix = lin_trans_list
Exponentiation_Matrix = exp_list

Linear_Transformation_Matrix[6][7]=83
print("Linear Transformation Matrix")
print(Linear_Transformation_Matrix)
print("Exponentiation Matrix")
print(Exponentiation_Matrix)
print("\n")

password_1 = "jgjliljpglmfkrij"   #first 8 byte
password_2 = "miirmrlfllitgrgh"   #last 8 byte

def byte_to_char(b):
    binnum = '{:0>8}'.format(format(b,"b"))
    a = mapping[binnum[0:4]], mapping[binnum[4:8]]
    return a[0]+a[1]


def DecryptPassword(password):
    password = block_to_byte(password)
    op = ""
    for ind in range(8):
        for ans in range(128):
            inp = op + byte_to_char(ans)+(16-len(op)-2)*'f'
            if ord(password[ind]) == EAEAE(block_to_byte(inp), Linear_Transformation_Matrix, Exponentiation_Matrix)[ind]:
                op += byte_to_char(ans)
                break
    return op

left = block_to_byte(DecryptPassword(password_1))
right = block_to_byte(DecryptPassword(password_2))

print("password")
print(left + right)

