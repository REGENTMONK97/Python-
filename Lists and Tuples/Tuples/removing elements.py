a = input("Enter all data separated by comma")
a = a.lstrip()
a1 = a.split(',')
tuple(a1)
e = input("Enter the element to be deleted")
e = e.lstrip()
count = 0
#l = len(tuple(a1))

if e in a1:
    a1.remove(e)
else:
    print(e," is not present in ",tuple(a1))
print(tuple(a1))

        #print("True")
        #for j in range(i+1,l,1):
         #   a1[j-1] = a1[j]
          #  print(a1[j])
           # count = 1
        #del(a1[l-1])
        #l = l-1
#if count == 1:
 #   tuple(a1)

#if count == 0:
    #print("Element ",e," is not present in the tuple")
    #exit()
#print(tuple(a1))

