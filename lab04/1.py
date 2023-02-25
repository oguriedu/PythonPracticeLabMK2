# Viết chương trình tính tổng bằng vòng lặp (while)
n=int(input("Nhập số nguyên dương:"))
if n<=0:
    print("Nhập lại")
    n=int(input("Nhập số nguyên dương"))
i1=0
i2=-1
i3=0
tong1=0
tong2=0
tong3=0
while i1<n:
    i1=i1+1
    tong1+=(i1**2)
print("Tổng S4:",tong1)
while i2<n:
    i2=i2+1
    tong2+=((2*i2+1)**3)
print("Tổng S5:",tong2)
while i3<n:
    i3=i3+1
    tong3+=(i3*2)**4
print("Tổng S6:",tong3)




