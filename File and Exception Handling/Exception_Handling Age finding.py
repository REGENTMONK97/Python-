c = False
while c == False:
    try:
        a = int(input("Enter age: "))
        if a>0:
            if a%2 == 0:
                print("even age")
            else:
                print("odd age")
            c = True
        else:
            raise Exception
    except Exception:
        print("Enter valid age!")
        c = False