#Nhập n số nguyên dương(tính tổng- vòng lặp while)
n = int(input("Nhập n: "))
while n<=0:
    n = int(input("Nhập n > 0: "))
s4=0
s5=0
s6=0
a=1
while a!=(n+1):
    s4+=a**2
    s5+=(2*a+1)**3
    s6+=(2*n)**4
    a+=1
print('S4= ',s4)
print("S5=",s5)
print("S6=",s6)