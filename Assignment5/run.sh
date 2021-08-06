#!/bin/ bash

python3 1_Input_Generation.py

ssh -tt student@65.0.124.36 <input/input1_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input1_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input2_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input2_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input3_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input3_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input4_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input4_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input5_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input5_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input6_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input6_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input7_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input7_2.txt >output.txt
python3 2_out_cipheronly.py 1
ssh -tt student@65.0.124.36 <input/input8_1.txt >output.txt
python3 2_out_cipheronly.py 0
ssh -tt student@65.0.124.36 <input/input8_2.txt >output.txt
python3 2_out_cipheronly.py 1
