from fractions import *
a=int(input('Nhập tử số :'))
b=int(input('Nhập mẫu số :'))
while b==0:
    print('Nhập lại mẫu số.')
    b=int(input('Nhập mẫu số :'))
    break
print('Phân số bạn vừa nhập là :',Fraction(a,b))