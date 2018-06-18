#Bit Setting
str = input("""Enter the Bit operation to be performed:
               Bit Setting,
               Bit Clearing,
               Bit Compliment:    """)
i = int(input("Enter the number to be manipulated"))

if str == "Bit Setting":
    k = int(input("Enter the bit number to be set"))
    m = 2 ** (k-1)
    f = i | m
#Bit Clearing
if str == "Bit Clearing":
    k = int(input("Enter the bit number to be cleared"))
    m = 2 ** (k-1)
    m = ~m
    f = i & m
if str == "Bit Compliment":
    k = int(input("Enter the bit nuumber to be complimented"))
    m = 2 ** (k-1)
    f = i^m
print(f)



