from math import sqrt
a=float(input('Nhập a:'))
b=float(input('Nhập b:'))
c=float(input("Nhập c:"))
if a==0:
    if b==0 and c==0:
        print('vố số nghiệm')
    elif b==0 and c !=0:
        print('Vô nghiệm')
    else:
        x=-c/b
        print('Nghiệm x=',x)
else:
    delta=b**2-4*a*c
    if delta<0:
            print('Vô nghiệm')
    elif delta==0:
            x=-b/(2*a)
            print('Nghiệm kép x1=x2=',x)
    else:
            x1=(-b-sqrt(delta))/(2*a)      
            x2=(-b+sqrt(delta))/(2*a)    
            print('x1= %0.2f'%x1)
            print('x2= %0.2f'%x2)
