a = int(input("Enter an integer: "))
if a==0:
    print("Factorial: ",1)
temp = a-1
fact = a
while temp>1:
    fact= fact*temp
    temp-=1
print("Factorial: ",fact)
