class square():
    def squarelist():
        l = []
        for i in range(1, 21, 1):
            l.append(i ** 2)
        print(l)
    def squaretuple():
        l = []
        for i in range(1, 21, 1):
            l.append(i ** 2)
        l = tuple(l)
        print(l)
square.squarelist()
square.squaretuple()

