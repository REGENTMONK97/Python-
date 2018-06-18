from sys import argv
l = []
print("Enter number of elements in the list")
n = int(argv[1])
count = 0
for i in range(2,n+2,1):
    l.append(argv[i])
for i in range(n):
    if int(l[i]) == 2 or int(l[i]) == 1:
        count+=1
    else:
        for j in range(2, int(l[i]), 1):
            if int(l[i])%j == 0:
                break
        else:
            count+=1
print"No of prime numbers are:", count


