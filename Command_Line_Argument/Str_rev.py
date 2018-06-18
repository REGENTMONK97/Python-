import sys
s = sys.argv[1:]
l = len(s)
for i in range(int(l/2)):
    temp = s[l-i-1]
    print(temp)
    s[l-1-i] = s[i]
    s[i]= temp
print(s)