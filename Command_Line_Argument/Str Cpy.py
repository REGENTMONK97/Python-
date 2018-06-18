import sys
s = sys.argv[1:]
l = len(s)
for i in range(l):
    if '.' in s[i]:
        m = i
        print("true")
        s = sys.argv[1:m + 2]
        t = sys.argv[m + 2:]
        print(s)
        print(t)
        print("Strs after copying")
        t = s
        print(s)
        print(t)



