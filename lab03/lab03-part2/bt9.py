import math
n = int(input("nhập số n:"))
while n<=0:
    print("Nhập sai xin vui lòng nhập lại")
    n = int(input("nhập số n:"))
s4=0
s5=1
s6=0
for i in range(1,n+1):
    s4+=(i**2)
    s5+=((2*i+1)**3)
    s6+=((2*i)**4)
print('S4 = ',s4)
print('S5 = ',s5)
print('S6 = ',s6)