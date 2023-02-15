n = int(input("nhập n:"))
tong = 1
a=1
for i in range(0,n):
    a*=(2*(i+1))/(2*i+3)
    tong += a
print ( tong)