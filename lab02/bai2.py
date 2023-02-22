import math
a = float(input('Nhập vào hệ số a:'))
b = float(input('Nhập vào hệ số b:'))
c = float(input('Nhập vào hệ số c:'))
if a == 0:
    if b == 0:
        print('phương trình vô nghiệm')
    else:
        print('phương trình có nghiệm x =',b/c)
else:
    denta = b*b - 4*a*c
    if denta < 0:
        print('Phương trình vô nghiệm')
    elif denta == 0:
        print('Phương trình có nghiệm duy nhất x =',-b/(2*a))
    else:
        x1 = (-b+math.sqrt(denta))/(2*a)
        x2 = (-b-math.sqrt(denta))/(2*a)
        print('Phương trình có hai nghiệm phân biệt x1 = %f, x2 = %f'%(x1,x2))