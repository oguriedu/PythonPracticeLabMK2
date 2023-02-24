n=int(input('nhập số nguyên dương n:'))
s4=0
s5=0
s6=0
if n<=0:
    print('mời bạn nhập lại:')
else:
    for i in range(0,n+1):
        s4=i**2
    for i in range(1,n+1):
        s5=(2*i+1)**3
    for i in range(0,n+1):
        s6=(2*i)**4
print('s4=',s4)
print('s5=',s5)
print('s6=',s6)