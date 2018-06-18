a = int(input("Enter an integer: "))
temp  = a-1
count  = 0
while temp > 1:
    if a % temp == 0:
        pass
    else:
        count+=1
    temp-=1
print(count)
if count == a-2:
    print(a," is a prime number")
else:
    print(a," is not a primre number")





