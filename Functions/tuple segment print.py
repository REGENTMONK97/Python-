t = (1,2,3,4,5,6,7,8,9,10)

def tuple_print(t):
    t = list(t)
    n = len(t)
    for i in range(int(n/2)):
        print(t[i],end=' ')
    print()
    for i in range(int(n/2),n,1):
        print(t[i],end=' ')

tuple_print(t)
