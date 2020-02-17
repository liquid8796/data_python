file=open("C:\\Users\\namtlh\\Desktop\\generate.txt","w+")
file.close()
file=open("C:\\Users\\namtlh\\Desktop\\generate.txt","a+")
def mapper():
    type=input("Type return: ")
    name=input("Function name: ")
    numParam=input("Number of param: ")


print("***Tool generate code by LIQUID***")
print("0. Generate mapper")
print("1. Generate component")
print("2. Generate componentImp")
print("3. Generate service")
print("4. Generate serviceImp")
print("Other. Quit")

