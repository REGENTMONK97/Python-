b = []
a = input("Enter all data separated by comma")
a = a.lstrip()
a1 = a.split(',')
tuple(a1)

#Finding repeated elements in tuple

l = len(tuple(a1))

for i in range(0,int(l/2)+1,1):
    count = 1
    for j in range(l-1-i,i,-1):
        #print(tuple(a1)[j],end=' ')
        if tuple(a1)[i] == tuple(a1)[j]:
            count+=1
    print(count)
    if count>1:
        b.append(tuple(a1)[i])
    print()

print(tuple(b))


