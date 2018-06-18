#Apple A Day Keeps Doctor Away
a = input("Enter a sentence")
a = a.lstrip()
a1 = a.split(" ")
print(a1)

l = len(a1)
count1 = 0
count2 = 0
for i in range(0,l,1):
    #print(a1[i])
    str(a1[i])
    m = len(str(a1[i]))
    print(m)
    for j in range(0,m,1):
        #print(a[i][j])
        if a1[i][j]>='a' and a1[i][j]<='z':
            count2+=1
        if a1[i][j]>='A' and a1[i][j]<='Z':
            count1+=1

print("The number of lower case letters: ",count2)
print("The number of upper case letters: ",count1)