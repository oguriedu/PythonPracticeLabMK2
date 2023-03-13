import math
a=float(input('Nhập vào số a :'))
b=float(input('Nhập vào số b :'))
c=float(input('Nhập vào số c :'))
# x=1
delta=(b**2)-4*a*c
# y=a*x^2+b*x+c
if delta==0:
    x=-b/(2*a)
    print(f'Phương trình có nghiệm x = {x:.2f}')
elif delta>0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'Phương trình có 2 nghiệm : \n x1 = {x1:.2f} \n x2 = {x2:.2f}')

