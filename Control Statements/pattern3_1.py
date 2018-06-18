for i in range(1,9,1):
    if(i<=5):
        for j in range(0,i,1):
            print('*',end=' ')
        print()
    else:
        for k in range(0,9-i,1):
            print('*',end=' ')
        print()
