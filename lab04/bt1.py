n=int(input('nhap n:'))
if n<=0:
    n=int(input('nhap n:'))
i1=0
i2=-1
i3=0
tong1=0
tong2=0
tong3=0
while i1<n:
    i1=i1+1
    tong1+=(i1**2)
print("Tổng S1:",tong1)
while i2<n:
    i2=i2+1
    tong2+=((2*i2+1)**3)
print("Tổng S2:",tong2)
while i3<n:
    i3=i3+1
    tong3+=(i3*2)**4
print("Tổng S3:",tong3)
