f = open("text.txt","r")
g = open("text1.txt","r")


m = f.readlines()
n = g.readlines()

o = zip(m,n)
print(*o)