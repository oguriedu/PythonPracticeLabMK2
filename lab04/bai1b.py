n=int(input("moi nhap n: "))
tong=0
while True:
    if n<=0:
        n=int(input("moi nhap lai n: "))
    for i in range(0,n+1):
        tong+=(2*i+1)**3
    if i==n:
        break
print(tong)