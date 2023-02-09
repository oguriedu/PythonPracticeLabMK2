a=[]
while True:
    nhap=int(input("moi nhap toa do diem thu 1: "))
    a.append(nhap)
    if len(a)==2:
        break
b=[]
while True:
    nhap2=int(input("moi nhap toa do diem thu 2: "))
    b.append(nhap2)
    if len(b)==2:
        break
c=[]
while True:
    nhap3=int(input("moi nhap toa do diem thu 3: "))
    c.append(nhap3)
    if len(c)==2:
        break
d=[]
for i in range (len(a)):
    for j in range( len(b)):
        for o in  range(len(c)):
            cong=a[0]+b[0]+c[0]
            trong_tam=cong/3
            cong2=a[1]+b[1]+c[1]
            trong_tam2=cong2/3
d.append(trong_tam)
d.append(trong_tam2)
print(d)            