s = input()
l = s.split(' ')
n = len(l)

count = 0
temp = int(l[0])
for i in range(n):
    if int(l[i]) > temp:
        temp = int(l[i])
for i in range(n):
    if temp == int(l[i]) :
        l[i] =''
        count+=1
n = n - count
print(n)
temp = int(l[0])
for i in range(n):x
    if int(l[i]) > temp:
        temp = int(l[i])
        print(temp

