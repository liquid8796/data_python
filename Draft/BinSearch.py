def search(S,S1,S2,x):
    i=j=0
    while (i+j)<len(S):
        if (j==len(S2) or i<len(S1)):
            if (S1[i]!=x):
                i+=1
            else:
                return S1[i]
        else:
            if(S2[j]!=x):
                j+=1
            else:
                return S2[j]
    return -1

def mergeList(S,x):
    n=len(S)
    if n<2:
        return S[n-1]
    mid=int(n/2)
    S1=S[0:int(mid)]
    S2=S[int(mid):n]
    mergeList(S1,x)
    mergeList(S2,x)
    result=search(S,S1,S2,x)
    return result

file=open("data.txt","r")
line=file.read()
list=line.split(' ')
print("list len=",len(list))
x=input("Enter number to search: ")
n=len(list)
result=mergeList(list,x)
if (result!=-1):
    print("Found "+result)
else:
    print(x+" not found!")



