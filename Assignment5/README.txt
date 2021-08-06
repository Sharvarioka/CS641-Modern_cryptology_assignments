Step 1:
Create an input folder to store the input plaintext files.
run.sh -> uses 1_Input_Generation.py and 2_out_cipheronly.py to generate plaintext and corresponding encrypted text from server.
1_Input_Generation.py requires :
Output file: input.txt
2_out_cipheronly.py requires :
Input file: output.txt which consists of terminal output which is cleaned and stored in  out_cipher.txt.

Step 2:
3_Decrypt_Cipher.py
Input file: input.txt, out_cipher.txt
Output: Possible diagonal elements, possible corresponding exponents, linear transformation matrix, exponentiation matrix, password.
