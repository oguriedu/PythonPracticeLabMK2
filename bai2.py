import math
n=int(input("moi nhap n: "))
tong=0
hieu=0
while True:
    if n<=0:
        n=int(input("moi nhap lai n: "))
        break
    for i in range(1,n+1):
        if i%2!=0:
            tong+=1/i
        if i%2==0:
            hieu+=-1/i
    if i==n:
        break

print(tong+hieu)

#b
n=int(input("moi nhap n: "))
tong=0
while n<=0:
    n=int(input("moi nhap lai n: "))
    if n>=0:
        break
for i in range(1,n+1):
    tong+=(1/i)*(1/(i+1))
    if i==n:
        break
print(tong)

#c
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