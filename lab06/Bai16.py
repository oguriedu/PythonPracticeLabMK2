x=int(input('Nhập X = '))
y=int(input('Nhập Y = '))
z=[]
t=[]  
for i in range(x):
    for j in range(y):
        z.append(i*j)
    t.append(z)
    z=[]
print(t)
            