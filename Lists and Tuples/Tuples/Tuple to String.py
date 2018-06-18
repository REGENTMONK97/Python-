b = []
a = input("Enter all data separated by comma")
a = a.lstrip()
a1 = a.split(',')
tuple(a1)
print("The tuple is",end=" ")
print(b)

s = ','.join(tuple(a1))
print("The string cversion of Tuple is: ",end=" ")
print(s)



