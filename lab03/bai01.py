n=int(input("Nhập n:"))
tong=1
tich=1
for i in range(0,n+1):
    tich*=(2*(i+1)/(2*n+3))
    tong+=tich
print(round(tong,3))
