file=open("data.txt","r")
line=file.read()
list=line.split(' ')
print("list len=",len(list))
x=input("Enter number to search: ")
n=len(list)

def search(S,S1,S2,x):
    i=j=0
    while (i+j)<len(S):
        if (j==len(S2) or (i<len(S1) and S1[i]!=x)):
            i+=1
        else:
            j+=1

def mergeList(S,x):
    n=len(S)
    mid=int(n/2)
    S1=S[0:mid]
    S2=S[mid:n]
    mergeList(S,x)

