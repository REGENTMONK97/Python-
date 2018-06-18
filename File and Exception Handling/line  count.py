f = open("text.txt","r")
count = 0
g = f.readlines()
for i in g:
    if '\n' in i:
        count+=1
    else:
        print("No new lines")
print(count)