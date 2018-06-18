import sys
m = 0
s = sys.argv[1:]
l = len(sys.argv[1:])
for i in range(l):
    m = m + len(s[i])
print(m)
