a = int(input("Enter an integer: "))
ano = 0
a1 = a
q = 1
while q>0:
    q = a/10
    m = int(a%10)
    ano = ano + m**3
    a = a/10
    #print(ano)
if ano == a1:
    print("The number is armstrong")
else:
    print("The number is not armstrong")