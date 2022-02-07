secure = (("a", "@"),("i","!"),("o","0"),("s","$"),("and","&"))

def securepass(password):
    for a,b in secure :
     password= password.replace(a,b) # a = input b = output if a= o b conbert it by tuple value 0 bcz we set it ("o","0")
    return password
s = input("Enter your Password : ")
y = securepass(s)

print(y)