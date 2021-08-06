import sys

num = int(sys.argv[1])
mylines=[]
f = open('output.txt', 'rt')
f1=open('out_cipher.txt','a+')
word ="shivers"
count=263
current=1
for line in f:  
    if current==count and word not in line:
        count=count+15                 
        mylines.append(line.lstrip("		")) 
    current=current+1 

k=0            
for i in mylines:
    #f1.write(line.lstrip("		"))
    if k==64:
        break;
    f1.write(i[:16])
    f1.write(" ")
    #f1.seek(0, os.SEEK_END)
    #f1.truncate()
    k=k+1
if num == 0:
    f1.write("")
if num == 1:
    f1.write("\n")
f1.close()