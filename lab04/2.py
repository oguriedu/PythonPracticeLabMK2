# Tính tổng
# a. S=1/1-1/2+1/3-1/4+1/5-............
n=int(input("Nhập giới hạn:"))
i1=-1
tong1=0
i2=0
tong2=0
while i1<n:
    i1=i1+1
    print(1,"/",(2*i1+1)," (+) ")
    tong1+=1/(2*i1+1)
while i2<n:
    i2=i2+1
    print(1,"/",(2*i2)," (-) ")
    tong2-=1/(2*i2)
print("a.S =",tong1+tong2)

# c. S=1/căn2+1/căn3+1/căn4+.......
import math
n1=int(input("Nhập giới hạn:"))
i3=-1
tong3=0
while i3<n:
    i3+=1
    print(1,"/ căn",(2+i3))
    tong3+=1/(math.sqrt(2+i3))
print("b. S=",tong3)

    