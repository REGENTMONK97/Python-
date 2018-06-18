#You have a record of students.
#Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
#The marks can be floating values.
#The user enters some integer followed by the names and marks for students.
#You are required to save the record in a dictionary data type.
#The user then enters a student's name.
#Output the average percentage marks obtained by that student, correct to two decimal places.

name = []
m1 = []
m2 = []
m3 = []
d = {}
n = int(input("Nos: "))
for i in range(n):
    name1 = input("Name: ")
    name.append(name1)
    m11 = float(input("M1"))
    m1.append(m11)
    m21 = float(input("M2"))
    m2.append(m21)
    #m31 = float(input("M3:"))
    #m1.append(m31)
    #m41 = float(input("M4:"))
    #m1.append(m41)
d = zip(name,m1,m2)
print(d)

