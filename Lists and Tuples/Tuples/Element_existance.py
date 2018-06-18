b = []
a = input("Enter all data separated by comma")
a = a.lstrip()
a1 = a.split(',')
tuple(a1)

#Finding repeated elements in tuple
print(tuple(a1))

l = len(tuple(a1))
count = 0
e =input("Enter the element to be searched: ")
e = e.lstrip()

for i in range(0,l,1):
    #print(str(tuple(a1)[i]))
    if e == str(tuple(a1)[i]):
            count+=1
if count>=1 :
    print("The element ", e, " is present")
else:
    print("The element ", e, " is  not present")



