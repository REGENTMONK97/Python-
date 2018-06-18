i = int(input("Enter an integer"))
if i == 1 or i == 0:
    print("Enter a number greater than 2")
    exit()
k = i
while k > 2:
    k = k>>1
    print(k,end=" ")
    j = k%2
    print(j)
    if j!=0:
        print("The entered integer is not a power of 2")
        exit()
print("The entered number",i,"is a power of 2")

















