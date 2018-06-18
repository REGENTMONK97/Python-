a = input("Enter all data separated by comma")
a = a.lstrip()
a1 = a.split(',')
tuple(a1)
#Fetching 4th element
print("The fourth element of the tuple is",end=" ")
print(tuple(a1)[3])

#Fetching 4th element from the last
print("The fourth element from the last of the tuple is",end=" ")
print(tuple(a1)[-4])
