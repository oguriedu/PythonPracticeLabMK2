n= int(input("Nhập số n:"))
tong=1
s=1
for i in range (0, n):
    s*=(2*(i+1))/(2*i+3)
    tong+=s
print(tong)