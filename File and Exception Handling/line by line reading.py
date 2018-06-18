f = open("name.txt", "r")
l = []
m = f.readlines()
for i in m:
    for j in i:
        if '\n':
            i.replace('\n', '')
    l.append(i)
print(l)