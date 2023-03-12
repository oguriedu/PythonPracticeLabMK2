n=int(input("so phan tu cua:"))
a=[]
c=[]
for i in range(1,n+1):
    b=int(input("nhaap soos :"))
    a.append(b)
    c.append(b)
a.remove(max(a))
d=max(a)
print('so lon thu nhi la:',d)
for num in c:
    if num==d:
        print('vi tri cua phan tu lon thu nhi la:',c.index(d))

