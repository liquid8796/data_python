user=input("Enter username: ")
path="C:\\Users\\"+user+"\\Desktop\\generate.txt"
file=open(path,"w+")
file.close()
file=open(path,"a+")
def mapper():
    type=input("Type return: ")
    name=input("Function name: ")
    numParam=input("Number of param: ")
    file.write("//\n")
    file.write("@Select(\"\")\n")
    file.write(type+" "+name+"(")
    n=int(numParam)
    i=0
    print("Input param:")
    while (i<n):      
        tmp=input(str(i)+". ")
        if (i==0):          
            file.write("@Param(\""+tmp+"\") String "+tmp)
        else:
            file.write(", @Param(\""+tmp+"\") String "+tmp)
        i+=1
    file.write(");")
def component():
    type=input("Type return: ")
    name=input("Function name: ")
    numParam=input("Number of param: ")
    file.write("//\n")
    file.write(type+" "+name+"(")
    n=int(numParam)
    i=0
    print("Input param:")
    while (i<n):
        print(str(i)+".")
        name_tmp=input("name: ")
        if (i==0):
            file.write("String "+name_tmp)
        else:
            file.write(", String "+name_tmp)
        i+=1
    file.write(");")
def componentImp():
    type=input("Type return: ")
    name=input("Function name: ")
    numParam=input("Number of param: ")
    file.write("//\n")
    file.write("@Override\n")
    file.write("public "+type+" "+name+"(")
    n=int(numParam)
    i=0
    print("Input param:")
    while (i<n):
        print(str(i)+".")
        name_tmp=input("name: ")
        if (i==0):
            file.write("final String "+name_tmp)
        else:
            file.write(", final String "+name_tmp)
        i+=1
    file.write("){\n\treturn null;\n}")

print("***Tool generate code by LIQUID***")
print("0. Generate mapper")
print("1. Generate component & service")
print("2. Generate componentImp & serviceImp")
print("Other. Quit")
select=input("Select: ")
while (select=="0" or select=="1" or select=="2"):
    if(select=="0"):
        mapper()      
    if(select=="1"):
        component()
    if(select=="2"):
        componentImp()
    select=input("Select: ")

