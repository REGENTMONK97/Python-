l1 = []
l2 = []
for i in range(2000,3001,1):
    if i%7==0 and i%5!=0:
        l1.append(i)
    if i%35 == 0:
        l2.append(i)
print(l1) # div by 7 but not 5
print(l2) # div by 7 and 5



