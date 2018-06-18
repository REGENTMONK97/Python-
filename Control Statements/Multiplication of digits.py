a = int(input("Enter an integer: "))
q = 1
m = 1
a1 = a
while q>0:
    q = int(a/10)
    m = m*int(a%10)
    a = a/10
print("Sum of digits of",a1,"is",m )