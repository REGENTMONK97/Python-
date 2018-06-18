a = int(input("Enter an integer: "))
b = int(input("Enter an integer to be checked in the word: "))
q = 1
a1 = a
count = 0
while q>0:
    q = int(a/10)
    m = int(a%10)
    if b==m:
        count+=1
    a = a/10
print("The number of occurrences of ",b," in ",a1," is: ",count)