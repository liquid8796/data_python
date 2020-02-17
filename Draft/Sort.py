import random as r

def merge(S,S1,S2):
    i=j=0
    while (i+j<len(S)):
        if(j==len(S2) or (i<len(S1) and S1[i]<S2[j])):
           S[i+j]=S1[i]
           i+=1
        else:
            S[i+j]=S2[j]
            j+=1
def mergeSort(S):
    n=len(S)
    if n<2:
        return
    mid=n/2
    S1=S[0:int(mid)]
    S2=S[int(mid):n]
    mergeSort(S1)
    mergeSort(S2)
    merge(S,S1,S2)
def genArray(S):   
    count=0
    while count<1000000:
        tmp=[r.randint(0,1000000)]
        S+=tmp
        count+=1
S=[]
genArray(S)
mergeSort(S)
print(S)
count=0
