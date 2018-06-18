l = ['Hi\n', 'This is amazing!\n']
f = open("text.txt","w")
f.writelines(l)
f.close()

f=open("text.txt","r")
print(f.read())
f.close()