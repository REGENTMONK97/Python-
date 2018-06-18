f = open("text.txt","r+")
g = f.readlines()
f.close()

h = open("text1.txt","w+")
h.writelines(g)
try:
    h.seek(0,0)
    i = h.read()
except:
    print("Not able to read")
else:
    print(i)
h.close()
