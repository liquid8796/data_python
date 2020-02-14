import random as r

def genArray(S):   
    count=0
    while count<1000000:
        tmp=[r.randint(0,1000000)]
        S+=tmp
        count+=1
file=open("data.txt","w+")
file.close()
file=open("data.txt","a+")
S=[]
genArray(S)
count=0
while count<1000000:
    file.write(str(S[count])+" ")
    count+=1
file.close()

    

