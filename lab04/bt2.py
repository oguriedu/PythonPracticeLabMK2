n=int(input("Nhập giới hạn:"))
i1=-1
tong1=0
i2=0
tong2=0
while i1<n:
    i1=i1+1
    tong1+=1/(2*i1+1)
print("câu a.S =",tong1)
while i2<n:
    i2=i2+1
    tong2-=1/(2*i2)
print("câu b.S =",tong2)
# c.
import math
n1=int(input("Nhập giới hạn:"))
i3=-1
tong3=0
while i3<n:
    i3+=1
    tong3+=1/(math.sqrt(2+i3))
print("câuc S=",tong3)