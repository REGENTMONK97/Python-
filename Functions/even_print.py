t = (1,2,3,4,5,6,7,8,9,10)

def even_print(t):
    l = []
    t = list(t)
    n = len(t)
    for i in range(n):
        if t[i]%2 ==0:
            l.append(t[i])
    l = tuple(l)
    print(l)

even_print(t)