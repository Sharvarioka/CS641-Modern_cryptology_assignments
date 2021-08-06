#!/bin/sh

a=0

until [ $a -gt 1000 ]
do
        python3 1_generate_text.py
        ssh -tt student@65.0.124.36 <input.txt >output.txt
        python3 2_out_cipheronly.py

   a=`expr $a + 1`
done

