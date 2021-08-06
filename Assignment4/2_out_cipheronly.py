mylines=[]
f = open('output.txt', 'rt')
f1=open('out_cipher.txt','a+')
word ="shivers"
count=461
current=1
for line in f:  
	if current==count and word not in line:
		count=count+15                 
		mylines.append(line.lstrip("		")) 
		f1.write(line.lstrip("		"))
	current=current+1             
f1.close()
#print(mylines)