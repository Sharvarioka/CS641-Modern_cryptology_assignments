README
step 1:
run.sh -> uses 1_generate_text.py and 2_out_cipheronly.py to generate cipher and corresponding encrypted text from server ->input.txt, output.txt, out_cipher.txt


step 2:
run 3_Differential.py
input file: out_cipher.txt
output files: XS_inp_14.txt, XS_out_14.txt, XExp_out_14.txt

step 3:
run 4_SBox.py
input files:
XS_inp_14.txt, XS_out_14.txt, XExp_out_14.txt
output: master key where 20 bits are missing

step 4:
Run 5_Key_Generator.py
generates 2^20 possible keys
output file:Keys_14.txt


In order to check whether the key is correct we used Plain=ffffffffffffffff whose corresponding ciphertext=fkomknkt'tnoiuksq. 
The decimal conversion for ciphertext is 5,151,88,94,232,147,245,219.We get this decimal conversion by using decimal_to_dec.py . 
This plain and ciphertext pair is used to calculate the key in n which we use in 6_desbrute.cpp .

step 5:
run 6_desbrute.cpp
output: return required key

step 6:
run 7_DES.cpp seperately with 'left' plain and then 'right' plain. where,
left plain={228,226,136,110,58,90,64,69,'\0'};
and right plain[]={70,210,47,89,150,226,5,32,'\0'};

Step 7:
output:
116 108 119 117 106 100 101 112 105 117 48 48 48 48 48 48

Now conver then in ASCII we get 
tlwujdepiu
