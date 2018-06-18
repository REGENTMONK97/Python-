#d = {'1':1;'2':4;'3':9}
dict = {}
dict['1'] = 1
dict['2'] = 4
dict['3'] = 9
print(dict)

for i in range(1,21,1):
    dict[str(i)] = i**2
print(dict.values())
print(dict.keys())


