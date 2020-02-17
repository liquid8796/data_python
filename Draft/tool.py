file=open("C:\\Users\\namtlh\\Desktop\\generate.txt","w+")
file.close()
file=open("C:\\Users\\namtlh\\Desktop\\generate.txt","a+")
def mapper():
    type=input("Type return: ")
    name=input("Function name: ")
    numParam=input("Number of param: ")
    file.write("@Select(\"\")\n")
    file.write(type+" "+name+"(")
    n=int(numParam)
    i=0
    while (i<n):
        print("Input param:")
        tmp=input(str(i)+". ")
        if (i==0):          
            file.write("@Param(\""+tmp+"\") String "+tmp)
        else:
            file.write(", @Param(\""+tmp+"\") String "+tmp)
        i+=1
    file.write(");")
print("***Tool generate code by LIQUID***")
print("0. Generate mapper")
print("1. Generate component")
print("2. Generate componentImp")
print("3. Generate service")
print("4. Generate serviceImp")
print("Other. Quit")
select=input("Select: ")
while (select=="0" or select=="1" or select=="2" or select=="3" or select=="4"):
    if(select=="0"):
        mapper()
        break;
    select=input("Select: ")

