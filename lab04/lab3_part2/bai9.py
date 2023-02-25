n = int(input('nhập n'))
s4=0
s5=0
s6=0
for i in range(1,n+1):
    if n<=0:
        print('bạn vui lòng nhập lại')
        n = int(input('nhập n'))
    if n>0:
        s4+=n**2
        s5+=(2*n+1)**2
        s6+=(2*n)**4
        n=n+1
    print('s4=',s4)
    print('s5=',s5)
    print('s6=',s6)
    break