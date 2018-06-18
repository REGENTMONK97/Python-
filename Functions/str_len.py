def str_len1(s1,s2):
    s11 = len(s1)
    s12 = len(s2)
    if s11 == s12:
        print(s1)
        print(s2)
    elif s11>s12:
        print(s1)
    elif s12>s11:
        print(s2)

str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

str_len1(str1,str2)




