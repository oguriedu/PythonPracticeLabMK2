n = int(input('Nhập n: '))
tong = 1
a = 1
for i in range(0,n+1):
    tong*=(2*i+2)/(2*i+3)
    a+=tong
print(a)