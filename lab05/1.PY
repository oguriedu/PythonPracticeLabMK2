n=input("nhap so: ")
s=0
for i in n:
    if i.isnumeric()==True:
        s+=1
    else:
        continue
print(s)