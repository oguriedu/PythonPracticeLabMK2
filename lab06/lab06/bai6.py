import random
a=[]
for i in range(0,1000):
    ngau_nhien=random.randrange(1,99999)
    a.append(ngau_nhien)
#dùng hàm sorted
b=a.copy()
print(sorted(b))
#không dùng hàm sorted
for j in range(len(a)):
    for k in range(j):
        if a[j]<a[k]:
            lon_hon=a[j]
            a[j]=a[k]
            a[k]=lon_hon
print(a)