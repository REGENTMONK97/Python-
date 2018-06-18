l1 = []
for i in range(1000,3001,1):
    q = 1
    i1 = i
    count = 0
    while q>0:
        q = int(i/10)
        m = int(i % 10)
        if m % 2 == 0:
            count += 1
        i = i/10
    if count == 4:
        l1.append(i1)
print(l1)


