f = open("text.txt", "r")
n = int(input("Enter the number of lines to read"))
f.seek(0, 2)
l = [1,n,1]
r = f.readline(l)
print(r)



