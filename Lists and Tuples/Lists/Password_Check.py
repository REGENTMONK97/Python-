j = input("Enter the passwords separated by comma")
j = j.lstrip()
a = list(j.split(','))
b = []
l = len(a)
for i in range(0,l,1):
        m = len(a[i])
        count1=0 ; count2=0 ; count3 =0 ; count4 = 0
        if m>=6 and m<=12:
            for j in range(0, m, 1):
                if a[i][j] >= 'a' and a[i][j] <= 'z':
                    count1 = 1
                if a[i][j] >= 'A' and a[i][j] <= 'Z':
                    count2 = 1
                if a[i][j] >= '0' and a[i][j] <= '9':
                    count3 = 1
                if a[i][j] == '$' or a[i][j] == '#' or a[i][j] == '@':
                    count4 = 1
            if count1>= 1 and count2>=1 and count3 >=1 and count4 >=1:
                b.append(a[i])
print(b)



    #for i in range(0, l, 1):
     #   print(a[i].isalpha())
      #  if a[i].isalpha():
       #     print(a[i].isalpha())
        #    if a[i].isnumeric():
         #       if a[i].isupper():
          #          b.append(a[i])
#print(b)
