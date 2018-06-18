s = input("Enter the numbers: ")
l = s.split(' ')
n = len(l)

temp = int(l[0])
for i in range(n):
    if int(l[i]) > temp:
      temp = int(l[i])
print(temp)


