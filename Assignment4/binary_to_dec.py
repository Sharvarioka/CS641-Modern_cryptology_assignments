char_map = {"f": "0000", "g": "0001", "h": "0010", "i": "0011", "j": "0100", "k": "0101","l":"0110", "m":"0111",
                "n": "1000","o": "1001", "p": "1010","q":"1011","r":"1100","s":"1101","t":"1110","u": "1111"}

reverse_char_mapping={}   #reverse_char_mapping contains {"0000":f ....... "1111":u}
for ele in char_map:
	reverse_char_mapping[char_map[ele]]=ele

# print(char_map_rev) 

s=['tj','th','nn','lt','ip','kp','jf','jk','jl','sh','hu','ko','ol','th','fk','hf']

def binary_to_dec(num):
	bnum = int(num)
	dnum = 0
	m = 1
	blen = len(str(bnum))
	for k in range(blen):
	    rem = bnum%10
	    dnum = dnum + (rem * m)
	    m = m * 2
	    bnum = int(bnum/10)
	print("\nEquivalent Decimal Value of "+s[i][0]+s[i][1]+" = ", dnum)


for i in range(0,16):
	n=char_map[s[i][0]]+char_map[s[i][1]]
	binary_to_dec(n)

	





