a = int(input("Enter an integer: "))
f = 0
i = 1
j = 0

print("The fibonacci numbers up till ",a," is: 0,",end = "")
while f<=a:
    f = i+j
    i = f
    j = i
    if f<a:
        print(f, end=",")





