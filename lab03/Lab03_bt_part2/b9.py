n=int(input('Nhập n :'))
if n<=0:
    print('Nhập sai .Mời nhập lại n>0')
    n=int(input('Nhập n: '))
s4=0
s5=0
s6=0
for i in range(1,n+1):
    k1=i*i
    k2=(2*i+1)**3
    k3=(2*i)**4
    s4+=k1
    s5+=k2
    s6+=k3
print('tổng S4 là ',s4)
print('tổng S5 là ',s5)
print('tổng S6 là ',s6)