n=int(input("Nhập giá trị của n: "))
s=1
m=1
for i in range(0,n+1):
    a=(2*(n+1))/((2*n)+3)
    m*=a
    s+=m
print("Tổng là: %0.3f"%s)
