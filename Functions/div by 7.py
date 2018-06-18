import sys
if len(sys.argv) == 2:
    n = int (sys.argv[1])
    if n%7 == 0:
        print(n)
    else:
        print('not divisibe by 7')
