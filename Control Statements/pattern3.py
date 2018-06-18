for i in range(0,8,1):
    for j in range(1,5-i,1):
        pass
    if j<=0:
        for k in range(0,8-i,1):
            pass
        print('* '*k)
    else:
        print('* '*j)
