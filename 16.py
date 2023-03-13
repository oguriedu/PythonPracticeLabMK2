x=int(input())
y=int(input())
z=[]
lst=[]  
for i in range(x):
    for j in range(y):
        z.append(i*j)
    lst.append(z)
    z=[]
print(lst)