
#i = int(input("Enter the elements separated by comma"))
#a.append(i)
#if ',' in i:
 #   print("Found you!")
#    a.remove(',')

#b = list(a)
#print(i)


#for i in range (0,2,1):


#for i in range(0,2,1):
 #   j = input("Enter the elements ")
  #  a.append(j)
#print(a)
#a.sort()
#print(a)
#if ',' in j:
#    print("Found you!")
#    a =

b =[]
j = input("Enter the elements by comma")
j = j.lstrip()
j1 = j.split(',')
print(j1)
a = list(j1)
k = len(a)
for i in range(0,k,1):
    a[i] = int(a[i])
    #print(a[i])
    if a[i]%2!=0:
       b.append(a[i])
print(b)




#l = len(j)
#for i in range (0,l,1):
 #   if ',' in j:
  #      k = j.index(',')
   # j = j.split(0,k)
    #print(k,end=' ')


