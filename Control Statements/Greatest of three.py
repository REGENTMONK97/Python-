a = int(input("The first number"))
b = int(input("The second number"))
c = int(input("The third number"))

temp = a
if temp>=b:
    if temp>c:
        print("The greatest of the three numbers is ",a)
        exit()
    else:
        temp = b
if temp>=a:
    if temp>c:
        print("The greatest of the three numbers is ",b)
        exit()
    else:
        temp = c
if temp>=a:
    if temp>b:
        print("The greatest of the three numbers is ",c)
        exit()
elif a == b == c:
    print("All three numbers are equal")
