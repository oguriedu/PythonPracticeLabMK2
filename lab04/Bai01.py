s4=0
s5=0
s6=0
while True :
    n=int(input('Nhập n = '))
    if n>0:
        i=int(1)
        while i<=n:
            s4+=i**2
            s5+=(2*i+1)**3
            s6+=(2*i)**4
            i+=1
        print('S4 = ',s4)
        print('S5 = ',s5)
        print('S6 = ',s6)
        break
        
