a = int(input("Enter an integer: "))
q = 1
m = 0
a1 = a
while q>0:
    q = int(a/10)
    m = m*10+int(a%10)
    a = a/10
print(m)
if m == a1:
    print(a1, "is palindrome")
else:
    print(a1," not a palindrome")
