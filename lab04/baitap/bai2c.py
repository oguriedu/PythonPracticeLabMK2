import math
n=int(input("moi nhap n: "))
tong=0
while n<=0:
    n=int(input("moi nhap lai n: "))
    if n>=0:
        break
for i in range(1,n+1):
    tong+=1/math.sqrt(i+1)
    if i==n:
        break
print(tong)