#giải pt bậc 2
import math

a = int(input('Nhập giá trị của a: '))
b = int(input('Nhập giá trị của b: '))
c = int(input('Nhập giá trị của c: '))
z = b**2-4*a*c
if a==0 and b==0:
    if c==0:
        print('Phương trình có vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')
elif a==0 and b!=0:
    print('Phương trình có nghiệm duy nhất x =',-c/b)
elif a!=0:
    if z<0:
        print('Phương trình vô nghiệm')
    elif z==0:
        print('Phương trình có nghiệm kép x =',-b/2/a)
    else:
        print('Phương trình có 2 nghiệm phân biệt x1 =',(-b+math.sqrt(z))/2/a,'x2 =',(-b-math.sqrt(z))/2/a)