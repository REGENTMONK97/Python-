from sys import argv
s = []
print("Enter the number of elements")
n = int(argv[1])
for i in range(2, n+2, 1):
    s.append(argv[i])
M = max(s)
m = min(s)

print("Largest number is ",M)
print("Smallest number is ",m)
