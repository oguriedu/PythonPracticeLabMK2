n=int(input("moi nhap n: "))
tong=0
if n<=0:
    print('moi nhap lai n')
for i in range(0,n+1):
    tong+=i**2
print(tong)