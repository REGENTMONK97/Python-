import sys
s = sys.argv[1:]
l = len(s)
for i in range(l):
    if '.' in s[i]:
        m = i
        #print(m)
print("Enter character to be searched")
c = sys.argv[m+2]
print(c)
print("Enter replacing character")
d = sys.argv[m+3]
print(d)
ss[5] = []
for i in range(m+1):
    ss[i] = s[i]
    sl = len(s[i])
    for j in range(sl):
        if c == ss[i][j]:
            print(i,j)
            ss[i][j] = d

print(ss)



