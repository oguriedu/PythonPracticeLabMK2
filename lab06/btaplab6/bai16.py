#tạo mảng hai chiều
x=int(input('nhập x = '))
y=int(input('nhập y = '))
z=[]
lst=[]  
for i in range(x):
    for j in range(y):
        z.append(i*j)
    lst.append(z)
    z=[]
print(lst)