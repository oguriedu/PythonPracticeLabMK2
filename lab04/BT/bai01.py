#a
n = int(input("Nhập n: "))
while n<=0:
    n = int(input("Nhập n > 0: "))
s4=0
a=1
while n!=(n+1):
    s4+=a**2
    a+=1
print('S4= ',s4)
#b
s5=0
a=1
while a!=(n+1):
    s5+=(2*a+1)**3
    a+=1
print('S5= ',s5)
#c
s6=0
a=1
while a!=(n+1):
    s6+=(2*n)**4
    a+=1
print('S6=',s6)